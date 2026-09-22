"""Script bổ sung các mod tuyển chọn (nhiều đồ chơi, đồ họa đẹp, QoL) từ kho mods/ vào Valheim_Mod.
Kèm đồng bộ toàn bộ file dịch tiếng Việt.
"""
import json
import os
import shutil
from pathlib import Path

REPO_ROOT = Path(r"E:\SteamLibrary\steamapps\common\valheim-vietnamese-community")
MODS_SOURCE = REPO_ROOT / "mods"
DATA_MODS = REPO_ROOT / "data" / "mods"

VALHEIM_MOD_ROOT = Path(r"E:\SteamLibrary\steamapps\common\Valheim_Mod")
VALHEIM_MOD_PLUGINS = VALHEIM_MOD_ROOT / "BepInEx" / "plugins"

# Danh sách các mod tuyển chọn cần bổ sung vào Valheim_Mod
SELECTED_MODS = [
    # 1. Vũ khí & Đồ chơi mới (Weapons & Content)
    {
        "folder_pattern": "ValheimArmory*",
        "dest_name": "ValheimArmory",
        "copy_subpath": "plugins", # neu co subpath
        "vi_file": "valheimarmory_vi.json",
        "vi_dest": "localizations/Vietnamese.json"
    },
    {
        "folder_pattern": "WeaponAdditions*",
        "dest_name": "WeaponAdditions",
        "copy_subpath": "",
        "vi_file": "weaponadditions_vi.json",
        "vi_dest": "translations.Vietnamese.yml"
    },
    {
        "folder_pattern": "Digitalroot.ArrowsJvL*",
        "dest_name": "Digitalroot.ArrowsJvL",
        "copy_subpath": "Digitalroot.ArrowsJvL",
        "vi_file": "digitalroot_arrows_vi.json",
        "vi_dest": "Assets/Translations/Vietnamese/translations.json"
    },
    {
        "folder_pattern": "Valheim Legends*",
        "dest_name": "ValheimLegends",
        "copy_subpath": "",
        "vi_file": None,
        "vi_dest": None
    },
    # 2. Phép thuật & Ma pháp (Magic & Spells)
    {
        "folder_pattern": "SkyheimFix*",
        "dest_name": "Skyheim",
        "copy_subpath": "",
        "vi_file": "skyheim_vi.json",
        "vi_dest": "skyheim.json"
    },
    {
        "folder_pattern": "MagicRevamp*",
        "dest_name": "MagicRevamp",
        "copy_subpath": "",
        "vi_file": "magicrevamp_vi.json",
        "vi_dest": "translations.Vietnamese.yml"
    },
    {
        "folder_pattern": "MagicBows*",
        "dest_name": "MagicBows",
        "copy_subpath": "",
        "vi_file": "magicbows_vi.json",
        "vi_dest": "translations.Vietnamese.yml"
    },
    {
        "folder_pattern": "DvergerStaves*",
        "dest_name": "DvergerStaves",
        "copy_subpath": "",
        "vi_file": "dvergerstaves_vi.json",
        "vi_dest": "translations.Vietnamese.yml"
    },
    # 3. Kiến trúc & Dân làng (Building & Colonization)
    {
        "folder_pattern": "CoreWoodExtras*",
        "dest_name": "CoreWoodExtras",
        "copy_subpath": "",
        "vi_file": "corewoodextras_vi.json",
        "vi_dest": "config/CoreWoodExtras/Translations/Vietnamese/CoreWoodExtras.json"
    },
    {
        "folder_pattern": "Innangard*",
        "dest_name": "Innangard",
        "copy_subpath": "BepInEx/plugins/Innangard",
        "vi_file": "innangard_vi.json",
        "vi_dest": "lang/Vietnamese.json"
    },
    # 4. Giao diện & Đồ họa (UI & Visuals)
    {
        "folder_pattern": "SeneaL UI*",
        "dest_name": "SeneaL-UI",
        "copy_subpath": "BepInEx/plugins/SeneaL-UI",
        "vi_file": "senealui_vi.json",
        "vi_dest": "Languages/vi.txt"
    },
    {
        "folder_pattern": "BadgersSkiesFix*",
        "dest_name": "BadgersSkiesFix",
        "copy_subpath": "",
        "vi_file": None,
        "vi_dest": None
    },
    # 5. Tiện ích cuộc sống (Quality of Life)
    {
        "folder_pattern": "Better Archery*",
        "dest_name": "BetterArchery",
        "copy_subpath": "BetterArchery/plugins",
        "vi_file": "betterarchery_vi.json",
        "vi_dest": "betterarchery_translations.json"
    },
    {
        "folder_pattern": "Quick Stack - Store - Sort - Trash*",
        "dest_name": "QuickStackStore",
        "copy_subpath": "",
        "vi_file": "quickstackstore_vi.json",
        "vi_dest": "Translations/QuickStackStore.Vietnamese.json"
    },
    {
        "folder_pattern": "CraftFromChestsPlus*",
        "dest_name": "CraftFromChestsPlus",
        "copy_subpath": "plugins",
        "vi_file": "craftfromchestsplus_vi.json",
        "vi_dest": "CraftFromChestsPlus.Languages.vi.json"
    },
    {
        "folder_pattern": "TeleportEverything*",
        "dest_name": "TeleportEverything",
        "copy_subpath": "",
        "vi_file": "teleporteverything_vi.json",
        "vi_dest": "translations.Vietnamese.yml"
    },
    {
        "folder_pattern": "VeinMining*",
        "dest_name": "VeinMining",
        "copy_subpath": "",
        "vi_file": None,
        "vi_dest": None
    },
    {
        "folder_pattern": "Tools in Water*",
        "dest_name": "ToolsInWater",
        "copy_subpath": "",
        "vi_file": None,
        "vi_dest": None
    },
    {
        "folder_pattern": "Fast Repair Button*",
        "dest_name": "FastRepairButton",
        "copy_subpath": "",
        "vi_file": None,
        "vi_dest": None
    },
    {
        "folder_pattern": "HoldAttack*",
        "dest_name": "HoldAttack",
        "copy_subpath": "",
        "vi_file": None,
        "vi_dest": None
    },
    {
        "folder_pattern": "Instant Monster Drop*",
        "dest_name": "InstantMonsterDrop",
        "copy_subpath": "",
        "vi_file": None,
        "vi_dest": None
    },
    {
        "folder_pattern": "AutoMapPins*",
        "dest_name": "AutoMapPins",
        "copy_subpath": "",
        "vi_file": None,
        "vi_dest": None
    },
    {
        "folder_pattern": "Cartur's Map Pins*",
        "dest_name": "CarturMapPins",
        "copy_subpath": "",
        "vi_file": None,
        "vi_dest": None
    },
    {
        "folder_pattern": "BeastMaster*",
        "dest_name": "BeastMaster",
        "copy_subpath": "",
        "vi_file": None,
        "vi_dest": None
    }
]

