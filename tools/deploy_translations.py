"""Công cụ triển khai (deploy) bản dịch tiếng Việt hoàn chỉnh cho Valheim và các Mod.
Hỗ trợ đồng bộ trực tiếp vào các thư mục game trên máy:
- Valheim
- Valheim_Mod
- Valheim_vi_mod
- Valheim - Copy
- Valheim_vi
"""
import argparse
import json
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"
DATA_MODS = DATA_DIR / "mods"
LOCAL_DIR = REPO_ROOT / "local"

TARGET_DIRS_DEFAULT = [
    Path(r"E:\SteamLibrary\steamapps\common\Valheim"),
    Path(r"E:\SteamLibrary\steamapps\common\Valheim_Mod"),
    Path(r"E:\SteamLibrary\steamapps\common\Valheim_vi_mod"),
    Path(r"E:\SteamLibrary\steamapps\common\Valheim - Copy"),
    Path(r"E:\SteamLibrary\steamapps\common\Valheim_vi")
]

def load_all_game_translations():
    """Hợp nhất các ứng viên dịch game từ data/valheim và local."""
    trans = {}
    for p in (DATA_DIR / "valheim").glob("*.jsonl"):
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip():
                row = json.loads(line)
                if row.get("vi"):
                    trans[row["key"]] = row["vi"]
    return trans

def deploy(target_root: Path):
    if not target_root.exists():
        print(f"[SKIP] Thu muc khong ton tai: {target_root}")
        return
    print(f"\n==========================================")
    print(f"TRIEN KHAI BAN DICH VAO: {target_root.name}")
    print(f"==========================================")

    bepinex = target_root / "BepInEx"
    plugins = bepinex / "plugins"
    plugins.mkdir(parents=True, exist_ok=True)

    # 1. Triển khai bản dịch Game
    game_trans = load_all_game_translations()
    valheim_vi_dir = plugins / "Translations" / "Vietnamese"
    valheim_vi_dir.mkdir(parents=True, exist_ok=True)
    all_trans_file = valheim_vi_dir / "all_translations.json"
    
    # Neu da co ban cu, cap nhat them
    existing = {}
    if all_trans_file.exists():
        try: existing = json.loads(all_trans_file.read_text(encoding="utf-8-sig"))
        except: pass
    existing.update(game_trans)
    all_trans_file.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[GAME] Da cap nhat {len(existing)} chuoi tieng Viet vao {all_trans_file.relative_to(target_root)}")

    # 2. Triển khai bản dịch từng Mod
    mod_copies = [
        # EpicLoot
        ("EpicLoot", [
            ("epicloot_vi.json", "localizations/Vietnamese.json"),
            ("epicloot_vi.json", "Vietnamese.json"),
        ]),
        # PlanBuild
        ("PlanBuild", [
            ("planbuild_vi.json", "PlanBuild/Translations/Vietnamese/PlanBuild.vietnamese.json"),
            ("planbuild_vi.json", "Translations/Vietnamese/PlanBuild.vietnamese.json"),
        ]),
        # QuickStackStore
        ("QuickStackStore", [
            ("quickstackstore_vi.json", "Translations/QuickStackStore.Vietnamese.json"),
        ]),
        # BetterArchery
        ("BetterArchery", [
            ("betterarchery_vi.json", "plugins/betterarchery_translations.json"),
        ]),
        # CoreWoodExtras
        ("CoreWoodExtras", [
            ("corewoodextras_vi.json", "Translations/Vietnamese/CoreWoodExtras.json"),
            ("corewoodextras_vi.json", "config/CoreWoodExtras/Translations/Vietnamese/CoreWoodExtras.json"),
        ]),
        # Innangard
        ("Innangard", [
            ("innangard_vi.json", "lang/Vietnamese.json"),
        ]),
        # SeneaL-UI
        ("SeneaL-UI", [
            ("senealui_vi.json", "Languages/vi.txt"),
        ]),
        # Skyheim
        ("Skyheim", [
            ("skyheim_vi.json", "skyheim.json"),
        ]),
    ]

    installed_count = 0
    for mod_name, mappings in mod_copies:
        for json_name, rel_path in mappings:
            src_data_file = DATA_MODS / json_name
            if not src_data_file.exists():
                continue
            # Tìm xem mod này có được cài trong target_root không
            possible_destinations = list(plugins.rglob(f"*{mod_name}*"))
            for dest_folder in possible_destinations:
                if dest_folder.is_dir():
                    dest_file = dest_folder / rel_path
                    dest_file.parent.mkdir(parents=True, exist_ok=True)
                    if dest_file.suffix == ".txt":
                        # Chuyen json sang txt dang key = val
                        data = json.loads(src_data_file.read_text(encoding="utf-8"))
                        txt_content = "\n".join([f"{k} = {v}" for k, v in data.items()])
                        dest_file.write_text(txt_content, encoding="utf-8")
                    else:
                        shutil.copyfile(src_data_file, dest_file)
                    print(f"  [MOD] Da cai dat ban dich {mod_name} -> {dest_file.relative_to(target_root)}")
                    installed_count += 1

    print(f"Hoan tat trien khai vao {target_root.name} ({installed_count} muc mod duoc cap nhat).")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=Path, help="Duong dan den thu muc game cu the")
    parser.add_argument("--all", action="store_true", help="Trien khai vao tat ca cac thu muc game tren may")
    args = parser.parse_args()

    targets = [args.target] if args.target else TARGET_DIRS_DEFAULT
    for t in targets:
        deploy(t)

if __name__ == "__main__":
    main()
