# Bản dịch mod

`jotunn_vi.json` và `modsettings_vi.json` là bản dịch do dự án viết từ snapshot nguồn English tương ứng; các file `*_draft.jsonl` thêm hash nguồn, chữ ký token và trạng thái. Snapshot không có commit/version gốc nên toàn bộ còn là `draft`, chưa được kiểm thử trong game.

Có thể tạo bản QA cục bộ bằng `python tools/build_translation.py --namespace jotunn --source-json Jotunn/JotunnLib/Localization/English.json --preview` hoặc lệnh tương tự với ModSettings. Khi đã đối chiếu nguồn và chạy game, người rà soát cập nhật từng bản ghi thành `reviewed` kèm tên; bản xuất mặc định chỉ lấy các bản ghi đó.
