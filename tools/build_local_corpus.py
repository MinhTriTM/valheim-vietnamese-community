"""Lập chỉ mục tìm kiếm offline cho mọi nguồn cục bộ; DB không được commit."""
import hashlib
import html.parser
import json
import os
import sqlite3
from pathlib import Path

TEXT_SUFFIXES = {".html", ".htm", ".json", ".csv", ".md", ".txt", ".yaml", ".yml", ".xml", ".cs", ".py", ".js", ".ts"}


class VisibleText(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hidden = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "svg"}:
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag in {"script", "style", "svg"} and self.hidden:
            self.hidden -= 1

    def handle_data(self, data):
        if not self.hidden and data.strip():
            self.parts.append(data.strip())


def searchable_text(path, raw):
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return None
    decoded = raw.decode("utf-8-sig", errors="replace")
    if path.suffix.lower() in {".html", ".htm"}:
        parser = VisibleText()
        parser.feed(decoded)
        return " ".join(parser.parts)
    return decoded


def main():
    root = Path(__file__).resolve().parents[1]
    entries = json.loads((root / "sources" / "local_sources.json").read_text(encoding="utf-8"))["sources"]
    output = root / "local" / "corpus.sqlite3"
    temporary = root / "local" / "corpus.sqlite3.tmp"
    if temporary.exists():
        temporary.unlink()
    db = sqlite3.connect(temporary)
    db.execute("CREATE TABLE files (id INTEGER PRIMARY KEY, source TEXT, path TEXT UNIQUE, bytes INTEGER, sha256 TEXT, text TEXT)")
    db.execute("CREATE VIRTUAL TABLE search USING fts5(path, text, content='files', content_rowid='id')")
    count = searchable = 0
    for entry in entries:
        if entry["path"] == "local":
            continue
        base = root / entry["path"]
        paths = base.rglob("*") if base.is_dir() else [base]
        for path in paths:
            if not path.is_file() or path.is_symlink():
                continue
            raw = path.read_bytes()
            content = searchable_text(path, raw)
            relative = path.relative_to(root).as_posix()
            cursor = db.execute("INSERT INTO files (source,path,bytes,sha256,text) VALUES (?,?,?,?,?)", (entry["path"], relative, len(raw), hashlib.sha256(raw).hexdigest(), content))
            if content:
                db.execute("INSERT INTO search (rowid,path,text) VALUES (?,?,?)", (cursor.lastrowid, relative, content))
                searchable += 1
            count += 1
    db.commit()
    db.close()
    os.replace(temporary, output)
    print(f"Đã lập chỉ mục {count} file; {searchable} file tìm kiếm được: {output}")


if __name__ == "__main__":
    main()
