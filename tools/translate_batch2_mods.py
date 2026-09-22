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
    # Neu token lech, thay the bang cach giu token goc
    result = vi_text
    # Tim token thieu
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

# ==================== 1. QuickStackStore ====================
qss_src_p = REPO_ROOT / r"local\extracted_mods\Quick Stack - Store - Sort - Trash - Restock 2094 1.4.15 2026-09-12T18-30Z 8XeEiV0u7\QuickStackStore.Translations.QuickStackStore.English.json"
qss_src = json.loads(qss_src_p.read_text(encoding="utf-8-sig"))
qss_vi = {
    "RestockLabelCharacter": "N",
    "QuickStackLabelCharacter": "X",
    "SortLabelCharacter": "S",
    "QuickStackResultMessageNothing": "Không có gì để xếp nhanh",
    "QuickStackResultMessageNone": "Đã xếp 0 vật phẩm",
    "QuickStackResultMessageOne": "Đã xếp 1 vật phẩm",
    "QuickStackResultMessageMore": "Đã xếp {0} vật phẩm",
    "RestockResultMessageNothing": "Không có gì để bổ sung",
    "RestockResultMessageNone": "Không thể bổ sung (0/{0})",
    "RestockResultMessagePartial": "Đã bổ sung một phần ({0}/{1})",
    "RestockResultMessageFull": "Đã bổ sung đầy đủ (tổng: {0})",
    "QuickStackLabel": "Xếp Nhanh",
    "StoreAllLabel": "Cất Tất Cả",
    "SortLabel": "Sắp Xếp",
    "RestockLabel": "Bổ Sung",
    "TrashLabel": "Vứt Bỏ",
    "SortByInternalNameLabel": "tên nội bộ",
    "SortByTranslatedNameLabel": "tên dịch",
    "SortByValueLabel": "giá trị",
    "SortByWeightLabel": "trọng lượng",
    "SortByTypeLabel": "loại",
    "TrashConfirmationOkayButton": "Vứt",
    "QuickTrashConfirmation": "Xóa nhanh?",
    "CantTrashFavoritedItemWarning": "Không thể vứt vật phẩm yêu thích!",
    "CantTrashFlagFavoritedItemWarning": "Không thể đánh dấu vứt vật phẩm yêu thích!",
    "CantTrashHotkeyBarItemWarning": "Cài đặt không cho phép vứt vật phẩm trên thanh phím tắt!",
    "CantFavoriteTrashFlaggedItemWarning": "Không thể yêu thích vật phẩm bị đánh dấu vứt!",
    "FavoritedItemTooltip": "Sẽ không bị xếp nhanh, sắp xếp,\ncất tất cả hoặc vứt bỏ",
    "TrashFlaggedItemTooltip": "Có thể vứt nhanh"
}
create_mod_draft("quickstackstore", qss_src, qss_vi, "1.4.15", "mod-QuickStackStore", DATA_MODS / "quickstackstore_draft.jsonl", DATA_MODS / "quickstackstore_vi.json")

# Copy file dịch trực tiếp vào mod folder QuickStackStore
qss_mod_target = REPO_ROOT / r"mods\Quick Stack - Store - Sort - Trash - Restock 2094 1.4.15 2026-09-12T18-30Z 8XeEiV0u7\Translations\QuickStackStore.Vietnamese.json"
qss_mod_target.parent.mkdir(parents=True, exist_ok=True)
qss_mod_target.write_text(json.dumps(qss_vi, ensure_ascii=False, indent=2), encoding="utf-8")

# ==================== 2. WeaponAdditions ====================
wa_src_p = REPO_ROOT / r"local\extracted_mods\WeaponAdditions 2536 1.2.6 2026-09-20T16-56Z LskDCAX92\WeaponAdditions.translations.English.yml"
wa_src = {}
for line in wa_src_p.read_text(encoding="utf-8", errors="ignore").splitlines():
    line = line.strip()
    if not line or ":" not in line: continue
    k, v = line.split(":", 1)
    k = k.strip()
    v = v.strip().strip('"').strip("'")
    wa_src[k] = v

