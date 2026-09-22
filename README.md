# Valheim Việt hóa cộng đồng

Kho dữ liệu và công cụ để Việt hóa Valheim, mod và nội dung tham khảo theo từng phiên bản. Repo public chỉ nhận nội dung do người đóng góp có quyền phân phối hoặc có giấy phép rõ ràng. Không commit game, DLL, bản dump nguyên văn từ game, hay bản sao website bên thứ ba.

## Trạng thái 22/09/2026

- Client local: Steam build `25390630`, tương ứng patch 1.0.15 ngày 18/09/2026. Đã trích 13 asset localization, 6.056 key và 37 ngôn ngữ từ `resources.assets`; dữ liệu gốc chỉ nằm trong `local/`.
- Dedicated server local: build `21981590`, Steam đang nhắm tới `25390671` và báo `StateFlags=6`; cần cập nhật trước QA chung.
- Có 6.038 ứng viên dịch game (6.021 từ bản dịch MIT của monokaijs, 17 do dự án viết), 25 ứng viên Jotunn/ModSettings và 9 ứng viên cho mod ví dụ. Bản game bao phủ toàn bộ key English có nội dung và không xung đột của bản trích hiện tại; tất cả vẫn là `draft`, chưa phải bản phát hành.
- Bản dịch cũ trên máy có chuỗi lẫn nhiều ngôn ngữ; bản nhập cũ chỉ nằm trong `local/` (Git bỏ qua).
- Chưa có kiểm thử chạy game trên bản 1.0.15.

## Cấu trúc

- `data/`: ứng viên dịch do dự án tự viết hoặc theo giấy phép MIT có ghi công; dạng JSONL, một bản ghi mỗi dòng. Chỉ `reviewed` mới được xuất thành bản cài mặc định.
- `sources/`: URL tham khảo, phiên bản và điều kiện sử dụng; không sao chép nội dung nguồn.
- `tools/`: nhập dữ liệu cục bộ và kiểm tra JSONL.
- `local/`: dữ liệu lấy từ bản game/mod cài trên máy, không xuất bản.
- `docs/INTEGRATION.md`: kết quả hợp nhất metadata của website, framework, mod và công cụ cục bộ.

## Quy trình

1. Chạy `python tools/audit_local.py` để cập nhật kiểm kê tại `local/source_inventory.json`.
   Muốn tra cứu tất cả bản chụp trên máy, chạy `python tools/build_local_corpus.py`, rồi `python tools/search_local.py 'từ khóa'`. Cơ sở dữ liệu `local/corpus.sqlite3` không được công bố.
2. Chạy `python tools/extract_game.py --resources <đường dẫn resources.assets> --build 25390630` để trích nguồn English và 37 ngôn ngữ vào `local/`. Hash và số lượng trong [`sources/game_build_25390630.json`](sources/game_build_25390630.json).
3. Với bản cũ, chạy `python tools/import_local.py --source <keys_en.json> --target <all_translations.json> --namespace valheim --build 25390630`. File nhập mặc định là `local/valheim.jsonl`; có thể dùng `--output local/imported.jsonl` cho tên cũ. Với mod chưa có bản dịch, bỏ `--target` và đặt namespace riêng.
4. Rà soát từng dòng: đối chiếu key, ngữ cảnh trong game, placeholder, quyền phân phối và trạng thái dịch. Các ứng viên game nằm trong [`data/valheim`](data/valheim/PROVENANCE.md); ứng viên mod nằm trong [`data/mods`](data/mods/README.md).
5. Chạy `python tools/validate.py data`. Dùng `python tools/build_translation.py --namespace valheim --source-catalog local/game_sources.jsonl --preview` để tạo bản QA cục bộ. Bỏ `--preview` khi chỉ xuất những mục `reviewed` còn khớp nguồn; sau đó kiểm tra trong game.
   Có thể tạo gói QA BepInEx cục bộ bằng `python tools/package_preview.py --upstream <checkout monokaijs/valheim-viet-hoa>`; gói nằm trong `local/` và không sửa bản cài Valheim.

Mod dùng namespace riêng, ví dụ `epicloot`; ghi tên mod, phiên bản, giấy phép/nguồn và đường dẫn dữ liệu trong `origin`. Khi nguồn đổi, chỉ tái sử dụng bản dịch nếu cùng key, `source_sha256` và `technical_signature`.

## Đóng góp

Xem [CONTRIBUTING.md](CONTRIBUTING.md). Mỗi PR nên kèm nguồn gốc, phiên bản game/mod, ảnh chụp ngữ cảnh khi cần và kết quả QA. Không gửi file game hoặc các chuỗi nguồn/bản dịch của bên thứ ba khi chưa có quyền.

## Website tham khảo

`valheimcheats.com` được ghi trong `sources/valheimcheats.json` dưới dạng liên kết và danh mục chủ đề. Bản chụp cục bộ đã được lập chỉ mục: 1.965 JSON hợp lệ có thể tra cứu trong `local/`. Điều khoản trang cấm tái xuất bản hàng loạt nội dung gốc; việc đăng toàn bộ lên repo chỉ thực hiện sau khi được chủ trang cấp quyền rõ ràng.

Xem [trạng thái QA](docs/STATUS.md) để biết ranh giới giữa dữ liệu đã trích, bản dịch nháp và bản phát hành.
Xem [giải thích từng thư mục và file](docs/FOLDER_GUIDE.md) để phân biệt nguồn cục bộ với nội dung repo công khai.
Mỗi pull request được CI kiểm tra cú pháp, test, schema/token và danh sách file công khai; bản clone và dữ liệu cục bộ vẫn bị chặn.
