import hashlib
import json
import re
from pathlib import Path
import yaml

REPO_ROOT = Path(r"E:\SteamLibrary\steamapps\common\valheim-vietnamese-community")
DATA_MODS = REPO_ROOT / "data" / "mods"
DATA_MODS.mkdir(parents=True, exist_ok=True)

def signature(value):
    tokens = re.findall(r"\$[A-Za-z_0-9][\w]*|\{\d+(?::[^{}]+)?\}|<[^>]+>", value)
    return hashlib.sha256(json.dumps(sorted(tokens), ensure_ascii=False).encode("utf-8")).hexdigest()

def create_mod_draft(namespace, source_dict, trans_dict, mod_version, origin, out_jsonl, out_vi_json=None):
    rows = []
    clean_trans = {}
    for k, orig in sorted(source_dict.items()):
        if not isinstance(orig, str) or not orig.strip():
            continue
        vi_val = trans_dict.get(k, orig)
        # Kiem tra token
        orig_sig = signature(orig)
        vi_sig = signature(vi_val)
        if orig_sig != vi_sig:
            print(f"[{namespace}] CANH BAO TOKEN KHONG KHOP cho key '{k}': orig='{orig}', vi='{vi_val}' -> Giu nguyen token goc")
            # Tự động thay thế hoặc điều chỉnh token
            orig_tokens = re.findall(r"\$[A-Za-z_0-9][\w]*|\{\d+(?::[^{}]+)?\}|<[^>]+>", orig)
            vi_tokens = re.findall(r"\$[A-Za-z_0-9][\w]*|\{\d+(?::[^{}]+)?\}|<[^>]+>", vi_val)
            # Neu token bi mat, bo sung lai
            for t in orig_tokens:
                if t not in vi_val:
                    vi_val += f" {t}"
        
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

# --- 1. CraftFromChestsPlus ---
cfc_src = {"cfc_loaded": "CraftFromChestsPlus ready (range {0:0.#} m)"}
cfc_vi = {"cfc_loaded": "CraftFromChestsPlus đã sẵn sàng (phạm vi {0:0.#} m)"}
create_mod_draft("craftfromchestsplus", cfc_src, cfc_vi, "1.0.5", "mod-CraftFromChestsPlus", DATA_MODS / "craftfromchestsplus_draft.jsonl", DATA_MODS / "craftfromchestsplus_vi.json")

# --- 2. DvergerStaves ---
dverger_src = {
    "bds_dvergerstaff_fire": "Dverger Staff (Fire)",
    "bds_dvergerstaff_fire_description": "A powerful staff created by dvergers.",
    "bds_dvergerstaff_heal": "Dverger Staff (Heal)",
    "bds_dvergerstaff_heal_description": "A powerfull healing staff created by dvergers.",
    "bds_dvergerstaff_ice": "Dverger Staff (Ice)",
    "bds_dvergerstaff_ice_description": "A powerful staff created by dvergers.",
    "bds_mistile": "Wisp"
}
dverger_vi = {
    "bds_dvergerstaff_fire": "Gậy Dverger (Lửa)",
    "bds_dvergerstaff_fire_description": "Cây trượng quyền năng do người Dverger chế tác.",
    "bds_dvergerstaff_heal": "Gậy Dverger (Trị Thương)",
    "bds_dvergerstaff_heal_description": "Cây trượng hồi phục đầy quyền năng do người Dverger chế tác.",
    "bds_dvergerstaff_ice": "Gậy Dverger (Băng)",
    "bds_dvergerstaff_ice_description": "Cây trượng quyền năng mang sức mạnh băng giá do người Dverger chế tác.",
    "bds_mistile": "Linh Hồn Khói (Wisp)"
}
create_mod_draft("dvergerstaves", dverger_src, dverger_vi, "1.1.0", "mod-DvergerStaves", DATA_MODS / "dvergerstaves_draft.jsonl", DATA_MODS / "dvergerstaves_vi.json")