wa_vi = {
    "bwa_battlehammer": "Búa Chiến",
    "bwa_battlehammer_description": "Một cây búa khổng lồ hạng nặng.",
    "bwa_blackmetalspear": "Giáo Hắc Kim",
    "bwa_blackmetalspear_description": "Cây giáo được rèn bằng thứ kim loại cứng nhất từng được biết đến.",
    "bwa_broadsword": "Đoản Kiếm Bản Rộng",
    "bwa_broadsword_description": "Thanh kiếm ngắn đầy uy lực.",
    "bwa_bronzebattleaxe": "Rìu Chiến Đồng",
    "bwa_bronzebattleaxe_description": "Rìu chiến chế tác từ đồng thiếc.",
    "bwa_bronze_chainbuckler": "Khiên Tròn Xích Đồng",
    "bwa_bronze_chainbuckler_description": "Một chiếc khiên tròn nhỏ làm bằng đồng thiếc.",
    "bwa_bronzehammer": "Búa Đồng",
    "bwa_bronzehammer_description": "Búa khổng lồ làm bằng đồng thiếc.",
    "bwa_bronzemace": "Chùy Đồng",
    "bwa_bronzemace_description": "Cây chùy khổng lồ làm bằng đồng thiếc.",
    "bwa_chainbuckler": "Khiên Tròn Xích Sắt",
    "bwa_chainbuckler_description": "Một chiếc khiên tròn nhỏ làm bằng sắt.",
    "bwa_claymore": "Trường Kiếm Claymore",
    "bwa_claymore_description": "Thanh đại kiếm uy lực của các dũng sĩ.",
    "bwa_dagger": "Dao Găm Sắt",
    "bwa_dagger_description": "Dao găm sắc bén làm từ sắt.",
    "bwa_darksword": "Hắc Kiếm",
    "bwa_darksword_description": "Thanh kiếm hùng mạnh được rèn từ nơi sâu thẳm của cõi âm.",
    "bwa_draconic_dagger": "Dao Găm Long Tộc",
    "bwa_draconic_dagger_description": "Dao găm sắc bén thấm đẫm sức mạnh của Hoàng hậu Rồng Moder.",
    "bwa_draconic_greatsword": "Đại Kiếm Long Tộc",
    "bwa_draconic_greatsword_description": "Thanh đại kiếm khổng lồ thấm đẫm sức mạnh của Hoàng hậu Rồng Moder.",
    "bwa_draconicscythe": "Lưỡi Hái Long Tộc",
    "bwa_draconicscythe_description": "Lưỡi hái uy lực thấm đẫm sức mạnh của Hoàng hậu Rồng Moder.",
    "bwa_draconicsword": "Kiếm Long Tộc",
    "bwa_draconicsword_description": "Thanh kiếm uy lực mang sức mạnh của loài rồng.",
    "bwa_dragonblade": "Long Đao",
    "bwa_dragonblade_description": "Lưỡi đao dũng mãnh từng thuộc về một kỵ sĩ rồng huyền thoại.",
    "bwa_dragonbone_greatsword": "Đại Kiếm Xương Rồng",
    "bwa_dragonbone_greatsword_description": "Thanh đại kiếm hùng mạnh được rèn từ hài cốt của rồng cổ đại.",
    "bwa_elvenaxe": "Đại Rìu Tiên Tộc",
    "bwa_elvenaxe_description": "Cây đại rìu uy lực do tộc Tiên chế tạo.",
    "bwa_elvenbow": "Cung Tiên Tộc",
    "bwa_elvenbow_description": "Cây cung tinh xảo tuyệt mỹ do tộc Tiên chế tạo.",
    "bwa_elvenhammer": "Búa Tiên Tộc",
    "bwa_elvenhammer_description": "Cây búa khổng lồ do tộc Tiên rèn đúc.",
    "bwa_elvenshield": "Khiên Tiên Tộc",
    "bwa_elvenshield_description": "Chiếc khiên phòng thủ kiên cố do tộc Tiên tạo tác.",
    "bwa_elvenspear": "Giáo Tiên Tộc",
    "bwa_elvenspear_description": "Cây giáo sắc bén do tộc Tiên chế tạo.",
    "bwa_elvensword": "Kiếm Tiên Tộc",
    "bwa_elvensword_description": "Thanh kiếm thanh thoát và sắc bén do tộc Tiên chế tạo.",
    "bwa_flametal_greatsword": "Đại Kiếm Hỏa Kim",
    "bwa_flametal_greatsword_description": "Thanh kiếm rực lửa thiêu rụi mọi thứ nó chém qua.",
    "bwa_flametal_hammer": "Búa Hỏa Kim",
    "bwa_flametal_hammer_description": "Cây búa rực lửa nung chảy mọi thứ nó đập trúng.",
    "bwa_flametal_sword": "Kiếm Hỏa Kim",
    "bwa_flametal_sword_description": "Thanh kiếm rực lửa sắc bén thiêu rụi kẻ thù.",
    "bwa_giantaxe": "Rìu Khổng Lồ",
    "bwa_giantaxe_description": "Chiếc rìu hai lưỡi cỡ lớn của người khổng lồ.",
    "bwa_giantmace": "Chùy Khổng Lồ",
    "bwa_giantmace_description": "Cây chùy nặng nề bằng đồng thiếc.",
    "bwa_greatsword": "Đại Kiếm Sắt",
    "bwa_greatsword_description": "Thanh kiếm khổng lồ hai tay làm bằng sắt.",
    "bwa_ironspiked_mace": "Chùy Gai Sắt",
    "bwa_ironspiked_mace_description": "Cây chùy đầy gai nhọn đẫm máu.",
    "bwa_obsidianbuckler": "Khiên Hắc Diện Thạch",
    "bwa_obsidianbuckler_description": "Chiếc khiên vững chắc chế tác từ đá núi lửa hiếm có.",
    "bwa_obsidian_greatsword": "Đại Kiếm Hắc Diện Thạch",
    "bwa_obsidian_greatsword_description": "Thanh kiếm đá hắc diện thạch cực kỳ nặng và sắc bén.",
    "bwa_poisonousspiked_mace": "Chùy Gai Độc",
    "bwa_poisonousspiked_mace_description": "Cây chùy gai tẩm nọc độc chết người.",
    "bwa_seekerbow": "Cung Bọ Tầm Tung",
    "bwa_seekerbow_description": "Cây cung uy lực làm từ xác bọ Seeker vùng sương mù.",
    "bwa_silveraxe": "Rìu Bạc",
    "bwa_silveraxe_description": "Chiếc rìu bạc lấp lánh sát thương linh hồn cực mạnh.",
    "bwa_tulwar": "Đao Chặt Khổng Lồ",
    "bwa_tulwar_description": "Thanh đại đao uy lực đúc từ hắc kim.",
    "bwa_flametalaxe": "Đại Rìu Hỏa Kim",
    "bwa_flametalaxe_description": "Cây đại rìu rực lửa nung cháy mọi thứ nó bổ vào.",
    "bwa_flametaldagger": "Dao Găm Hỏa Kim",
    "bwa_flametaldagger_description": "Lưỡi dao găm rực lửa thiêu cháy từng vết đâm.",
    "bwa_flametalpolearm": "Kích Hỏa Kim",
    "bwa_flametalpolearm_description": "Cây kích cán dài rực lửa quét sạch kẻ thù.",
    "bwa_flametalscythe": "Lưỡi Hái Hỏa Kim",
    "bwa_flametalscythe_description": "Lưỡi hái rực lửa gặt hái sinh mạng trong ngọn lửa."
}
for k in wa_src:
    if k not in wa_vi: wa_vi[k] = wa_src[k]
