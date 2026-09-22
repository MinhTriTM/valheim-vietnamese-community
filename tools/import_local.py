"""Nhập nguồn và bản dịch cục bộ vào vùng Git bỏ qua để rà soát."""
import argparse
import hashlib
import json
import re
from pathlib import Path


def signature(value):
    tokens = re.findall(r"\$[A-Za-z_][\w]*|\{\d+(?::[^{}]+)?\}|<[^>]+>", value)
    return hashlib.sha256(json.dumps(sorted(tokens), ensure_ascii=False).encode("utf-8")).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--namespace", required=True)
    parser.add_argument("--build", required=True)
    args = parser.parse_args()
    source = json.loads(args.source.read_text(encoding="utf-8-sig"))
    target = json.loads(args.target.read_text(encoding="utf-8-sig"))
    if not isinstance(source, dict) or not isinstance(target, dict):
        raise ValueError("Nguồn và bản dịch phải là JSON object")
    output = Path(__file__).resolve().parents[1] / "local" / "imported.jsonl"
    output.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with output.open("w", encoding="utf-8") as stream:
        for key, original in source.items():
            if not isinstance(original, str) or not isinstance(key, str):
                continue
            translated = target.get(key, "")
            row = {
                "namespace": args.namespace, "key": key,
                "source_sha256": hashlib.sha256(original.encode("utf-8")).hexdigest(),
                "technical_signature": signature(original),
                "vi": translated if isinstance(translated, str) else "",
                "status": "quarantine", "origin": "local-install",
                "game_build": args.build, "mod_version": "", "reviewer": "",
            }
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
            count += 1
    print(f"Đã nhập {count} key vào {output}; toàn bộ ở trạng thái quarantine")


if __name__ == "__main__":
    main()

