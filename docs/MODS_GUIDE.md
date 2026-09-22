# Cẩm nang và Trạng thái 74 Mod Valheim (22/09/2026)

Tài liệu này tổng hợp toàn bộ 74 mod được lưu trữ trong thư mục `mods/` của dự án, phân loại theo cơ chế ngôn ngữ và cung cấp thông tin chi tiết về từng mod.

---

## 1. Nhóm Mod Đã Được Tách Chuỗi & Việt Hóa Toàn Diện (18 Mod)

Các mod này có hệ thống bản ngữ riêng (JSON, YAML, TXT, hoặc Embedded Manifest Resources trong DLL), đã được trích xuất dữ liệu gốc, biên dịch sang tiếng Việt và lưu trữ tại `data/mods/*.jsonl` (đáp ứng 100% token signature):

| STT | Tên Mod | Thư mục mod | Số Key | Tính năng chính |
|---|---|---|---|---|
| 1 | **EpicLoot** (v0.14.11) | `EpicLoot-0.14.11.zip...` | 2.114 | Hệ thống trang bị ma thuật, độ hiếm (Magic/Rare/Epic/Legendary), nhiệm vụ săn tiền thưởng, phù phép và đá khảm. |
| 2 | **Innangard** (v0.1.9) | `Innangard 3607...` | 757 | Hệ thống định cư, chiêu mộ dân làng Viking, xây dựng làng xóm và công trình tự động. |
| 3 | **CoreWoodExtras** (v2.2.6) | `CoreWoodExtras V2.2.6...` | 359 | Bổ sung hơn 50 khối kiến trúc, quầy chợ, thùng cá và đồ nội thất gỗ lõi. |
| 4 | **SeneaL UI** (v1.1.3) | `SeneaL UI 1.1.3...` | 358 | Nâng cấp giao diện hiển thị: thanh máu chi tiết, sát thương, hiệu ứng trạng thái kẻ thù. |
| 5 | **MagicRevamp** (v1.5.1) | `MagicRevamp 2743...` | 343 | Mở rộng hệ thống ma thuật, thêm các bộ trang phục và gậy phép nguyên tố. |
| 6 | **ValheimArmory** (v1.33.0) | `ValheimArmory 1455...` | 286 | Kho vũ khí đồ sộ: nỏ, đại kiếm, giáo hắc kim, khiên và giáp chiến binh. |
| 7 | **PlanBuild** (v0.19.1) | `PlanBuild 1125...` | 174 | Công cụ lập bản thiết kế kiến trúc (blueprint), dựng khung kế hoạch xây dựng trước khi tốn nguyên liệu. |
| 8 | **WeaponAdditions** (v1.2.6) | `WeaponAdditions 2536...` | 80 | Bổ sung hàng loạt vũ khí đặc trưng: vũ khí hỏa kim, rồng, hắc diện thạch, tộc tiên. |
| 9 | **Skyheim** / **SkyheimFix** (v1.3.12) | `Skyheim-916...` | 77 | Hệ thống ma thuật cổ tự (runes), kỹ năng phép thuật phong cách Skyrim. |
| 10 | **Digitalroot.ArrowsJvL** (v1.0.0) | `Digitalroot.ArrowsJvL...` | 40 | Bổ sung các loại tên nặng và đầu tù xuyên giáp, làm choáng mục tiêu từ xa. |
| 11 | **Quick Stack - Store - Sort - Trash** (v1.4.15) | `Quick Stack - Store...` | 29 | Xếp nhanh đồ vào rương xung quanh, sắp xếp túi đồ thông minh, nút bổ sung vật phẩm. |
| 12 | **Jotunn** | `Jotunn` | 21 | Framework nền tảng số 1 hỗ trợ tạo mod, nạp item, piece và localization cho Valheim. |
| 13 | **MagicBows** (v1.1.9) | `MagicBows 2346...` | 20 | Bộ cung và nỏ ma thuật nguyên tố (Lửa, Băng, Sấm Sét, Linh Hồn, Độc Tố). |
| 14 | **Better Archery** (v2.0.2) | `Better Archery 348...` | 11 | Ống đựng tên (quiver), nhặt lại mũi tên, cơ chế ngắm bắn và kéo cung cải tiến. |
| 15 | **TeleportEverything** (v2.9.1) | `TeleportEverything-1806...` | 8 | Dịch chuyển động vật thuần hóa, đồng minh và quặng qua cổng (kèm phí cấu hình). |
| 16 | **DvergerStaves** (v1.1.0) | `DvergerStaves 2670...` | 7 | Bộ gậy phép của người lùn Dverger (Lửa, Trị Thương, Băng Giá). |
| 17 | **ModSettings** | `ModSettings` | 4 | Giao diện cấu hình cài đặt mod trực tiếp trong menu game. |
| 18 | **CraftFromChestsPlus** (v1.0.5) | `CraftFromChestsPlus...` | 1 | Chế tạo trang bị và công trình trực tiếp sử dụng nguyên liệu từ các rương lân cận. |

