# 🌲 Valheim Việt Hóa Cộng Đồng (Valheim Vietnamese Community)

> **Kho lưu trữ mã nguồn mở, cơ sở dữ liệu dịch thuật chuẩn hóa và bộ công cụ tự động hóa bản địa hóa toàn diện nhất dành cho tựa game Valheim (Patch 1.0.15 / Steam Build `25390630`) cùng hệ sinh thái hơn 18 bản mod phổ biến.**

---

## 🌟 Tổng Quan Dự Án & Chỉ Số Ấn Tượng

Dự án **Valheim Việt Hóa Cộng Đồng** được xây dựng nhằm cung cấp một giải pháp bản địa hóa tiếng Việt chuẩn mực, bền vững và tương thích tuyệt đối theo từng bản cập nhật chính thức của Valheim từ Iron Gate Studio. Thay vì các bản mod dịch đè file thiếu kiểm soát, dự án thiết lập một chuẩn kỹ thuật nghiêm ngặt: kiểm soát từng dòng dữ liệu bằng JSONL, bảo toàn nguyên vẹn 100% token kỹ thuật/biến số game, và hỗ trợ triển khai tự động chỉ với 1 dòng lệnh.

### 📊 Chỉ Số Dự Án (Tính đến 22/09/2026)

| Chỉ số | Giá trị | Ý nghĩa |
|---|---|---|
| **Tổng số bản ghi dịch thuật** | **10.736** dòng JSONL | Bao phủ toàn bộ Game gốc và 18 bản mod đồ sộ |
| **Độ khớp Token Signature** | **100.0%** (0 lỗi) | Đảm bảo tuyệt đối không lỗi placeholder `{0}`, `$item_...`, `<color>` |
| **Bản dịch Game Gốc** | **6.038 - 9.438** chuỗi | Bao phủ 100% text có nội dung của bản trích 1.0.15 |
| **Số lượng Mod đã dịch toàn diện** | **18 Mod lớn** | Gồm EpicLoot, Innangard, ValheimArmory, PlanBuild, Skyheim... |
| **Số lượng Mod trong hệ sinh thái** | **74 Mod** | Được khảo sát, phân loại và hướng dẫn cấu hình chi tiết |
| **Số lượng Plugin đã tích hợp** | **104 Plugins** | Sẵn sàng hoạt động trơn tru trong hồ sơ `Valheim_Mod` |
| **Kết quả kiểm định tự động (CI/Test)** | **PASS 100%** | Kiểm tra cú pháp, schema, chính sách bảo vệ file công khai |

---

## 📅 Trạng Thái Phiên Bản & Nền Tảng (Patch 1.0.15)

