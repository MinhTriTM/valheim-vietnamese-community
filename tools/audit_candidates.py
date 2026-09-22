"""Ưu tiên rà soát bản dịch bằng các tín hiệu tĩnh, không tự duyệt nghĩa."""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

from import_local import signature


def inspect(source, target):
    issues = []
    original = source["source"].strip()
    translated = target["vi"].strip()
    if signature(original) != signature(translated):
        issues.append("token_mismatch")
    if original and original.casefold() == translated.casefold() and len(original) > 12:
        issues.append("unchanged_english")
    if len(original) >= 25 and (len(translated) > len(original) * 3 or len(translated) < len(original) / 4):
        issues.append("length_outlier")
    if re.search(r"[\u0400-\u052f\u0590-\u08ff\u3040-\u30ff\u3400-\u9fff\uac00-\ud7af]", translated) and not target["key"].startswith("language_"):
        issues.append("non_latin_script")
    if source["conflict"]:
        issues.append("source_conflict")
    return issues


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-catalog", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    sources = {row["key"]: row for row in (json.loads(line) for line in args.source_catalog.read_text(encoding="utf-8").splitlines())}
    records = [json.loads(line) for path in (root / "data" / "valheim").glob("*_draft.jsonl") for line in path.read_text(encoding="utf-8").splitlines()]
    counts = Counter()
    flagged = []
    for target in records:
        source = sources.get(target["key"])
        if not source:
            counts["missing_source"] += 1
            continue
        issues = inspect(source, target)
        for issue in issues:
            counts[issue] += 1
        if issues:
            flagged.append({"key": target["key"], "issues": issues})
    report = {"records": len(records), "flagged_records": len(flagged), "signals": dict(counts), "flagged": flagged}
    output = root / "local" / "translation_audit.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(records)} bản ghi, {len(flagged)} cần ưu tiên rà soát: {dict(counts)}")


if __name__ == "__main__":
    main()
