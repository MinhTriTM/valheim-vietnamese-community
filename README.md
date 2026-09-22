# Valheim Việt hóa cộng đồng

Kho dữ liệu và công cụ để Việt hóa Valheim, mod và nội dung tham khảo theo từng phiên bản. Repo public chỉ nhận nội dung do người đóng góp có quyền phân phối. Không commit game, DLL, bản dump nguyên văn từ game, hay bản sao website bên thứ ba.

## Trạng thái 22/09/2026

- Client local: Steam build `25390630`, tương ứng patch 1.0.15 ngày 18/09/2026.
- Dedicated server local: build `21981590`, Steam đang nhắm tới `25390671` và báo `StateFlags=6`; cần cập nhật trước QA chung.
- Bản dịch hiện có chưa đạt QA vì có chuỗi lẫn nhiều ngôn ngữ. Các bản nhập chỉ nằm trong `local/` (Git bỏ qua).
- Chưa có kiểm thử chạy game trên bản 1.0.15.

## Cấu trúc

- `data/`: bản dịch do dự án tự viết và được phép công bố; dạng JSONL, một bản ghi mỗi dòng.
- `sources/`: URL tham khảo, phiên bản và điều kiện sử dụng; không sao chép nội dung nguồn.
- `tools/`: nhập dữ liệu cục bộ và kiểm tra JSONL.
- `local/`: dữ liệu lấy từ bản game/mod cài trên máy, không xuất bản.
- `docs/INTEGRATION.md`: kết quả hợp nhất metadata của website, framework, mod và công cụ cục bộ.

## Quy trình

1. Chạy `python tools/audit_local.py` để cập nhật kiểm kê tại `local/source_inventory.json`.
2. Chạy `python tools/import_local.py --source <keys_en.json> --target <all_translations.json> --namespace valheim --build 25390630`. File nhập mặc định là `local/valheim.jsonl`; có thể dùng `--output local/imported.jsonl` cho tên cũ. Với mod chưa có bản dịch, bỏ `--target` và đặt namespace riêng. File JSON đầu vào phải hợp lệ; các pack cũ có cú pháp hỏng cần sửa riêng trước khi nhập.
3. Rà soát từng dòng: đối chiếu key, ngữ cảnh trong game, placeholder, quyền phân phối và trạng thái dịch.
4. Chỉ chép bản ghi đã rà soát và được phép công bố vào `data/`, đặt `status` là `reviewed`.
5. Chạy `python tools/validate.py data`. Sau đó kiểm tra trong game và ghi phiên bản tương thích.

Mod dùng namespace riêng, ví dụ `epicloot`; ghi tên mod, phiên bản, giấy phép/nguồn và đường dẫn dữ liệu trong `origin`. Khi nguồn đổi, chỉ tái sử dụng bản dịch nếu cùng key, `source_sha256` và `technical_signature`.

## Đóng góp

Xem [CONTRIBUTING.md](CONTRIBUTING.md). Mỗi PR nên kèm nguồn gốc, phiên bản game/mod, ảnh chụp ngữ cảnh khi cần và kết quả QA. Không gửi file game hoặc các chuỗi nguồn/bản dịch của bên thứ ba khi chưa có quyền.

## Website tham khảo

`valheimcheats.com` được ghi trong `sources/valheimcheats.json` dưới dạng liên kết và danh mục chủ đề. Điều khoản trang cấm tái xuất bản hàng loạt nội dung gốc; việc clone toàn bộ chỉ thực hiện sau khi được chủ trang cấp quyền rõ ràng.
