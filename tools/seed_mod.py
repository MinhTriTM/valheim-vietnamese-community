"""Ghép bản dịch mod tự viết với key nguồn để tạo bản ghi draft."""
import argparse
import hashlib
import json
from pathlib import Path

from import_local import signature


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--translation", type=Path, required=True)
    parser.add_argument("--namespace", required=True)
    parser.add_argument("--origin", required=True)
    parser.add_argument("--game-build", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    output = args.output.resolve()
    if (root / "data").resolve() not in output.parents:
        raise ValueError("Đầu ra phải nằm trong data/")
    source = json.loads(args.source.read_text(encoding="utf-8-sig"))
    translated = json.loads(args.translation.read_text(encoding="utf-8-sig"))
    if not isinstance(source, dict) or not isinstance(translated, dict):
        raise ValueError("Đầu vào phải là JSON object")
    if source.keys() != translated.keys():
        raise ValueError(f"Key thiếu: {sorted(source.keys() - translated.keys())}; key thừa: {sorted(translated.keys() - source.keys())}")
    rows = []
    for key, original in sorted(source.items()):
        value = translated[key]
        if not isinstance(original, str) or not isinstance(value, str) or not value:
            raise ValueError(f"Giá trị không hợp lệ: {key}")
        if signature(original) != signature(value):
            raise ValueError(f"Token không khớp: {key}")
        rows.append({"namespace": args.namespace, "key": key, "source_sha256": hashlib.sha256(original.encode("utf-8")).hexdigest(), "technical_signature": signature(original), "vi": value, "status": "draft", "origin": args.origin, "game_build": args.game_build, "mod_version": "unknown", "reviewer": ""})
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    print(f"{len(rows)} bản ghi draft: {output}")


if __name__ == "__main__":
    main()