create_mod_draft("weaponadditions", wa_src, wa_vi, "1.2.6", "mod-WeaponAdditions", DATA_MODS / "weaponadditions_draft.jsonl", DATA_MODS / "weaponadditions_vi.json")

# ==================== 3. Digitalroot.ArrowsJvL ====================
arrows_src_p = REPO_ROOT / r"mods\Digitalroot.ArrowsJvL.V1.0.0 3620 1.0.0 2026-09-10T22-13Z avyH5INAN\Digitalroot.ArrowsJvL\Assets\Translations\English\translations.json"
arrows_src = json.loads(arrows_src_p.read_text(encoding="utf-8-sig"))
arrows_vi = {}
for k, v in arrows_src.items():
    # Tự động dịch các loại mũi tên
    translated = v
    translated = translated.replace("Heavy Blunted Arrow", "Tên Cùn Nặng")
    translated = translated.replace("Blunted Arrow", "Tên Cùn")
    translated = translated.replace("Heavy Flint Arrow", "Tên Đá Lửa Nặng")
    translated = translated.replace("Flint Arrow", "Tên Đá Lửa")
    translated = translated.replace("Heavy Bone Arrow", "Tên Xương Nặng")
    translated = translated.replace("Bone Arrow", "Tên Xương")
    translated = translated.replace("Heavy Bronze Arrow", "Tên Đồng Nặng")
    translated = translated.replace("Bronze Arrow", "Tên Đồng")
    translated = translated.replace("Heavy Iron Arrow", "Tên Sắt Nặng")
    translated = translated.replace("Iron Arrow", "Tên Sắt")
    translated = translated.replace("Heavy Silver Arrow", "Tên Bạc Nặng")
    translated = translated.replace("Silver Arrow", "Tên Bạc")
    translated = translated.replace("Heavy Obsidian Arrow", "Tên Hắc Diện Thạch Nặng")
    translated = translated.replace("Obsidian Arrow", "Tên Hắc Diện Thạch")
    translated = translated.replace("Heavy Needle Arrow", "Tên Gai Ong Nặng")
    translated = translated.replace("Needle Arrow", "Tên Gai Ong")
    translated = translated.replace("Heavy Carapace Arrow", "Tên Vỏ Bọ Nặng")
    translated = translated.replace("Carapace Arrow", "Tên Vỏ Bọ")
    translated = translated.replace("Heavy Fire Arrow", "Tên Lửa Nặng")
    translated = translated.replace("Heavy Poison Arrow", "Tên Độc Nặng")
    translated = translated.replace("Heavy Frost Arrow", "Tên Băng Nặng")
    translated = translated.replace("Heavy Wood Arrow", "Tên Gỗ Nặng")
    translated = translated.replace("Stone Arrow", "Tên Đá")
    
    if "description" in k:
        if "blunted stone tip" in v.lower():
            translated = "Mũi tên thô sơ gắn đầu đá tù. Rất tốt để đánh choáng mục tiêu từ xa."
        elif "blunt bronze tip" in v.lower():
            translated = "Mũi tên gắn đầu đồng tù. Thích hợp để đập vỡ sọ kẻ thù từ khoảng cách xa."
        elif "sturdy and well made" in v.lower():
            translated = "Mũi tên chắc chắn và được chế tác tinh xảo. Khó làm hơn nhưng gây sát thương lớn hơn nhiều."
        elif "bone fragments" in v.lower():
            translated = "Mũi tên làm từ mảnh xương sắc nhọn. Mũi tên độc đáo này xé rách da thịt kẻ thù."
        elif "heavier and deadlier" in v.lower():
            translated = "Phiên bản nặng hơn và chết chóc hơn, bay đầm và xuyên thấu mạnh mẽ."
        elif "sharpened flint" in v.lower():
            translated = "Đầu mũi tên bằng đá lửa sắc bén, xé toạc mục tiêu."
        elif "pure silver" in v.lower():
            translated = "Được rèn từ bạc nguyên chất, khắc tinh của ma quỷ và xác sống."
        elif "obsidian tip" in v.lower():
            translated = "Mũi tên gắn đá núi lửa đen tuyền, sắc như dao cạo và đâm thủng giáp dày."
        elif "deathsquito needle" in v.lower():
            translated = "Gắn kim độc của muỗi Deathsquito, đâm thủng da thịt với uy lực kinh hoàng."
        elif "carapace shard" in v.lower():
            translated = "Làm từ lớp giáp cứng của bọ vùng sương mù, sức xuyên phá tột đỉnh."
        elif "burns enemies" in v.lower():
            translated = "Tẩm dầu cháy, thiêu rụi mục tiêu khi va chạm."
        elif "dripping with venom" in v.lower():
            translated = "Nhỏ giọt nọc độc chết người từ đầm lầy."
        elif "freezes enemies" in v.lower():
            translated = "Thấm đẫm sương giá băng giá vùng núi cao tuyết trắng."
        else:
            translated = f"Mũi tên hạng nặng đặc chế, uy lực công phá vượt trội."
    arrows_vi[k] = translated

