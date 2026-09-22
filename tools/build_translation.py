"""Xuất JSON key/value cho runtime; mặc định chỉ lấy bản reviewed còn khớp nguồn."""
import argparse
import hashlib
import json
import os
from collections import Counter
from pathlib import Path

from import_local import signature


def source_map(args):
    if args.source_catalog:
        return {row["key"]: row for row in (json.loads(line) for line in args.source_catalog.read_text(encoding="utf-8").splitlines())}
    data = json.loads(args.source_json.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("Source JSON phải là object")
    return {key: {"source": value, "source_sha256": hashlib.sha256(value.encode("utf-8")).hexdigest(), "technical_signature": signature(value), "conflict": False} for key, value in data.items()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--namespace", required=True)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--source-catalog", type=Path)
    source.add_argument("--source-json", type=Path)
    parser.add_argument("--preview", action="store_true", help="Cho phép draft, chỉ để QA cục bộ")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    current = source_map(args)
    selected = {}
    report = Counter()
    for path in (root / "data").rglob("*.jsonl"):
        for line in path.read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            if row["namespace"] != args.namespace:
                continue
            report["records"] += 1
            source_row = current.get(row["key"])
            if not source_row or source_row["conflict"]:
                report["missing_or_conflicting_source"] += 1
                continue
            if row["source_sha256"] != source_row["source_sha256"] or row["technical_signature"] != source_row["technical_signature"]:
                report["stale_source"] += 1
                continue
            if signature(row["vi"]) != row["technical_signature"]:
                report["broken_tokens"] += 1
                continue
            if row["status"] != "reviewed" and not args.preview:
                report["unreviewed"] += 1
                continue
            if row["key"] in selected:
                raise ValueError(f"Key trùng: {row['key']}")
            selected[row["key"]] = row["vi"]
    if not selected:
        raise SystemExit(f"Không có bản dịch đủ điều kiện xuất: {dict(report)}")
    name = "".join(char if char.isalnum() or char in "-_" else "_" for char in args.namespace)
    output = root / "local" / "export" / f"{name}{'.preview' if args.preview else ''}.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(output.suffix + ".tmp")
    temporary.write_text(json.dumps(selected, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, output)
    report["exported"] = len(selected)
    print(f"{output}: {dict(report)}")


if __name__ == "__main__":
    main()