---

## 2. Nhóm Mod Tiện Ích Gameplay & Cấu Hình BepInEx (56 Mod)

Các mod này can thiệp trực tiếp vào mã nguồn game (IL / Harmony Patches), sử dụng trực tiếp các từ khóa ngôn ngữ gốc của game (`$item_...`, `$piece_...`) hoặc cấu hình qua tệp `BepInEx/config/*.cfg`:

1. **AchievementEnabler** / **DarkmoonBlade's Valheim Achievements Enabler** / **KeepAchivements**: Mở lại hệ thống thành tựu Steam khi chạy kèm mod.
2. **AutoMapPins**: Tự động đánh dấu tài nguyên trên bản đồ khi người chơi phát hiện.
3. **Autosmelter**: Tự động hút quặng và than vào lò nấu kim loại khi đứng gần rương.
4. **BadgersSkiesFix**: Sửa lỗi hiển thị bầu trời và ánh sáng mây.
5. **BeastMaster**: Mở rộng khả năng thuần hóa và cưỡi nhiều loài sinh vật.
6. **BetterUI**: Nâng cấp thanh hiển thị thông số nhân vật và độ bền trang bị.
7. **BoundaryLoadStaggerer**: Giảm giật lag khi chuyển đổi giữa các vùng bản đồ bằng cách tải so le ranh giới.
8. **Cartur's Map Pins**: Bổ sung nhiều biểu tượng đánh dấu bản đồ sinh động.
9. **Cartur's Safe Stamina**: Không bị tiêu hao thể lực vô ích khi làm việc trong vùng an toàn (nhà/bảo hộ).
10. **Chest Label**: Gắn nhãn tên chữ lên mặt trước rương chứa đồ.
11. **Comic GI**: Preset đồ họa phong cách cel-shading truyện tranh.
12. **CraftingStorageLink**: Liên kết túi đồ chế tạo với các kho chứa.
13. **Death Tweaks**: Tùy chỉnh những gì bị rơi khi nhân vật ngã xuống (giữ trang bị, giữ kỹ năng).
14. **Denikson BepInExPack Valheim**: Bộ cài đặt BepInEx 5.4 nền tảng chạy mod.
15. **Digitalroot.HeightmapUnlimitedJvL**: Bỏ giới hạn độ cao/độ sâu khi san lấp địa hình đất.
16. **EasyLiving**: Tự động hóa các tác vụ lặp đi lặp lại hàng ngày trong căn cứ.
17. **EndosCryptKeySlotMod**: Khe cắm chìa khóa hầm mộ riêng biệt.
18. **Fast Repair Button**: Sửa nhanh toàn bộ trang bị chỉ với một cú nhấp chuột.
19. **ForgeOfCertainty**: Đảm bảo tỉ lệ thành công và tối ưu hóa lò rèn.
20. **HoldAttack**: Nhấn giữ chuột để tấn công liên tục thay vì phải bấm liên tục.
21. **Instant Monster Drop**: Quái vật rơi đồ ngay lập tức khi chết, không cần đợi khói tan.
22. **JsonDotNet**: Thư viện JSON nền tảng phục vụ các mod khác.
23. **KingsTweaks**: Tổng hợp các tùy chỉnh tiện ích chất lượng cuộc sống (QoL).
24. **Loot Multiplier**: Nhân số lượng vật phẩm rơi ra theo tỉ lệ thiết lập.
25. **mtnewton-ItemStacks**: Tăng kích thước cộng dồn (stack size) của vật phẩm.
26. **Oathbound**: Hệ thống lời thề và phần thưởng chiến binh cổ xưa.
27. **OpenKeep**: Mở rộng tương tác với các rương chứa và kho đồ.
28. **Performance Booster**: Tối ưu hóa hiệu năng render và xử lý CPU/GPU.
29. **Plant Easily**: Trồng cây theo hàng lối nhanh chóng và đồng đều.
30. **Plant Everything**: Cho phép trồng tất cả các loài cây, bụi dâu, nấm và hoa trong thiên nhiên.
31. **Quartermaster**: Quản lý kho hàng và trạm tiếp tế quân trang.
32. **QuickStack**: Bản xếp nhanh gọn nhẹ cổ điển.
33. **Regen And No Skill Loss** / **Regen No Skill Loss Achievements Enabled**: Hồi phục thể lực nhanh hơn và không bị giảm cấp kỹ năng khi chết.
34. **Swap Weapons On The Run**: Cho phép đổi vũ khí mượt mà ngay cả khi đang chạy nước rút.
35. **TamedHpRegen**: Thú nuôi đã thuần hóa tự động hồi máu nhanh theo thời gian.
36. **Terrain Loading Priority Fix**: Tối ưu thứ tự nạp dữ liệu địa hình, chống hẫng map.
37. **Tools in Water**: Cho phép sử dụng búa, rìu, vũ khí bình thường ngay cả khi đang bơi dưới nước.
38. **Unbound**: Giải phóng các giới hạn ràng buộc của engine.
39. **Unrestricted Portals**: Cho phép mang kim loại và quặng thô qua cổng dịch chuyển.
40. **VBNetTweaks**: Tinh chỉnh mã mạng và đồng bộ máy chủ nhiều người chơi.
41. **Valhalla ReShade HD**: Bộ lọc màu đồ họa rực rỡ sắc nét.
42. **Valheim Extension**: Trình mở rộng chức năng hệ thống BepInEx.
43. **Valheim Legends**: Bổ sung các lớp nhân vật (Class/Mage/Ranger/Druid...) với kỹ năng độc đáo.
44. **ValheimCommunityPatch**: Bản vá cộng đồng sửa các lỗi nhỏ của game gốc.
45. **ValheimPlus**: Đại tu toàn diện cài đặt cơ chế trò chơi (xây dựng, túi đồ, thời gian, sản xuất).
46. **ValheimWaterproofBrush**: Quét lớp chống nước bảo vệ các khối gỗ khỏi bị mục rữa do mưa.
47. **VeinMining**: Đập một phát vỡ toàn bộ mạch quặng lớn.
48. **YamlDotNet**: Thư viện phân tích cú pháp YAML cho BepInEx.
49. **unstripped_managed**: Bộ DLL tham chiếu phục vụ lập trình và dịch ngược mod.

---

## 3. Cách Triển Khai Vào Game

Chạy một lệnh duy nhất:
```bash
python tools/deploy_translations.py
```
Toàn bộ bản dịch tiếng Việt của Game và tất cả các mod trên sẽ được cài đặt tức thì vào các thư mục game trên máy người dùng.
