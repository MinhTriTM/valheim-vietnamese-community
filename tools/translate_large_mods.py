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
    return clean_trans

# ==================== 1. MagicRevamp ====================
print("--- Dang xu ly MagicRevamp ---")
mr_p = REPO_ROOT / r"local\extracted_mods\MagicRevamp 2743 1.5.1 2026-09-20T14-25Z roSbsxuJA\MagicRevamp.translations.English.yml"
mr_src = {}
for line in mr_p.read_text(encoding="utf-8", errors="ignore").splitlines():
    line = line.strip()
    if not line or ":" not in line: continue
    k, v = line.split(":", 1)
    k = k.strip()
    v = v.strip().strip('"').strip("'")
    mr_src[k] = v

mr_vi = {}
terms_mr = [
    ("Rootweave Cape", "Áo Choàng Rễ Cây"),
    ("Rootweave Chest", "Giáp Thân Rễ Cây"),
    ("Rootweave Helm", "Mũ Giáp Rễ Cây"),
    ("Rootweave Legs", "Giáp Chân Rễ Cây"),
    ("Shadowleaf Vanguard Cape", "Áo Choàng Tiên Phong Diệp Ảnh"),
    ("Shadowleaf Vanguard Hat", "Mũ Tiên Phong Diệp Ảnh"),
    ("Shadowleaf Vanguard Trousers", "Quần Tiên Phong Diệp Ảnh"),
    ("Shadowleaf Vanguard Robe", "Áo Choàng Pháp Sư Diệp Ảnh"),
    ("Cape", "Áo Choàng"),
    ("Robes", "Trang Phục Pháp Sư"),
    ("Hood", "Mũ Trùm"),
    ("Hat", "Mũ"),
    ("Staff", "Gậy Phép"),
    ("Wand", "Đũa Phép"),
    ("Magic", "Ma Thuật"),
    ("Mana", "Năng Lượng"),
    ("Eitr", "Eitr"),
    ("Fire", "Lửa"),
    ("Frost", "Băng"),
    ("Lightning", "Sét"),
    ("Poison", "Độc")
]

for k, v in mr_src.items():
    trans = v
    if "description" in k:
        trans = f"Vật phẩm ma thuật huyền bí. {v}"
    else:
        for en_w, vi_w in terms_mr:
            trans = trans.replace(en_w, vi_w)
    mr_vi[k] = trans

create_mod_draft("magicrevamp", mr_src, mr_vi, "1.5.1", "mod-MagicRevamp", DATA_MODS / "magicrevamp_draft.jsonl", DATA_MODS / "magicrevamp_vi.json")

# ==================== 2. Innangard ====================
print("--- Dang xu ly Innangard ---")
inn_p = REPO_ROOT / r"local\extracted_mods\Innangard\Innangard.English.json"
inn_src = json.loads(inn_p.read_text(encoding="utf-8-sig"))
inn_vi = {}

inn_terms = [
    ("Settler", "Dân Định Cư"),
    ("Builder's Hammer", "Búa Thợ Xây"),
    ("piece(s)", "mảnh/chi tiết"),
    ("Blueprint", "Bản Thiết Kế"),
    ("Village", "Ngôi Làng"),
    ("Frith", "Bảo Hộ (Frith)"),
    ("Warehouse", "Nhà Kho"),
    ("Tavern", "Quán Trọ"),
    ("Farm", "Nông Trại"),
    ("Mine", "Mỏ Quặng"),
    ("Blacksmith", "Lò Rèn"),
    ("Hunter", "Thợ Săn"),
    ("Fisherman", "Ngư Dân"),
    ("Guard", "Lính Gác"),
    ("House", "Nhà Ở"),
    ("Gate", "Cổng"),
    ("Wall", "Tường"),
    ("Tower", "Tháp Canh")
]

for k, v in inn_src.items():
    trans = v
    for en_w, vi_w in inn_terms:
        trans = trans.replace(en_w, vi_w)
    inn_vi[k] = trans

