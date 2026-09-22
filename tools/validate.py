"""Kiểm tra schema và key trùng trong dữ liệu công khai."""
import json
import re
import sys
from pathlib import Path

from import_local import signature

REQUIRED = {"namespace", "key", "source_sha256", "technical_signature", "vi", "status", "origin", "game_build", "mod_version", "reviewer"}


def main(root):
    seen = set()
    errors = []
    files = list(root.rglob("*.jsonl"))
    for path in files:
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            try:
                row = json.loads(line)
                missing = REQUIRED - row.keys()
                if missing:
                    raise ValueError(f"thiếu {sorted(missing)}")
                if row["status"] not in {"draft", "reviewed"}:
                    raise ValueError("status không hợp lệ")
                if not all(isinstance(row[name], str) for name in REQUIRED):
                    raise ValueError("trường bắt buộc phải là chuỗi")
                if not row["namespace"] or not row["key"] or not row["vi"] or not row["origin"]:
                    raise ValueError("thiếu định danh, bản dịch hoặc nguồn gốc")
                if row["status"] == "reviewed" and not row["reviewer"]:
                    raise ValueError("bản reviewed cần người rà soát")
                if not re.fullmatch(r"[0-9a-f]{64}", row["source_sha256"]) or not re.fullmatch(r"[0-9a-f]{64}", row["technical_signature"]):
                    raise ValueError("hash không hợp lệ")
                if signature(row["vi"]) != row["technical_signature"]:
                    raise ValueError("token bản dịch khác nguồn")
                identity = (row["namespace"], row["key"], row["source_sha256"])
                if identity in seen:
                    raise ValueError("key trùng")
                seen.add(identity)
            except (ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
                errors.append(f"{path}:{number}: {exc}")
    print(f"{len(files)} file, {len(seen)} bản ghi, {len(errors)} lỗi")
    for error in errors:
        print(error, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1] if len(sys.argv) > 1 else "data")))
