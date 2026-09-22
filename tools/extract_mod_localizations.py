import io
import json
import os
import re
import sys
import zipfile
from pathlib import Path

# Thư mục gốc dự án
REPO_ROOT = Path(r"E:\SteamLibrary\steamapps\common\valheim-vietnamese-community")
MODS_DIR = REPO_ROOT / "mods"
OUTPUT_DIR = REPO_ROOT / "local" / "extracted_mods"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Khởi tạo danh sách trích xuất
extracted_summary = []

# 1. Trích xuất tài nguyên từ EpicLoot
epic_dll = MODS_DIR / "EpicLoot-0.14.11.zip 387 0.14.11 2026-09-21T18-53Z sVRYlHWAd" / "plugins" / "EpicLoot.dll"
if not epic_dll.exists():
    epic_dll = Path(r"E:\SteamLibrary\steamapps\common\Valheim_Mod\BepInEx\plugins\RandyKnapp-EpicLoot\EpicLoot.dll")

print(f"Reading EpicLoot: {epic_dll}")
# Trong C#, assembly có thể đọc Manifest Resources hoặc quét blob JSON
epic_bytes = epic_dll.read_bytes()
# Tìm chuỗi EpicLoot.localizations.English.json trong dll
# Thay vì phụ thuộc assembly load, ta có thể tìm JSON blob hoặc dùng pwsh script để export chính xác
print("EpicLoot size:", len(epic_bytes))
