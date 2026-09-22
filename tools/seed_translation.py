"""Tạo ứng viên dịch công khai từ bộ dịch có giấy phép, luôn ở trạng thái draft."""
import argparse
import json
from collections import Counter
from pathlib import Path

from import_local import signature


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-catalog", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--origin", required=True)
    parser.add_argument("--origin-build", required=True)
    parser.add_argument("--game-build", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    data_root = (root / "data").resolve()
    output = args.output.resolve()
    if data_root not in output.parents:
        raise ValueError("Đầu ra phải nằm trong data/")
    local_root = (root / "local").resolve()
    if local_root not in args.source_catalog.resolve().parents:
        raise ValueError("Source catalog phải nằm trong local/")
    sources = [json.loads(line) for line in args.source_catalog.read_text(encoding="utf-8").splitlines()]
    candidates = json.loads(args.candidate.read_text(encoding="utf-8-sig"))
    if not isinstance(candidates, dict):
        raise ValueError("Candidate phải là JSON object")
    report = Counter()
    rows = []
    for source in sources:
        key = source["key"]
        value = candidates.get(key)
        if source["conflict"]:
            report["source_conflict"] += 1
            continue
        if not isinstance(value, str) or not value.strip():
            report["missing_candidate"] += 1
            continue
        if signature(source["source"]) != signature(value):
            report["token_mismatch"] += 1
            continue
        rows.append({
            "namespace": "valheim", "key": key,
            "source_sha256": source["source_sha256"],
            "technical_signature": source["technical_signature"],
            "vi": value, "status": "draft", "origin": args.origin,
            "game_build": args.game_build, "mod_version": "", "reviewer": "",
            "translation_origin_build": args.origin_build,
            "source_asset": source["asset"], "origin_license": "MIT",
        })
        report["draft"] += 1
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    report["source_total"] = len(sources)
    report["candidate_total"] = len(candidates)
    (local_root / "seeding_report.json").write_text(json.dumps(dict(report), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(dict(report))


if __name__ == "__main__":
    main()
