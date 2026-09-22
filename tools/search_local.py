"""Tìm file trong corpus.sqlite3 cục bộ theo từ khóa FTS5."""
import argparse
import sqlite3
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="Truy vấn FTS5, ví dụ: troll hoặc \"spawn ID\"")
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()
    database = Path(__file__).resolve().parents[1] / "local" / "corpus.sqlite3"
    if not database.is_file():
        raise SystemExit("Chưa có corpus; chạy python tools/build_local_corpus.py")
    with sqlite3.connect(database) as db:
        rows = db.execute("SELECT files.path, files.source FROM search JOIN files ON files.id=search.rowid WHERE search MATCH ? LIMIT ?", (args.query, max(1, min(args.limit, 100)))).fetchall()
    for path, source in rows:
        print(f"{source}\t{path}")
    print(f"{len(rows)} kết quả")


if __name__ == "__main__":
    main()