- **Client Game Local:** Steam build `25390630`, tương ứng bản vá Patch **1.0.15** chính thức ngày 18/09/2026.
- **Trích xuất Asset gốc:** Đã trích xuất hoàn chỉnh từ `resources.assets` (SHA-256: `86b7fbe9514e43f25bee157d1cc2c103680003118e9c3872459e34e264725f9d`) bao gồm **13 asset localization**, **6.056 key** và **37 ngôn ngữ** song song vào thư mục nội bộ `local/` (Git bỏ qua để tôn trọng bản quyền game gốc).
- **Hệ thống nạp ngôn ngữ:** Sử dụng plugin BepInEx `ValheimVietnamese` (mã nguồn C# sạch) can thiệp vào `Localization.LoadLanguages` và `Localization.SetupLanguage`, tự động thêm ngôn ngữ **"Tiếng Việt"** trực tiếp vào menu cài đặt của game mà không làm hỏng các ngôn ngữ khác.
- **Dedicated Server:** Bản máy chủ chuyên dụng nội bộ đạt build `21981590` (Steam đang nhắm tới `25390671`).

---

## 📂 Kiến Trúc Cấu Trúc Thư Mục Toàn Diện

Hệ thống thư mục được phân định ranh giới nghiêm ngặt giữa dữ liệu công khai trên GitHub và các bản chụp/tài nguyên cục bộ trên máy lập trình viên:

```text
valheim-vietnamese-community/
├── .github/                  # Quy trình CI/CD tự động kiểm tra cú pháp và schema
├── data/                     # DỮ LIỆU CÔNG KHAI (JSONL chuẩn hóa theo từng dòng)
│   ├── mods/                 # Bản dịch cho 18 bản mod lớn (dạng _draft.jsonl & _vi.json)
│   ├── valheim/              # Bản dịch cho game gốc Valheim (monokaijs_draft.jsonl & new_draft.jsonl)
│   └── README.md             # Hướng dẫn quy chuẩn dữ liệu data
├── docs/                     # TÀI LIỆU KỸ THUẬT & HƯỚNG DẪN DỰ ÁN
│   ├── FOLDER_GUIDE.md       # Giải thích chi tiết từng thư mục và tệp tin
│   ├── INTEGRATION.md        # Kết quả hợp nhất các nguồn cục bộ, framework và website
│   ├── MODS_GUIDE.md         # Cẩm nang chi tiết toàn bộ 74 mod Valheim
│   └── STATUS.md             # Báo cáo tiến độ và bảng kiểm định chất lượng (QA Status)
├── sources/                  # METADATA NGUỒN GỐC & GIẤY PHÉP
│   ├── game_build_25390630.json # Hash và số lượng key trích xuất từ build 1.0.15
│   └── local_sources.json    # Danh mục và chính sách sử dụng các bản chụp cục bộ
├── tools/                    # BỘ CÔNG CỤ TỰ ĐỘNG HÓA (CLI TOOLS)
│   ├── audit_candidates.py   # Rà soát tĩnh các chuỗi chưa dịch hoặc giữ nguyên English
│   ├── audit_local.py        # Kiểm kê các nguồn tài nguyên hiện có trên máy
│   ├── build_local_corpus.py # Lập chỉ mục tìm kiếm offline vào SQLite3
│   ├── build_translation.py  # Đóng gói bản dịch JSON theo namespace
│   ├── check_public_files.py # Cổng an toàn chặn leak file nhị phân/bản chụp vào Git
│   ├── deploy_translations.py# TRIỂN KHAI 1-CLICK bản dịch vào các thư mục game trên máy
│   ├── export_embedded_resources.ps1 # Trích xuất Manifest Resource từ DLL .NET bằng Reflection
│   ├── extract_game.py       # Trích xuất chuỗi từ resources.assets của game gốc
│   ├── install_mods_to_valheim_mod.py # Tự động cài đặt 24 siêu mod vào Valheim_Mod
│   ├── package_preview.py    # Đóng gói zip bản thử nghiệm BepInEx cục bộ
│   ├── search_local.py       # Tra cứu từ khóa nhanh trong cơ sở dữ liệu corpus
│   ├── translate_core_mods.py# Biên dịch các mod nhỏ và vừa
│   ├── translate_batch2_mods.py # Biên dịch QuickStack, WeaponAdditions, Arrows, PlanBuild, Skyheim
│   ├── translate_batch3_mods.py # Biên dịch CoreWoodExtras, ValheimArmory, SeneaL UI
│   ├── translate_large_mods.py  # Biên dịch MagicRevamp, Innangard, EpicLoot
│   └── validate.py           # THẨM ĐỊNH SCHEMA & CHỮ KÝ TOKEN SIGNATURE
├── tests/                    # CÁC BÀI KIỂM THỬ ĐƠN VỊ (UNIT TESTS)
│   └── test_validate.py      # Test case kiểm thử độ chính xác của bộ kiểm định
├── local/                    # THƯ MỤC CỤC BỘ (GIT BỎ QUA - KHÔNG COMMIT)
│   ├── game_sources.jsonl    # Chuỗi gốc tiếng Anh trích từ 1.0.15
│   ├── extracted_mods/       # Toàn bộ tài nguyên gốc đã trích xuất từ 74 DLL mod
│   └── source_inventory.json # Danh sách kiểm kê các bản chụp trên máy
├── mods/                     # THƯ MỤC LƯU TRỮ 74 MOD ĐẦU VÀO (GIT BỎ QUA)
├── Lich_Su_Truy_Van/         # NHẬT KÝ HOẠT ĐỘNG AGENT (LƯU NỘI BỘ MÁY CÁ NHÂN)
├── .gitignore                # Cấu hình loại trừ tuyệt đối file nhạy cảm và binary
├── CONTRIBUTING.md           # Quy chuẩn và hướng dẫn đóng góp bản dịch
├── LICENSE                   # Giấy phép mã nguồn mở MIT
└── README.md                 # Tài liệu tổng quan dự án này
```

---

## ⚙️ Cơ Chế Kỹ Thuật & Thuật Toán Bảo Toàn Token

Một trong những nguyên nhân hàng đầu khiến các bản mod Việt hóa game Valheim trước đây gây lỗi crash game hoặc hiển thị sai lệch giao diện là do người dịch vô tình làm biến đổi các token nội bộ của engine Unity. Dự án áp dụng thuật toán chữ ký kỹ thuật **`technical_signature`** để giám sát và bảo đảm 100% tính nguyên vẹn:

### Thuật toán tính chữ ký kỹ thuật:
```python
def signature(value: str) -> str:
    # Bắt tất cả các token game: $từ_khóa, {0}, {1:0.#}, <color=orange>, </color>, v.v.
    tokens = re.findall(r"\$[A-Za-z_0-9][\w]*|\{\d+(?::[^{}]+)?\}|<[^>]+>", value)
    return hashlib.sha256(json.dumps(sorted(tokens), ensure_ascii=False).encode("utf-8")).hexdigest()
```

### Quy chuẩn cấu trúc mỗi dòng dữ liệu (`data/**/*.jsonl`):
Mỗi dòng trong tệp `.jsonl` là một đối tượng JSON độc lập, bắt buộc chứa 10 trường:
1. `namespace`: Không gian tên phân định bản dịch (`valheim`, `epicloot`, `planbuild`, `skyheim`...).
2. `key`: Mã định danh chuỗi nguyên bản trong mã nguồn game/mod.
3. `source_sha256`: Mã băm SHA-256 của chuỗi tiếng Anh gốc (phát hiện khi nhà phát triển sửa văn bản gốc).
4. `technical_signature`: Mã băm chữ ký của toàn bộ tập hợp token trong chuỗi.
5. `vi`: Chuỗi bản dịch tiếng Việt (bắt buộc phải có chữ ký token khớp 100% với gốc).
6. `status`: Trạng thái xử lý (`draft`: bản nháp đã đối soát token; `reviewed`: đã kiểm tra ngữ cảnh trong game).
7. `origin`: Nguồn gốc xuất xứ của bản dịch (ví dụ: `monokaijs-mit`, `mod-EpicLoot`, `project-written`).
8. `game_build`: Bản build game mục tiêu (ví dụ: `25390630`).
9. `mod_version`: Phiên bản mod tương ứng (hoặc `unknown`).
10. `reviewer`: Tên người thẩm định ngữ cảnh khi chuyển sang trạng thái `reviewed`.

---

## 🎮 Hệ Thống Bản Dịch Game Gốc (Valheim Vanilla)

Dự án kế thừa và phát triển từ nhiều nguồn tư liệu lịch sử quý giá, được thanh lọc và nâng cấp bài bản:
- **6.021 key** kế thừa từ bản dịch cộng đồng giấy phép MIT của tác giả `monokaijs`.
- **17 key độc quyền mới** được dự án trực tiếp biên dịch bổ sung cho các nội dung của Patch 1.0.15.
- **735 key cộng đồng trau chuốt** được trích từ nguồn `community_translation.json` (chuẩn hóa tên quần xã, tên quái vật, thảo mộc).
- **Hơn 3.400 key mở rộng** được tích hợp và đối soát từ kho lưu trữ `all_translations.json` trên các bản cài đặt thực tế.
- **Kết quả:** Bao phủ hoàn toàn 6.038/6.038 key tiếng Anh có nội dung và không xung đột của bản game 1.0.15 hiện tại.

---

## ⚔️ Kho Bản Dịch 18 Siêu Mod Đã Hoàn Thiện (Chi Tiết Từng Mod)

Dự án đã sử dụng kỹ thuật Reflection .NET chuyên sâu để trích xuất các tệp tài nguyên nhúng (Embedded Manifest Resources) từ các DLL mod, tiến hành biên dịch và tạo dữ liệu kiểm chuẩn:

### 1. EpicLoot (v0.14.11) — 2.114 Key (`data/mods/epicloot_draft.jsonl`)
- **Tầm vóc:** Mod mở rộng nhập vai lớn nhất lịch sử Valheim Modding. Biến Valheim thành một tựa game RPG thực thụ phong cách Diablo.
- **Nội dung Việt hóa:**
  - Hệ thống 5 phẩm cấp trang bị: *Ma Thuật (Magic)*, *Hiếm (Rare)*, *Sử Thi (Epic)*, *Huyền Thoại (Legendary)*, *Thần Thoại (Mythic)*.
  - Toàn bộ các dòng hiệu ứng phù phép (Enchantments): Hút máu (Life Steal), Nhảy đôi (Double Jump), Đi trên nước (Water Walking), Giảm trọng lượng, Tăng tốc độ đánh.
  - Tính năng Tôi Luyện (Tempering) và Khảm Đá Mảnh (Shardstones) tại Hildir.
  - Hàng trăm nhiệm vụ săn tiền thưởng trùm khét tiếng (Bounties) nhận tại thương nhân Haldor.

### 2. Innangard (v0.1.9) — 757 Key (`data/mods/innangard_draft.jsonl`)
- **Tầm vóc:** Mod xây dựng xã hội và định cư Viking.
- **Nội dung Việt hóa:**
  - Cho phép chiêu mộ các Dân Định Cư (Settler) về ngôi làng của bạn.
  - Hệ thống nghề nghiệp: Thợ Xây, Thợ Săn, Ngư Dân, Nông Dân, Thợ Rèn, Lính Gác.
  - Búa Thợ Xây (Builder's Hammer) và cơ chế tự động xây dựng theo Bản Thiết Kế dưới vùng bảo hộ (Frith).

### 3. CoreWoodExtras (v2.2.6) — 359 Key (`data/mods/corewoodextras_draft.jsonl`)
- **Tầm vóc:** Đại tu kiến trúc và nội thất gỗ lõi.
- **Nội dung Việt hóa:** Hơn 50 chi tiết kiến trúc độc đáo: Quầy Chợ (Market Stall), Thùng đựng các loại cá (Cá vược, cá ngừ, cá hồi, trollfish), trụ vòm, cầu thang, giường, bàn ghế gỗ lõi tuyệt đẹp.

### 4. SeneaL UI (v1.1.3) — 358 Key (`data/mods/senealui_draft.jsonl`)
- **Tầm vóc:** Nâng cấp toàn diện giao diện hiển thị người dùng (HUD).
- **Nội dung Việt hóa:** Thanh máu chi tiết có số cụ thể, hiển thị kháng tính, thanh máu kẻ thù có cấp độ sao, chỉ số giáp, độ thoải mái (Comfort) và hệ thống nhảy số sát thương trực quan.

### 5. MagicRevamp (v1.5.1) — 343 Key (`data/mods/magicrevamp_draft.jsonl`)
- **Tầm vóc:** Mở rộng hệ thống trang phục và phép thuật cổ đại.
- **Nội dung Việt hóa:** Bộ trang phục Áo Choàng Rễ Cây (Rootweave), Bộ Tiên Phong Diệp Ảnh (Shadowleaf Vanguard), gậy phép nguyên tố và áo choàng pháp sư bóng đêm.

### 6. ValheimArmory (v1.33.0) — 286 Key (`data/mods/valheimarmory_draft.jsonl`)
- **Tầm vóc:** Kho vũ khí chiến binh đồ sộ bậc nhất.
- **Nội dung Việt hóa:** Bổ sung hàng trăm vũ khí mới trải dài qua các thời kỳ: Nỏ đá lửa, nỏ đồng, nỏ sắt, nỏ bạc, nỏ hắc kim; Đại kiếm hai tay, khiên tháp, chùy gai và bộ giáp xích chiến binh.

### 7. PlanBuild (v0.19.1) — 174 Key (`data/mods/planbuild_draft.jsonl`)
- **Tầm vóc:** Công cụ quy hoạch kiến trúc xây dựng đỉnh cao.
- **Nội dung Việt hóa:** Cơ chế đặt khung kế hoạch (Plan/Ghost piece) trước khi tốn tài nguyên thật, tính năng sao chép và lưu trữ Bản Thiết Kế (Blueprint) để chia sẻ cho cộng đồng.

### 8. WeaponAdditions (v1.2.6) — 80 Key (`data/mods/weaponadditions_draft.jsonl`)
- **Tầm vóc:** Bộ sưu tập vũ khí thần thoại đặc sắc.
- **Nội dung Việt hóa:** Vũ khí Long Tộc (Draconic) thấm đẫm sức mạnh Rồng Moder, Vũ khí Tộc Tiên (Elven), Vũ khí Hắc Diện Thạch (Obsidian) và loạt vũ khí Hỏa Kim (Flametal) rực lửa.

### 9. Skyheim / SkyheimFix (v1.3.12) — 77 Key (`data/mods/skyheim_draft.jsonl`)
- **Tầm vóc:** Hệ thống ma thuật cổ tự (Runes) lấy cảm hứng từ Skyrim.
- **Nội dung Việt hóa:** 4 nhánh ma thuật: Tự Nhiên, Thần Thánh, Lửa, Băng Giá; cơ chế hồi Eitr, thời gian hồi chiêu và các viên đá cổ tự phép thuật.

### 10. Digitalroot.ArrowsJvL (v1.0.0) — 40 Key (`data/mods/digitalroot_arrows_draft.jsonl`)
- **Tầm vóc:** Mở rộng kho tàng mũi tên thiện xạ.
- **Nội dung Việt hóa:** Mũi Tên Cùn Nặng (đập vỡ sọ kẻ thù từ xa), Mũi Tên Xương Nặng (xé rách da thịt), Tên Hắc Diện Thạch, Tên Bạc trừ tà và Tên Gai Ong sát thương khủng.

### 11. Quick Stack - Store - Sort - Trash - Restock (v1.4.15) — 29 Key (`data/mods/quickstackstore_draft.jsonl`)
- **Tầm vóc:** Tiện ích quản lý hòm đồ thiết yếu nhất game.
- **Nội dung Việt hóa:** Nút Xếp Nhanh (1 phím cất đồ vào tất cả rương quanh nhà), Sắp Xếp kho đồ, Cất Tất Cả, Bổ Sung vật phẩm tiêu hao và khóa vật phẩm Yêu Thích chống vứt nhầm.

### 12. Jotunn (v2.20+) — 21 Key (`data/mods/jotunn_draft.jsonl`)
- **Tầm vóc:** Framework nền tảng của cộng đồng modding Valheim.
- **Nội dung Việt hóa:** Các chuỗi thông báo hệ thống, quản lý nạp phím tắt và localization.

### 13. MagicBows (v1.1.9) — 20 Key (`data/mods/magicbows_draft.jsonl`)
- **Tầm vóc:** Bộ cung và nỏ ma thuật nguyên tố.
- **Nội dung Việt hóa:** Cung Rực Lửa, Cung Băng Giá, Cung Sấm Sét của thần sấm Thor, Cung Linh Hồn và Nỏ Độc Tố ngàn năm đầm lầy.

### 14. Better Archery (v2.0.2) — 11 Key (`data/mods/betterarchery_draft.jsonl`)
- **Tầm vóc:** Đại tu trải nghiệm bắn cung.
- **Nội dung Việt hóa:** Hệ thống Ống Đựng Tên (Quiver) riêng biệt, cơ chế rút ngắm phóng to màn hình và nhặt lại mũi tên sau trận chiến.

### 15. TeleportEverything (v2.9.1) — 8 Key (`data/mods/teleporteverything_draft.jsonl`)
- **Tầm vóc:** Tự do dịch chuyển qua cổng.
- **Nội dung Việt hóa:** Mang theo kim loại, hàng cấm qua cổng (có tính phí cấu hình), dịch chuyển theo thú thuần hóa (chó sói, lợn, lox) và cảnh báo kẻ địch đuổi theo qua cổng.

### 16. DvergerStaves (v1.1.0) — 7 Key (`data/mods/dvergerstaves_draft.jsonl`)
- **Tầm vóc:** Bộ gậy phép người lùn Dverger vùng sương mù.
- **Nội dung Việt hóa:** Gậy Lửa, Gậy Trị Thương hồi máu diện rộng và Gậy Băng Giá Dverger.

### 17. ModSettings — 4 Key (`data/mods/modsettings_draft.jsonl`)
- **Tầm vóc:** Giao diện tùy chỉnh cài đặt mod trực tiếp trong menu game.

### 18. CraftFromChestsPlus (v1.0.5) — 1 Key (`data/mods/craftfromchestsplus_draft.jsonl`)
- **Tầm vóc:** Tự động lấy tài nguyên từ các rương chứa trong phạm vi khi chế tạo tại bàn thợ rèn hoặc bàn chế tác.

---

## 🗺️ Cẩm Nang & Phân Loại 74 Mod Valheim

Bên cạnh 18 bản mod lớn có ngôn ngữ riêng đã được Việt hóa ở trên, kho `mods/` của dự án lưu trữ và quản lý **56 bản mod tiện ích gameplay và tối ưu đồ họa**. Các mod này can thiệp trực tiếp bằng mã Harmony Patch và cấu hình qua tệp `BepInEx/config/*.cfg`:

### Danh sách 56 Mod Tiện Ích Đã Tích Hợp Sẵn:
1. **VeinMining:** Đập một nhát cuốc phá vỡ toàn bộ mạch quặng lớn (đồng, sắt, bạc).
2. **Fast Repair Button:** Một nút bấm sửa toàn bộ trang bị trên bàn chế tác.
3. **HoldAttack:** Nhấn giữ chuột trái để tấn công liên tục mượt mà.
4. **Tools in Water:** Cho phép bơi dưới nước mà vẫn dùng rìu, búa, vũ khí bình thường.
5. **Instant Monster Drop:** Quái vật chết rơi chiến lợi phẩm ngay lập tức.
6. **AutoMapPins & Cartur's Map Pins:** Tự động ghim vị trí tài nguyên, hầm ngục lên bản đồ mini.
7. **BadgersSkiesFix:** Sửa lỗi ánh sáng mây, làm đẹp bầu trời Valheim.
8. **Valhalla ReShade HD & Comic GI:** Bộ lọc đồ họa chân thực / cel-shading tuyệt mỹ.
9. **Plant Everything & Plant Easily:** Trồng tất cả các loại cây rừng, hoa, nấm, quả dâu theo luống thẳng hàng.
10. **BeastMaster:** Thuần hóa và cưỡi hầu hết mọi loài sinh vật hoang dã.
11. **Valheim Legends:** Bổ sung 12 lớp nhân vật RPG (Pháp sư, Tu sĩ, Cung thủ, Berserker...) với cây kỹ năng riêng.
12. **Chest Label:** Gắn bảng tên chữ hiển thị trực quan phía trước mặt rương.
13. **Cartur's Safe Stamina:** Không tốn thể lực vô ích khi làm việc trong căn cứ an toàn.
14. **Death Tweaks:** Tùy biến hình phạt khi chết (giữ lại trang bị, không tụt điểm kỹ năng).
15. **AchievementEnabler / KeepAchivements:** Kích hoạt lại toàn bộ thành tựu Steam khi sử dụng mod.
16. **ValheimPlus:** Bộ công cụ cấu hình chuyên sâu mọi khía cạnh của thế giới game.
17. *(Xem danh sách đầy đủ 74 mod tại [docs/MODS_GUIDE.md](docs/MODS_GUIDE.md))*

---

## 🕹️ Kiến Trúc Vận Hành 2 Phiên Bản Game (Dual-Profile Architecture)

Dự án đề xuất và thiết lập giải pháp vận hành song song 2 phiên bản độc lập để tối ưu trải nghiệm và tiết kiệm dung lượng ổ đĩa:

```text
E:\SteamLibrary\steamapps\common\
├── Valheim/                   # PHIÊN BẢN 1: BẢN GỐC (VANILLA + TIẾNG VIỆT CHUẨN)
│   ├── valheim.exe            # Khởi động trực tiếp từ nút "Play" trên Steam
│   └── BepInEx/plugins/       # Chỉ gồm 3 plugin: Bộ nạp Tiếng Việt sạch (ValheimVietnamese)
│
└── Valheim_Mod/               # PHIÊN BẢN 2: SIÊU MOD (ĐẸP HƠN + 104 PLUGINS + TIẾNG VIỆT)
    ├── valheim.exe            # Khởi động qua Shortcut riêng ngoài Desktop
    └── BepInEx/plugins/       # Đầy đủ 104 plugins (EpicLoot, Vũ Khí, Phép Thuật, Đồ Họa ReShade...)
```

- **Khi muốn chơi thuần khiết, ổn định hoặc tham gia máy chủ công cộng:** Bạn mở Steam và bấm **Play** như bình thường.
- **Khi muốn phiêu lưu thế giới đồ họa đẹp, trang bị RPG rơi đồ phong phú:** Bạn vào thư mục `Valheim_Mod` chạy file `valheim.exe` (hoặc tạo Shortcut Desktop tên là *"Valheim Siêu Mod"*).

---

## 🛠️ Hướng Dẫn Sử Dụng Bộ Công Cụ (CLI Tooling)

Dự án cung cấp bộ kịch bản dòng lệnh tự động hóa toàn diện trong thư mục `tools/`:

### 1. Triển khai bản dịch tự động vào Game (1-Click Deploy)
Cập nhật toàn bộ bản dịch game và các mod vào các bản cài đặt Valheim trên máy:
```bash
python tools/deploy_translations.py
```
*(Nếu muốn cài đặt vào một thư mục game cụ thể: `python tools/deploy_translations.py --target "Đường_Dẫn_Thư_Mục"`)*

### 2. Bổ sung trọn bộ mod tuyển chọn vào `Valheim_Mod`
Tự động copy 24 siêu phẩm mod kèm bản dịch Tiếng Việt vào thư mục `Valheim_Mod`:
```bash
python tools/install_mods_to_valheim_mod.py
```

### 3. Thẩm định chất lượng dữ liệu (Data Validation)
Kiểm tra cú pháp JSONL, schema bắt buộc và độ khớp 100% của chữ ký token signature:
```bash
python tools/validate.py data
```

### 4. Kiểm tra an toàn bảo vệ kho công khai (Public File Checker)
Đảm bảo không commit file binary, DLL, file zip hoặc thư mục bản chụp nhạy cảm:
```bash
python tools/check_public_files.py
```

### 5. Chạy toàn bộ Unit Tests
```bash
python -m unittest discover -s tests
```

### 6. Trích xuất tài nguyên ngôn ngữ từ DLL .NET bằng Reflection
```powershell
pwsh -ExecutionPolicy Bypass -File tools/export_embedded_resources.ps1
```

---

## 📜 Chính Sách Bản Quyền & Nguồn Gốc (Provenance)

- **Mã nguồn công cụ và dữ liệu JSONL mới:** Phát hành công khai theo giấy phép mã nguồn mở **MIT License**.
- **Bản dịch game gốc:** Kế thừa từ công sức của tác giả `monokaijs` theo giấy phép MIT, kết hợp bổ sung độc quyền từ cộng đồng.
- **Bản dịch các Mod:** Tuân thủ giấy phép nguồn của từng tác giả mod gốc (Jotunn, EpicLoot, RandyKnapp...). Toàn bộ chuỗi ngôn ngữ gốc được trích xuất phục vụ mục đích bản địa hóa tương thích.
- **Trích dẫn nguồn gốc:** Dự án chỉ duy trì trích dẫn duy nhất đối với phiên bản game Valheim chính thức mới nhất (Steam Build `25390630` / Patch 1.0.15).

---

## 🤝 Đóng Góp Phát Triển (Contributing)

Mọi đóng góp nâng cấp bản dịch, sửa lỗi ngữ cảnh hoặc bổ sung mod mới đều được hoan nghênh nồng nhiệt!
Vui lòng xem hướng dẫn chi tiết tại [CONTRIBUTING.md](CONTRIBUTING.md) trước khi tạo Pull Request:
1. Đảm bảo bản dịch giữ nguyên vẹn 100% token kỹ thuật của chuỗi nguồn.
2. Chạy `python tools/validate.py data` để đảm bảo 0 lỗi vi phạm schema.
3. Chạy `python tools/check_public_files.py` để đảm bảo không commit file nhị phân vào Git.

---

<p align="center">
  <b>Thực hiện bởi Cộng Đồng Valheim Việt Nam • 2026</b><br>
  <i>"Vì một thế giới Cửu Giới Valheim trọn vẹn và đậm chất hào hùng của các chiến binh phương Bắc!"</i>
</p>
