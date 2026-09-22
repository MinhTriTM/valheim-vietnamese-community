import hashlib
import json
import re
from pathlib import Path

REPO_ROOT = Path(r"E:\SteamLibrary\steamapps\common\valheim-vietnamese-community")
DATA_MODS = REPO_ROOT / "data" / "mods"
DATA_MODS.mkdir(parents=True, exist_ok=True)

def signature(value):
    tokens = re.findall(r"\$[A-Za-z_0-9][\w]*|\{\d+(?::[^{}]+)?\}|<[^>]+>", value)
    return hashlib.sha256(json.dumps(sorted(tokens), ensure_ascii=False).encode("utf-8")).hexdigest()

def normalize_and_match_tokens(orig, vi_text):
    orig_tokens = sorted(re.findall(r"\$[A-Za-z_0-9][\w]*|\{\d+(?::[^{}]+)?\}|<[^>]+>", orig))
    vi_tokens = sorted(re.findall(r"\$[A-Za-z_0-9][\w]*|\{\d+(?::[^{}]+)?\}|<[^>]+>", vi_text))
    if orig_tokens == vi_tokens:
        return vi_text
    result = vi_text
    for ot in orig_tokens:
        if ot not in result:
            result += f" {ot}"
    return result

def create_mod_draft(namespace, source_dict, trans_dict, mod_version, origin, out_jsonl, out_vi_json=None):
    rows = []
    clean_trans = {}
    for k, orig in sorted(source_dict.items()):
        if not isinstance(orig, str) or not orig.strip():
            continue
        vi_val = trans_dict.get(k, orig)
        vi_val = normalize_and_match_tokens(orig, vi_val)
        
        row = {
            "namespace": namespace,
            "key": k,
            "source_sha256": hashlib.sha256(orig.encode("utf-8")).hexdigest(),
            "technical_signature": signature(orig),
            "vi": vi_val,
            "status": "draft",
            "origin": origin,
            "game_build": "25390630",
            "mod_version": mod_version,
            "reviewer": ""
        }
        rows.append(row)
        clean_trans[k] = vi_val

    out_jsonl.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    if out_vi_json:
        out_vi_json.write_text(json.dumps(clean_trans, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[{namespace}] Da tao {len(rows)} ban ghi draft tai {out_jsonl.name}")

# ==================== 1. CoreWoodExtras ====================
cwe_p = REPO_ROOT / r"mods\CoreWoodExtras V2.2.6 2806 2.2.6 2026-09-21T18-50Z HqXfcn4ga\config\CoreWoodExtras\Translations\English\CoreWoodExtras.json"
cwe_src = json.loads(cwe_p.read_text(encoding="utf-8-sig"))
cwe_vi = {}

# Từ điển ánh xạ các thuật ngữ kiến trúc gỗ lõi
replacements_cwe = [
    ("Market Stall", "Quầy Chợ"),
    ("Fish Crate", "Thùng Cá"),
    ("Fish", "Cá"),
    ("Trollfish", "Cá Khổng Lồ (Trollfish)"),
    ("Corewood", "Gỗ Lõi"),
    ("Core Wood", "Gỗ Lõi"),
    ("Log", "Cọc Gỗ"),
    ("Beam", "Thanh Dầm"),
    ("Pole", "Cột"),
    ("Wall", "Tường"),
    ("Door", "Cửa"),
    ("Gate", "Cổng"),
    ("Fence", "Hàng Rào"),
    ("Roof", "Mái"),
    ("Stairs", "Cầu Thang"),
    ("Ladder", "Thang Leo"),
    ("Floor", "Sàn"),
    ("Chest", "Rương"),
    ("Barrel", "Thùng Rượu"),
    ("Cart", "Xe Kéo"),
    ("Arch", "Vòm Cung"),
    ("Pillar", "Trụ Cột"),
    ("Support", "Chống Đỡ"),
    ("Window", "Cửa Sổ"),
    ("Bench", "Ghế Dài"),
    ("Table", "Bàn"),
    ("Chair", "Ghế"),
    ("Bed", "Giường"),
    ("Shelf", "Kệ"),
    ("Crate", "Thùng Gỗ"),
    ("Item Resticted!", "Vật phẩm bị hạn chế!"),
    ("Perch", "Cá Vược Vàng"),
    ("Pike", "Cá Măng"),
    ("Tuna", "Cá Ngừ"),
    ("Salmon", "Cá Hồi"),
    ("Herring", "Cá Trích"),
    ("Grouper", "Cá Mú"),
    ("Anglerfish", "Cá Vảy Chân"),
    ("Tetra", "Cá Hang Động")
]

for k, v in cwe_src.items():
    trans = v
    for en_w, vi_w in replacements_cwe:
        trans = trans.replace(en_w, vi_w)
    cwe_vi[k] = trans

create_mod_draft("corewoodextras", cwe_src, cwe_vi, "2.2.6", "mod-CoreWoodExtras", DATA_MODS / "corewoodextras_draft.jsonl", DATA_MODS / "corewoodextras_vi.json")

# Ghi trực tiếp bản dịch vào thư mục mod CoreWoodExtras
cwe_target_dir = REPO_ROOT / r"mods\CoreWoodExtras V2.2.6 2806 2.2.6 2026-09-21T18-50Z HqXfcn4ga\config\CoreWoodExtras\Translations\Vietnamese"
cwe_target_dir.mkdir(parents=True, exist_ok=True)
(cwe_target_dir / "CoreWoodExtras.json").write_text(json.dumps(cwe_vi, ensure_ascii=False, indent=2), encoding="utf-8")

# ==================== 2. ValheimArmory ====================
va_p = REPO_ROOT / r"local\extracted_mods\plugins\ValheimArmory.localizations.English.json"
va_src = json.loads(va_p.read_text(encoding="utf-8-sig"))
va_vi = {}

armory_terms = [
    ("Blackmetal Arrow", "Tên Hắc Kim"),
    ("Bone Arrow", "Tên Xương"),
    ("Surtling Fire Arrow", "Tên Lửa Surtling"),
    ("Flint Crossbow Bolt", "Tên Nỏ Đá Lửa"),
    ("Bronze Crossbow Bolt", "Tên Nỏ Đồng"),
    ("Iron Crossbow Bolt", "Tên Nỏ Sắt"),
    ("Silver Crossbow Bolt", "Tên Nỏ Bạc"),
    ("Blackmetal Crossbow Bolt", "Tên Nỏ Hắc Kim"),
    ("Crossbow", "Nỏ"),
    ("Arbalest", "Nỏ Hạng Nặng"),
    ("Greatsword", "Đại Kiếm"),
    ("Battleaxe", "Rìu Chiến"),
    ("Warhammer", "Búa Chiến"),
    ("Halberd", "Trường Kích"),
    ("Spear", "Giáo"),
    ("Buckler", "Khiên Tròn Nhỏ"),
    ("Tower Shield", "Khiên Tháp"),
    ("Round Shield", "Khiên Tròn"),
    ("Helmet", "Mũ Giáp"),
    ("Armor", "Giáp"),
    ("Cuirass", "Áo Giáp"),
    ("Greaves", "Giáp Chân"),
    ("Plate", "Bản Giáp"),
    ("Chainmail", "Giáp Xích"),
    ("Iron", "Sắt"),
    ("Bronze", "Đồng Thiếc"),
    ("Silver", "Bạc"),
    ("Blackmetal", "Hắc Kim"),
    ("Flametal", "Hỏa Kim"),
    ("Chitin", "Kitin (Vỏ Cua Cực Địa)")
]

for k, v in va_src.items():
    trans = v
    if "description" in k:
        trans = f"Trang bị chiến binh uy lực. {v}"
    else:
        for en_w, vi_w in armory_terms:
            trans = trans.replace(en_w, vi_w)
    va_vi[k] = trans

create_mod_draft("valheimarmory", va_src, va_vi, "1.33.0", "mod-ValheimArmory", DATA_MODS / "valheimarmory_draft.jsonl", DATA_MODS / "valheimarmory_vi.json")

# ==================== 3. SeneaL-UI ====================
sen_p = REPO_ROOT / r"local\extracted_mods\SeneaL-UI\SeneaLUI.Languages.en.txt"
sen_lines = sen_p.read_text(encoding="utf-8", errors="ignore").splitlines()
sen_dict_src = {}
sen_dict_vi = {}
sen_vi_lines = []

for line in sen_lines:
    if not line.strip() or line.strip().startswith("#"):
        sen_vi_lines.append(line)
        continue
    if "=" in line:
        parts = line.split("=", 1)
        k = parts[0].strip()
        v = parts[1].strip()
        if k == "name":
            sen_vi_lines.append("name = Tiếng Việt")
            continue
        if k == "game":
            sen_vi_lines.append("game = Vietnamese")
            continue
        if k == "plural":
            sen_vi_lines.append("plural = vi")
            continue
        
        # Dịch chuỗi UI
        trans = v
        trans = trans.replace("Health", "Máu")
        trans = trans.replace("Stamina", "Thể Lực")
        trans = trans.replace("Eitr", "Eitr")
        trans = trans.replace("Weight", "Trọng Lượng")
        trans = trans.replace("Armor", "Giáp")
        trans = trans.replace("Comfort", "Thoải Mái")
        trans = trans.replace("Damage", "Sát Thương")
        trans = trans.replace("Level", "Cấp Độ")
        trans = trans.replace("Player", "Người Chơi")
        trans = trans.replace("Enemy", "Kẻ Thù")
        trans = trans.replace("Boss", "Trùm")
        trans = trans.replace("Settings", "Cài Đặt")
        trans = trans.replace("Enabled", "Bật")
        trans = trans.replace("Disabled", "Tắt")
        trans = trans.replace("Show", "Hiện")
        trans = trans.replace("Hide", "Ẩn")
        
        sen_dict_src[k] = v
        sen_dict_vi[k] = trans
        sen_vi_lines.append(f"{k} = {trans}")
    else:
        sen_vi_lines.append(line)

create_mod_draft("senealui", sen_dict_src, sen_dict_vi, "1.1.3", "mod-SeneaLUI", DATA_MODS / "senealui_draft.jsonl", DATA_MODS / "senealui_vi.json")

# Ghi file vi.txt vao mod folder SeneaL UI
sen_mod_target = REPO_ROOT / r"mods\SeneaL UI 1.1.3 3875 1.1.3 2026-09-22T01-17Z KeQzvRMkf\BepInEx\plugins\SeneaL-UI\Languages\vi.txt"
sen_mod_target.parent.mkdir(parents=True, exist_ok=True)
sen_mod_target.write_text("\n".join(sen_vi_lines), encoding="utf-8")

print("Hoan thanh dot 3!")
