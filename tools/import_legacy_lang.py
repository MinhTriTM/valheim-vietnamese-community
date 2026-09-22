"""Nhập .lang hoặc bảng |key|value| cũ vào quarantine cục bộ."""
import argparse
import json
from collections import Counter
from pathlib import Path


def parse_line(line, style):
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return None
    if style == "lang":
        if "=" not in stripped:
            return None
        key, value = stripped.split("=", 1)
    else:
        if not stripped.startswith("|") or not stripped.endswith("|"):
            return None
        fields = stripped[1:-1].split("|", 1)
        if len(fields) != 2:
            return None
        key, value = fields
    key, value = key.strip(), value.strip()
    return (key, value) if key and key != "File_Name" and value else None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--style", choices=("lang", "pipe"), required=True)
    parser.add_argument("--namespace", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    output = args.output.resolve()
    if (root / "local").resolve() not in output.parents:
        raise ValueError("Đầu ra phải nằm trong local/")
    seen = set()
    rows = []
    stats = Counter()
    for number, line in enumerate(args.input.read_text(encoding="utf-8-sig", errors="replace").splitlines(), 1):
        parsed = parse_line(line, args.style)
        if not parsed:
            stats["skipped"] += 1
            continue
        key, value = parsed
        if key in seen:
            stats["duplicate_key"] += 1
            continue
        seen.add(key)
        rows.append({"namespace": args.namespace, "key": key, "vi": value, "status": "quarantine", "origin": str(args.input), "line": number, "source_sha256": None, "technical_signature": None})
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    print(f"{len(rows)} key quarantine, {dict(stats)}: {output}")


if __name__ == "__main__":
    main()