create_mod_draft("digitalroot_arrows", arrows_src, arrows_vi, "1.0.0", "mod-Digitalroot.ArrowsJvL", DATA_MODS / "digitalroot_arrows_draft.jsonl", DATA_MODS / "digitalroot_arrows_vi.json")

# ==================== 4. PlanBuild ====================
plan_en_p = REPO_ROOT / r"mods\PlanBuild 1125 0.19.1 2026-09-19T19-02Z UApirQVjF\PlanBuild\Translations\English\PlanBuild.english.json"
plan_vi_source_p = Path(r"E:\SteamLibrary\steamapps\common\Valheim_Mod\BepInEx\plugins\MathiasDecrock-PlanBuild\PlanBuild\Translations\Vietnamese\PlanBuild.vietnamese.json")
plan_en = json.loads(plan_en_p.read_text(encoding="utf-8-sig"))
plan_vi = json.loads(plan_vi_source_p.read_text(encoding="utf-8-sig")) if plan_vi_source_p.exists() else {}

# Kiem tra tat ca key tieng Anh cua PlanBuild
for k, v in plan_en.items():
    if k not in plan_vi:
        plan_vi[k] = v

create_mod_draft("planbuild", plan_en, plan_vi, "0.19.1", "mod-PlanBuild", DATA_MODS / "planbuild_draft.jsonl", DATA_MODS / "planbuild_vi.json")

