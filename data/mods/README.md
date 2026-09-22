# Bản dịch mod

Kho dữ liệu ứng viên dịch tiếng Việt cho các bản mod Valheim, định dạng JSONL theo schema chuẩn của dự án:
Mỗi dòng bao gồm: `namespace`, `key`, `source_sha256`, `technical_signature`, `vi`, `status`, `origin`, `game_build`, `mod_version`, `reviewer`.

## Danh mục mod đã tách và dịch (22/09/2026)

| STT | Mod | Namespace | Số lượng key | Nguồn trích xuất |
| --- | --- | --- | --- | --- |
| 1 | **EpicLoot** | `epicloot` | 2.114 | `EpicLoot.localizations.English.json` |
| 2 | **Innangard** | `innangard` | 757 | `Innangard.English.json` |
| 3 | **CoreWoodExtras** | `corewoodextras` | 359 | `CoreWoodExtras.json` |
| 4 | **SeneaL UI** | `senealui` | 358 | `SeneaLUI.Languages.en.txt` |
| 5 | **MagicRevamp** | `magicrevamp` | 343 | `MagicRevamp.translations.English.yml` |
| 6 | **ValheimArmory** | `valheimarmory` | 286 | `ValheimArmory.localizations.English.json` |
| 7 | **PlanBuild** | `planbuild` | 174 | `PlanBuild.english.json` (hợp nhất từ `Valheim_Mod`) |
| 8 | **WeaponAdditions** | `weaponadditions` | 80 | `WeaponAdditions.translations.English.yml` |
| 9 | **Skyheim** | `skyheim` | 77 | `skyheim.json` |
| 10 | **Digitalroot.ArrowsJvL** | `digitalroot_arrows` | 40 | `translations.json` |
| 11 | **QuickStackStore** | `quickstackstore` | 29 | `QuickStackStore.Translations.QuickStackStore.English.json` |
| 12 | **Jotunn** | `jotunn` | 21 | `JotunnLib/Localization/English.json` |
| 13 | **MagicBows** | `magicbows` | 20 | `MagicBows.translations.English.yml` |
| 14 | **Better Archery** | `betterarchery` | 11 | `betterarchery_translations.json` |
| 15 | **TeleportEverything** | `teleporteverything` | 8 | `TeleportEverything.translations.English.yml` |
| 16 | **DvergerStaves** | `dvergerstaves` | 7 | `DvergerStaves.translations.English.yml` |
| 17 | **ModSettings** | `modsettings` | 4 | `ModSettings` |
| 18 | **CraftFromChestsPlus** | `craftfromchestsplus` | 1 | `CraftFromChestsPlus.Languages.en.json` |

## Triển khai và Kiểm thử

Chạy công cụ triển khai tự động:
```bash
python tools/deploy_translations.py
```
Lệnh trên sẽ tự động cập nhật bản dịch tiếng Việt cho cả Game và tất cả các Mod vào các thư mục game trên máy (`Valheim`, `Valheim_Mod`, `Valheim_vi_mod`, `Valheim - Copy`, `Valheim_vi`).
