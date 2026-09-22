"""Trích English localization của Valheim đang cài vào local/ để đối chiếu."""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path

from import_local import signature


def file_hash(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_assets(path):
    import UnityPy

    assets = []
    for obj in UnityPy.load(str(path)).objects:
        if obj.type.name != "TextAsset":
            continue
        data = obj.read()
        name = getattr(data, "m_Name", "")
        if not name.lower().startswith("localization"):
            continue
        script = data.m_Script
        content = script.decode("utf-8-sig") if isinstance(script, bytes) else script
        assets.append((name, content))
    if not any(name == "localization" for name, _ in assets):
        raise ValueError("Không tìm thấy TextAsset localization gốc")
    return assets


def extract_rows(assets):
    keys = {}
    total = 0
    languages = set()
    for asset_name, content in assets:
        rows = csv.reader(io.StringIO(content))
        header = next(rows, [])
        if "English" not in header:
            raise ValueError(f"{asset_name} không có cột English")
        languages.update(header[1:])
        index = header.index("English")
        for row in rows:
            if not row or not row[0] or row[0].startswith("//"):
                continue
            key = row[0]
            original = row[index] if index < len(row) else ""
            texts = {lang: row[column] for column, lang in enumerate(header[1:], start=1) if lang and column < len(row) and row[column]}
            keys.setdefault(key, []).append({"asset": asset_name, "source": original, "texts": texts})
            total += 1
    return keys, total, languages


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--resources", type=Path, required=True)
    parser.add_argument("--build", required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    output = root / "local"
    output.mkdir(exist_ok=True)
    assets = read_assets(args.resources)
    keys, occurrences, languages = extract_rows(assets)
    conflicts = 0
    with (output / "game_sources.jsonl").open("w", encoding="utf-8") as stream, (output / "game_languages.jsonl").open("w", encoding="utf-8") as language_stream:
        for key, variants in sorted(keys.items()):
            preferred = next((item for item in reversed(variants) if item["asset"] != "localization"), variants[-1])
            conflict = len({item["source"] for item in variants if item["source"]}) > 1
            conflicts += conflict
            original = preferred["source"]
            row = {"key": key, "source": original, "source_sha256": hashlib.sha256(original.encode("utf-8")).hexdigest(), "technical_signature": signature(original), "asset": preferred["asset"], "conflict": conflict, "occurrences": [{"asset": item["asset"], "source": item["source"]} for item in variants]}
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
            language_stream.write(json.dumps({"key": key, "asset": preferred["asset"], "texts": preferred["texts"]}, ensure_ascii=False) + "\n")
    report = {"game_build": args.build, "resources_sha256": file_hash(args.resources), "resources_size": args.resources.stat().st_size, "assets": [name for name, _ in assets], "languages": sorted(languages), "row_occurrences": occurrences, "unique_keys": len(keys), "source_conflicts": conflicts}
    (output / "game_manifest.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(keys)} key, {occurrences} lượt xuất hiện, {conflicts} key xung đột; chỉ lưu trong local/")


if __name__ == "__main__":
    main()