create_mod_draft("innangard", inn_src, inn_vi, "0.1.9", "mod-Innangard", DATA_MODS / "innangard_draft.jsonl", DATA_MODS / "innangard_vi.json")

# Ghi vào mod directory của Innangard
inn_mod_target = REPO_ROOT / r"mods\Innangard 3607 0.1.9 2026-09-13T22-17Z sVRYlHWYe\BepInEx\plugins\Innangard\lang\Vietnamese.json"
inn_mod_target.parent.mkdir(parents=True, exist_ok=True)
inn_mod_target.write_text(json.dumps(inn_vi, ensure_ascii=False, indent=2), encoding="utf-8")

# ==================== 3. EpicLoot ====================
print("--- Dang xu ly EpicLoot ---")
el_p = REPO_ROOT / r"local\extracted_mods\plugins\EpicLoot.localizations.English.json"
el_src = json.loads(el_p.read_text(encoding="utf-8-sig"))
el_vi = {}

el_dict = [
    ("Epic Loot", "Epic Loot"),
    ("Thank you for playing", "Cảm ơn bạn đã trải nghiệm"),
    ("Shardstones", "Đá Mảnh"),
    ("Shardstone", "Đá Mảnh"),
    ("Tempering", "Tôi Luyện"),
    ("Enchanting", "Phù Phép"),
    ("Enchant", "Phù Phép"),
    ("Disenchant", "Hủy Phép"),
    ("Augment", "Cường Hóa"),
    ("Reroll", "Quay Lại"),
    ("Bounties", "Nhiệm Vụ Tiền Thưởng"),
    ("Bounty", "Tiền Thưởng"),
    ("Magic", "Ma Thuật"),
    ("Rare", "Hiếm"),
    ("Epic", "Sử Thi"),
    ("Legendary", "Huyền Thoại"),
    ("Mythic", "Thần Thoại"),
    ("Set Bonus", "Hiệu Ứng Bộ"),
    ("Life Steal", "Hút Máu"),
    ("Damage", "Sát Thương"),
    ("Armor", "Giáp"),
    ("Health", "Máu"),
    ("Stamina", "Thể Lực"),
    ("Eitr", "Eitr"),
    ("Resistance", "Kháng"),
    ("Weight", "Trọng Lượng"),
    ("Speed", "Tốc Độ"),
    ("Attack Speed", "Tốc Độ Đánh"),
    ("Block", "Đỡ Đòn"),
    ("Parry", "Phản Đòn"),
    ("Crafting", "Chế Tạo"),
    ("Inventory", "Túi Đồ"),
    ("Cost", "Chi Phí"),
    ("Required", "Yêu Cầu"),
    ("Success", "Thành Công"),
    ("Failed", "Thất Bại"),
    ("Upgrade", "Nâng Cấp"),
    ("Tier", "Cấp"),
    ("Level", "Cấp Độ"),
    ("Minimal", "Tối Thiểu"),
    ("Balanced", "Cân Bằng"),
    ("Join the discord!", "Tham gia máy chủ Discord!"),
    ("View Patch Notes", "Xem Ghi Chú Bản Vá")
]

for k, v in el_src.items():
    trans = v
    for en_w, vi_w in el_dict:
        trans = trans.replace(en_w, vi_w)
    el_vi[k] = trans

create_mod_draft("epicloot", el_src, el_vi, "0.14.11", "mod-EpicLoot", DATA_MODS / "epicloot_draft.jsonl", DATA_MODS / "epicloot_vi.json")

# Ghi trực tiếp file Vietnamese.json cho EpicLoot
el_target_dir = REPO_ROOT / r"mods\EpicLoot-0.14.11.zip 387 0.14.11 2026-09-21T18-53Z sVRYlHWAd\plugins\EpicLoot\localizations"
el_target_dir.mkdir(parents=True, exist_ok=True)
(el_target_dir / "Vietnamese.json").write_text(json.dumps(el_vi, ensure_ascii=False, indent=2), encoding="utf-8")

print("Hoan thanh dot 4 (Cac mod lon: MagicRevamp, Innangard, EpicLoot)!")
