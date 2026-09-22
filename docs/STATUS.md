# Trạng thái QA 22/09/2026

| Hạng mục | Trạng thái | Bằng chứng / giới hạn |
| --- | --- | --- |
| Khôi phục Git và đẩy repo public | PASS | `main` theo dõi `origin/main`; các bản chụp ngoài repo bị Git bỏ qua. |
| Trích Valheim 1.0.15 | PASS | `resources.assets` SHA-256 `86b7fbe9514e43f25bee157d1cc2c103680003118e9c3872459e34e264725f9d`, 13 asset, 6.056 key, 37 ngôn ngữ, 136.412 ô có nội dung; 9 key xung đột. Dữ liệu gốc chỉ trong `local/`. |
| Ứng viên dịch game | PARTIAL | 6.038 mục `draft`: 6.021 theo MIT của monokaijs và 17 do dự án viết. Bao phủ 6.038/6.038 key English có nội dung và không xung đột. Chín key rỗng, chín key xung đột; chưa kiểm tra nghĩa từng mục. |
| Ứng viên dịch mod | PARTIAL | 21 Jotunn, 4 ModSettings và 9 key JotunnModExample do dự án viết; nguồn snapshot chưa rõ commit/version nên vẫn là `draft`. ExampleMod chỉ là ví dụ, không phải gói mod chạy thực tế. |
| Dữ liệu website | PARTIAL | 7.440 file clone cục bộ; 1.965 JSON parse thành công; 488 đường dẫn bản clone nhỏ nằm trong bản lớn. Corpus offline có 13.003 file và 8.076 file tìm kiếm được. Chưa có quyền tái xuất bản bulk được cung cấp. |
| Dữ liệu legacy | PARTIAL | `Vietnamese.lang`: 34 key; `vi.txt`: 4.045 key, trong đó 3.980 key trùng tên nguồn game hiện tại. Tất cả nằm trong `local/` ở trạng thái `quarantine`, chưa có hash nguồn/giấy phép đủ để nhập công khai. |
| Rà soát tĩnh toàn bộ ứng viên game | PASS | 6.038 mục qua kiểm tra token. Quét ưu tiên đánh dấu 16 mục giữ nguyên English; đã xem từng mục, đều là tên riêng, tên ngôn ngữ hoặc câu hát. Đây không phải kiểm tra nghĩa toàn bộ. |
| Xuất bản cài game | BLOCKED | Cổng xuất mặc định từ chối vì không có mục `reviewed`. Bản `--preview` chỉ dành cho QA cục bộ. |
| Kiểm thử runtime 1.0.15 và dedicated server | NOT_RUN | Chưa cài bản `draft` vào game; dedicated server local chưa đạt target build Steam. |

## Việc cần làm để phát hành

1. Rà soát 6.038 ứng viên theo ngữ cảnh, ưu tiên 17 key mới và xác định thứ tự nạp thực tế của 9 key xung đột; cập nhật `reviewer` và `status` theo từng mục.
2. Xác định commit/version của Jotunn và ModSettings; đối chiếu nguồn hiện hành, kiểm thử mod trong game.
3. Xuất chỉ những bản `reviewed`, cài trên bản sao/test profile, kiểm tra giao diện, font, lore, placeholder và log BepInEx.
4. Chỉ công bố nội dung website theo phạm vi được chủ trang cấp quyền; giữ bản chụp hiện tại trong `local/`/thư mục Git bỏ qua.

CI chạy test, kiểm tra JSONL và chặn file clone/binary trong mỗi push hoặc pull request. [Lượt chạy trên commit `8029766`](https://github.com/MinhTriTM/valheim-vietnamese-community/actions/runs/35697282040) đã hoàn thành `success`. Chạy cùng các cổng ở máy bằng `python -m unittest discover -s tests`, `python tools/validate.py data`, `python tools/check_public_files.py`.