def main():
    VALHEIM_MOD_PLUGINS.mkdir(parents=True, exist_ok=True)
    installed_count = 0

    print("==================================================")
    print("BẮT ĐẦU BỔ SUNG MOD TUYỂN CHỌN VÀO Valheim_Mod")
    print("==================================================")

    for item in SELECTED_MODS:
        pattern = item["folder_pattern"]
        matched_folders = list(MODS_SOURCE.glob(pattern))
        if not matched_folders:
            print(f"[KHONG TIM THAY] Khong tim thay mod voi mau: {pattern}")
            continue
        
        src_folder = matched_folders[0]
        if not src_folder.is_dir():
            # Tim thu muc giai nen tuong ung
            dirs = [d for d in matched_folders if d.is_dir()]
            if dirs: src_folder = dirs[0]
            else: continue

        subpath = item["copy_subpath"]
        copy_from = src_folder / subpath if subpath else src_folder
        dest_dir = VALHEIM_MOD_PLUGINS / item["dest_name"]
        dest_dir.mkdir(parents=True, exist_ok=True)

        # Sao chep cac file dll, asset, json, config
        for root, dirs, files in os.walk(copy_from):
            rel_root = Path(root).relative_to(copy_from)
            target_sub = dest_dir / rel_root
            target_sub.mkdir(parents=True, exist_ok=True)
            for f in files:
                # Bo qua zip, icon to
                if f.endswith(".zip") or f.endswith(".rar"): continue
                s_file = Path(root) / f
                d_file = target_sub / f
                shutil.copy2(s_file, d_file)

        # Cai dat file tieng Viet neu co
        vi_file = item["vi_file"]
        vi_dest = item["vi_dest"]
        if vi_file and vi_dest:
            src_vi = DATA_MODS / vi_file
            if src_vi.exists():
                dest_vi = dest_dir / vi_dest
                dest_vi.parent.mkdir(parents=True, exist_ok=True)
                if dest_vi.suffix == ".txt":
                    # Chuyen dict sang dang key = val
                    data = json.loads(src_vi.read_text(encoding="utf-8"))
                    dest_vi.write_text("\n".join([f"{k} = {v}" for k, v in data.items()]), encoding="utf-8")
                else:
                    shutil.copy2(src_vi, dest_vi)

        print(f"  [DA BO SUNG] {item['dest_name']} (Tu: {src_folder.name})")
        installed_count += 1

    # Đồng thời cập nhật bộ dịch game cho Valheim_Mod
    print("\n--- Đồng bộ toàn bộ bản dịch Tiếng Việt game (all_translations.json) ---")
    valheim_vi_dest = VALHEIM_MOD_PLUGINS / "Translations" / "Vietnamese"
    valheim_vi_dest.mkdir(parents=True, exist_ok=True)
    
    # Lấy all_translations.json từ Valheim gốc
    master_trans_p = Path(r"E:\SteamLibrary\steamapps\common\Valheim\BepInEx\plugins\Translations\Vietnamese\all_translations.json")
    if master_trans_p.exists():
        shutil.copy2(master_trans_p, valheim_vi_dest / "all_translations.json")
        print(f"  -> Đã đồng bộ {master_trans_p.stat().st_size} bytes bản dịch game vào Valheim_Mod")

    # Đảm bảo có ValheimVietnamese.dll loader trong Valheim_Mod
    loader_dll = Path(r"E:\SteamLibrary\steamapps\common\Valheim\BepInEx\plugins\ValheimVietnamese.dll")
    if loader_dll.exists():
        shutil.copy2(loader_dll, VALHEIM_MOD_PLUGINS / "ValheimVietnamese.dll")
        print("  -> Đã bổ sung ValheimVietnamese.dll loader vào Valheim_Mod")

    print(f"\n==================================================")
    print(f"HOÀN TẤT: Đã bổ sung thành công {installed_count} mod tuyển chọn vào Valheim_Mod!")
    print("==================================================")

if __name__ == "__main__":
    main()
