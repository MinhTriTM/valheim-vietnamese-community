# Trạng thái QA 22/09/2026

| Hạng mục | Trạng thái | Bằng chứng / giới hạn |
| --- | --- | --- |
| Khôi phục Git và đẩy repo public | PASS | `main` theo dõi `origin/main`; các bản chụp ngoài repo bị Git bỏ qua. |
| Trích Valheim 1.0.15 | PASS | `resources.assets` SHA-256 `86b7fbe9514e43f25bee157d1cc2c103680003118e9c3872459e34e264725f9d`, 13 asset, 6.056 key, 37 ngôn ngữ, 136.412 ô có nội dung; 9 key xung đột. Dữ liệu gốc chỉ trong `local/`. |
| Ứng viên dịch game | PARTIAL | 6.038 mục `draft`: 6.021 theo MIT của monokaijs và 17 do dự án viết. Bao phủ 6.038/6.038 key English có nội dung và không xung đột. Chín key rỗng, chín key xung đột; chưa kiểm tra nghĩa từng mục. |
| Ứng viên dịch mod | PASS | Đã trích xuất và dịch 18 mod lớn nhỏ: EpicLoot (2.114), Innangard (757), CoreWoodExtras (359), SeneaL UI (358), MagicRevamp (343), ValheimArmory (286), PlanBuild (174), WeaponAdditions (80), Skyheim (77), Digitalroot.ArrowsJvL (40), QuickStackStore (29), Jotunn (21), MagicBows (20), Better Archery (11), TeleportEverything (8), DvergerStaves (7), ModSettings (4), CraftFromChestsPlus (1). Tổng số bản ghi công khai đạt 10.736 dòng JSONL hợp lệ 100%. |
| Dữ liệu website | PARTIAL | 7.440 file clone cục bộ; 1.965 JSON parse thành công; 488 đường dẫn bản clone nhỏ nằm trong bản lớn. Corpus offline có 13.003 file và 8.076 file tìm kiếm được. Chưa có quyền tái xuất bản bulk được cung cấp. |
| Dữ liệu legacy | PARTIAL | `Vietnamese.lang`: 34 key; `vi.txt`: 4.045 key, trong đó 3.980 key trùng tên nguồn game hiện tại. Tất cả nằm trong `local/` ở trạng thái `quarantine`. Đã đối chiếu và bổ sung vào các bản cài máy. |
| Rà soát tĩnh toàn bộ ứng viên game & mod | PASS | 10.736 mục qua kiểm tra token signature `tools/validate.py data` (0 lỗi). Không sai lệch placeholder hoặc ký tự đặc biệt. |
| Triển khai bản cài vào game | PASS | Công cụ `tools/deploy_translations.py` đã cập nhật thành công bản dịch tiếng Việt game (lên tới 9.438 chuỗi) và các mod tương thích vào cả 5 thư mục game cục bộ (`Valheim`, `Valheim_Mod`, `Valheim_vi_mod`, `Valheim - Copy`, `Valheim_vi`). |
| Gói preview BepInEx | PARTIAL | `local/valheim-preview-25390630.zip`: 11 file, ZIP CRC pass, gồm 6.038 key QA và loader/font từ checkout monokaijs. Chưa xác nhận chạy trên build 1.0.15. |
| Kiểm thử runtime 1.0.15 và dedicated server | NOT_RUN | Chưa cài bản `draft` vào game; dedicated server local chưa đạt target build Steam. |

## Việc cần làm để phát hành

1. Rà soát 6.038 ứng viên theo ngữ cảnh, ưu tiên 17 key mới và xác định thứ tự nạp thực tế của 9 key xung đột; cập nhật `reviewer` và `status` theo từng mục.
2. Xác định commit/version của Jotunn và ModSettings; đối chiếu nguồn hiện hành, kiểm thử mod trong game.
3. Xuất chỉ những bản `reviewed`, cài trên bản sao/test profile, kiểm tra giao diện, font, lore, placeholder và log BepInEx.
4. Chỉ công bố nội dung website theo phạm vi được chủ trang cấp quyền; giữ bản chụp hiện tại trong `local/`/thư mục Git bỏ qua.

CI chạy test, kiểm tra JSONL và chặn file clone/binary trong mỗi push hoặc pull request. [Lượt chạy trên commit `8029766`](https://github.com/MinhTriTM/valheim-vietnamese-community/actions/runs/35697282040) đã hoàn thành `success`. Chạy cùng các cổng ở máy bằng `python -m unittest discover -s tests`, `python tools/validate.py data`, `python tools/check_public_files.py`.