# --- 3. TeleportEverything ---
tele_src = {
    "te_transporting_allies_message": "Transporting $1 allies!",
    "te_transported_allies_message": "Transported $1 allies. Transport allies enabled: $2.",
    "te_transporting_enemies_message": "Beware: $1 enemies may charge the portal!",
    "te_transported_enemies_message": "Taking Enemies With You! $1 enemies charge the portal!!!",
    "te_vikings_dont_run": "Vikings Don't run from a fight: $1 enemies with in $2 meters.",
    "te_deducted_items_message": "$1 out of $2 items deducted as a fee for transporting contraband.",
    "te_deducted_items_detailed_message": "$1 out of $2 $3 deducted as a fee for transporting contraband.",
    "te_item_transport_fee": "Transport Fee: <color=orange>$1%</color>"
}
tele_vi = {
    "te_transporting_allies_message": "Đang dịch chuyển $1 đồng minh!",
    "te_transported_allies_message": "Đã dịch chuyển $1 đồng minh. Bật dịch chuyển đồng minh: $2.",
    "te_transporting_enemies_message": "Coi chừng: $1 kẻ địch có thể lao qua cổng!",
    "te_transported_enemies_message": "Dẫn theo kẻ địch! $1 kẻ thù tràn qua cổng!!!",
    "te_vikings_dont_run": "Chiến binh Viking không trốn chạy trận chiến: $1 kẻ thù trong phạm vi $2 mét.",
    "te_deducted_items_message": "Đã trừ $1 trên tổng số $2 vật phẩm làm phí vận chuyển hàng cấm.",
    "te_deducted_items_detailed_message": "Đã trừ $1 trên tổng số $2 $3 làm phí vận chuyển hàng cấm.",
    "te_item_transport_fee": "Phí Vận Chuyển: <color=orange>$1%</color>"
}
create_mod_draft("teleporteverything", tele_src, tele_vi, "2.9.1", "mod-TeleportEverything", DATA_MODS / "teleporteverything_draft.jsonl", DATA_MODS / "teleporteverything_vi.json")

# --- 4. Better Archery ---
ba_src_path = REPO_ROOT / "mods" / "Better Archery 348 2.0.2 2026-09-20T10-37Z OSa6kCD1S" / "BetterArchery" / "plugins" / "betterarchery_translations.json"
ba_src = json.loads(ba_src_path.read_text(encoding="utf-8-sig"))
ba_vi = {
    "mod_betterarchery_test": "Đã Tải",
    "mod_betterarchery_tombstone_space_error": "Không đủ chỗ trong túi đồ, Vật phẩm bị rơi:",
    "mod_betterarchery_quiver_equipped_error": "Bạn không thể thả ống tên khi đang trang bị.",
    "mod_betterarchery_quiver_wrong_item_error": "Bạn không thể đặt vật phẩm này vào ống tên.",
    "mod_betterarchery_quiver_transfer_chest_error": "Hãy tháo trang bị vật phẩm trước.",
    "mod_betterarchery_quiver_item_swap_error": "Không thể đổi vật phẩm này.",
    "mod_betterarchery_quiver_swap_chest_error": "Tháo trang bị vật phẩm trước khi di chuyển.",
    "mod_betterarchery_quiver_drop_outside_error": "Tháo trang bị ống tên trước.",
    "mod_betterarchery_quiver_unequip_error": "Lấy hết tên trong ống ra trước.",
    "mod_betterarchery_quiver_no_room_error": "Ống tên đã đầy.",
    "mod_betterarchery_arrow_retrieval_success": "Đã thu hồi {0} mũi tên.",
    "mod_betterarchery_zoom_tooltip": "Ngắm bắn bằng cung",
    "mod_betterarchery_sneak_tooltip": "Bắn lén lút",
    "mod_betterarchery_bow_draw_tooltip": "Kéo dây cung",
    "mod_betterarchery_arrow_slot": "Khe Đựng Tên"
}
for k in ba_src:
    if k not in ba_vi:
        ba_vi[k] = ba_src[k]
create_mod_draft("betterarchery", ba_src, ba_vi, "2.0.2", "mod-BetterArchery", DATA_MODS / "betterarchery_draft.jsonl", DATA_MODS / "betterarchery_vi.json")

