"""Kiểm kê các bản chụp cục bộ; kết quả chỉ ghi trong local/."""
import json
from collections import Counter
from pathlib import Path


def inspect_item(root, entry):
    path = root / entry["path"]
    files = [item for item in path.rglob("*") if item.is_file() and not item.is_symlink()] if path.is_dir() else ([path] if path.is_file() else [])
    kinds = Counter(item.suffix.lower() or "[none]" for item in files)
    result = {
        "path": entry["path"], "role": entry["role"], "exists": path.exists(),
        "file_count": len(files), "bytes": sum(item.stat().st_size for item in files),
        "extensions": dict(kinds.most_common(12)),
    }
    if entry["role"] not in {"website_reference", "duplicate_website_reference", "website_archive", "private_translation_workspace"}:
        result["translation_candidates"] = sorted(str(item.relative_to(root)).replace("\\", "/") for item in files if item.suffix.lower() in {".json", ".csv", ".yaml", ".yml"} and any(part in str(item).lower() for part in ("localiz", "translation", "language")))[:100]
    return result


def main():
    root = Path(__file__).resolve().parents[1]
    catalog = json.loads((root / "sources" / "local_sources.json").read_text(encoding="utf-8"))
    report = {"schema_version": 1, "sources": [inspect_item(root, item) for item in catalog["sources"]]}
    large = root / "valheimcheats.com"
    small = root / "valheimcheats_clone"
    if large.is_dir() and small.is_dir():
        large_paths = {str(path.relative_to(large)).lower() for path in large.rglob("*") if path.is_file()}
        small_paths = {str(path.relative_to(small)).lower() for path in small.rglob("*") if path.is_file()}
        report["website_path_overlap"] = len(large_paths & small_paths)
        report["website_smaller_path_count"] = len(small_paths)
    output = root / "local" / "source_inventory.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Đã kiểm kê {len(report['sources'])} nguồn vào {output}")


if __name__ == "__main__":
    main()