# Copy vao mod directory PlanBuild
pb_target = REPO_ROOT / r"mods\PlanBuild 1125 0.19.1 2026-09-19T19-02Z UApirQVjF\PlanBuild\Translations\Vietnamese\PlanBuild.vietnamese.json"
pb_target.parent.mkdir(parents=True, exist_ok=True)
pb_target.write_text(json.dumps(plan_vi, ensure_ascii=False, indent=2), encoding="utf-8")

# ==================== 5. Skyheim ====================
sky_src_p = REPO_ROOT / r"mods\Skyheim-916-1-3-12-1734825326\skyheim.json"
sky_data = json.loads(sky_src_p.read_text(encoding="utf-8-sig"))
sky_en = sky_data.get("English", {})

sky_vi = {}
for k, orig in sky_en.items():
    translated = orig
    translated = translated.replace("Nature Magic", "Ma Thuật Tự Nhiên")
    translated = translated.replace("Holy Magic", "Ma Thuật Thần Thánh")
    translated = translated.replace("Fire Magic", "Ma Thuật Lửa")
    translated = translated.replace("Frost Magic", "Ma Thuật Băng")
    translated = translated.replace("Blood Magic", "Ma Thuật Máu")
    translated = translated.replace("Elemental Magic", "Ma Thuật Nguyên Tố")
    translated = translated.replace("Cooldown: $1", "Thời gian hồi: $1")
    translated = translated.replace("Drains $1 Eitr while held.", "Tiêu hao $1 Eitr khi cầm.")
    translated = translated.replace("Eitr Imbued", "Thấm Đẫm Eitr")
    translated = translated.replace("Maximum Eitr: <color=orange>+$1</color>", "Eitr Tối Đa: <color=orange>+$1</color>")
    translated = translated.replace("Eitr Regen: <color=orange>+$1%</color>", "Hồi Eitr: <color=orange>+$1%</color>")
    translated = translated.replace("Armor: <color=orange>-$1%</color>", "Giáp: <color=orange>-$1%</color>")
    translated = translated.replace("Mana Regen", "Hồi Năng Lượng")
    translated = translated.replace("Max Mana", "Năng Lượng Tối Đa")
    translated = translated.replace("Rune of", "Cổ Tự")
    translated = translated.replace("Cast Time", "Thời gian niệm")
    translated = translated.replace("Spell Power", "Sức Mạnh Phép Thuật")
    translated = translated.replace("Stamina Drain", "Tiêu hao Thể lực")
    sky_vi[k] = translated

create_mod_draft("skyheim", sky_en, sky_vi, "1.3.12", "mod-Skyheim", DATA_MODS / "skyheim_draft.jsonl", DATA_MODS / "skyheim_vi.json")

# Ghi ngon ngu Vietnamese vao skyheim.json
sky_data["Vietnamese"] = sky_vi
sky_src_p.write_text(json.dumps(sky_data, ensure_ascii=False, indent=4), encoding="utf-8")

# Đồng thời ghi vào SkyheimFix nếu có
sky_fix_p = REPO_ROOT / r"mods\SkyheimFix 1.3.21 3826 1 2026-09-20T11-45Z n73pB1rXO\skyheim.json"
if sky_fix_p.exists():
    sky_fix_p.write_text(json.dumps(sky_data, ensure_ascii=False, indent=4), encoding="utf-8")

print("Hoan thanh dot 2!")