# --- 5. MagicBows ---
mb_src = {
    "bmb_fierybow": "Fiery Bow",
    "bmb_fierybow_description": "An ancient bow forge from the burning souls of the fallen and imbued with the magic of flames.",
    "bmb_frozenbow": "Frozen Bow",
    "bmb_frozenbow_description": "An ancient bow frozen in the battlefield along with its master.",
    "bmb_lightningbow": "Lightning Bow",
    "bmb_lightningbow_description": "An ancient bow rarely used by the god of thunder.",
    "bmb_spiritbow": "Spirit Bow",
    "bmb_spiritbow_description": "An ancient bow cursed and haunted by its victims.",
    "bmb_toxicbow": "Toxic Bow",
    "bmb_toxicbow_description": "An ancient bow found in the depths of the swamps soaked with the most poisonous substance for over a thousand years.",
    "bmb_crossbow_fiery": "Fiery Crossbow",
    "bmb_crossbow_fiery_description": "An ancient crossbow forge in the depths of hell.",
    "bmb_crossbow_frozen": "Frozen Crossbow",
    "bmb_crossbow_frozen_description": "An ancient crossbow covered in perpetual frost.",
    "bmb_crossbow_lightning": "Lightning Crossbow",
    "bmb_crossbow_lightning_description": "An ancient crossbow crackling with pure storm energy.",
    "bmb_crossbow_spirit": "Spirit Crossbow",
    "bmb_crossbow_spirit_description": "An ancient crossbow whispering echoes of the deceased.",
    "bmb_crossbow_toxic": "Toxic Crossbow",
    "bmb_crossbow_toxic_description": "An ancient crossbow dripping with deadly venom."
}
mb_vi = {
    "bmb_fierybow": "Cung Rực Lửa",
    "bmb_fierybow_description": "Cây cung cổ đại được rèn từ linh hồn thiêu đốt của những kẻ bại trận và thấm đẫm ma thuật lửa.",
    "bmb_frozenbow": "Cung Băng Giá",
    "bmb_frozenbow_description": "Cây cung cổ bị đóng băng trên chiến trường cùng với chủ nhân của nó.",
    "bmb_lightningbow": "Cung Sấm Sét",
    "bmb_lightningbow_description": "Cây cung cổ đại từng được thần sấm sử dụng.",
    "bmb_spiritbow": "Cung Linh Hồn",
    "bmb_spiritbow_description": "Cây cung cổ mang lời nguyền và bị ám bởi các nạn nhân của nó.",
    "bmb_toxicbow": "Cung Độc Tố",
    "bmb_toxicbow_description": "Cây cung cổ được tìm thấy dưới đáy đầm lầy, ngâm trong chất độc kịch độc hơn ngàn năm.",
    "bmb_crossbow_fiery": "Nỏ Rực Lửa",
    "bmb_crossbow_fiery_description": "Cây nỏ cổ đại được rèn từ nơi sâu thẳm của địa ngục.",
    "bmb_crossbow_frozen": "Nỏ Băng Giá",
    "bmb_crossbow_frozen_description": "Cây nỏ cổ bị bao phủ bởi lớp sương giá vĩnh cửu.",
    "bmb_crossbow_lightning": "Nỏ Sấm Sét",
    "bmb_crossbow_lightning_description": "Cây nỏ cổ kêu lách tách mang năng lượng bão tố thuần khiết.",
    "bmb_crossbow_spirit": "Nỏ Linh Hồn",
    "bmb_crossbow_spirit_description": "Cây nỏ cổ thì thầm tiếng vọng của những người đã khuất.",
    "bmb_crossbow_toxic": "Nỏ Độc Tố",
    "bmb_crossbow_toxic_description": "Cây nỏ cổ rỉ ra nọc độc chết người."
}
create_mod_draft("magicbows", mb_src, mb_vi, "1.1.9", "mod-MagicBows", DATA_MODS / "magicbows_draft.jsonl", DATA_MODS / "magicbows_vi.json")

print("Hoan thanh dot 1!")
