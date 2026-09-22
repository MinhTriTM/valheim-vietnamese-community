"""Gộp JSON website đã có trên máy thành JSONL cục bộ, không xuất bản."""
import hashlib
import json
from collections import Counter
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    website = root / "valheimcheats.com"
    if not website.is_dir():
        raise SystemExit("Không thấy bản chụp valheimcheats.com cục bộ")
    output = root / "local" / "site_entities.jsonl"
    report = Counter()
    errors = []
    with output.open("w", encoding="utf-8") as stream:
        for path in sorted(website.rglob("*.json")):
            if path.is_symlink():
                continue
            raw = path.read_bytes()
            relative = path.relative_to(website).as_posix()
            try:
                payload = json.loads(raw.decode("utf-8-sig"))
            except (UnicodeError, json.JSONDecodeError) as exc:
                errors.append({"path": relative, "error": str(exc)})
                continue
            category = "/".join(path.relative_to(website).parts[:-1])
            row = {"path": relative, "category": category, "sha256": hashlib.sha256(raw).hexdigest(), "payload": payload}
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
            report[category] += 1
    summary = {"json_files_parsed": sum(report.values()), "categories": dict(report.most_common()), "errors": errors, "publish": False}
    (root / "local" / "site_entities_report.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{summary['json_files_parsed']} JSON hợp lệ, {len(errors)} lỗi; đầu ra chỉ trong local/")


if __name__ == "__main__":
    main()
