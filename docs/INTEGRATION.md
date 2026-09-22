# Hợp nhất nguồn dữ liệu cục bộ

## Kết quả kiểm kê 22/09/2026

Thư mục dự án từng mất `.git` và `.gitignore` sau khi thêm các bản chụp. Đã kết nối lại `origin/main` mà không ghi đè file làm việc. Các thư mục nguồn vẫn nằm nguyên vị trí nhưng bị Git bỏ qua. Danh sách và chính sách công bố nằm tại [`sources/local_sources.json`](../sources/local_sources.json).

| Nhóm | Dữ liệu hiện có | Cách dùng |
| --- | --- | --- |
| Game | `local/imported.jsonl`: 8.164 key; toàn bộ `quarantine` | Rà soát nguồn, bản dịch, token và build trước khi đưa vào `data/`. |
| Website | `valheimcheats.com`: 7.440 file; `valheimcheats_clone`: 488 HTML; thêm ZIP 58,9 MB | Chỉ dùng cục bộ để tra cứu. 488 đường dẫn bản clone nhỏ đều có trong bản lớn; chưa so hash nội dung và chưa chứng minh clone đầy đủ. |
| Framework/mod | Jotunn, ValheimLib, ModSettings, các example/stub và tool khác | Dùng để tìm schema/key và viết adapter; giữ giấy phép, phiên bản và provenance riêng cho từng dự án. |
| Công cụ | AssetRipper, CommonPackages | Dùng cục bộ; dữ liệu `AssetRipper/Localizations` dịch giao diện công cụ, không phải Valheim. |

## Cổng nhập dữ liệu

1. Xác định nguồn gốc chính xác của từng file: URL, phiên bản/commit, giấy phép, game/mod build.
2. Tách dữ liệu theo `namespace` (`valheim`, `jotunn`, tên mod cụ thể). Không gộp chỉ vì key trùng tên.
3. Đối chiếu `key + source_sha256 + technical_signature`. Key đổi nguồn hoặc token phải quay lại `draft`/rà soát; key biến mất được ghi là retired trong nhật ký cập nhật.
4. Kiểm tra bản dịch bằng `tools/validate.py`, sau đó kiểm tra ngữ cảnh trong game. Chỉ công bố bản dịch do người đóng góp có quyền phân phối.
5. Với website, tạo các mục tham chiếu gồm URL, chủ đề và nguồn gốc; không sao chép hàng loạt trang, ảnh, JS, lời giải thích hoặc bản tuyển chọn vào repo public khi chưa có quyền riêng.

## Việc còn lại

- Chưa xác định commit gốc của các source snapshot; chúng không có `.git`.
- Chưa có bản dịch công khai được rà soát, adapter cho mod cụ thể, hay kiểm thử runtime Valheim 1.0.15.
- Script `clone_12_threads.py` là bản chụp cục bộ, có đường dẫn hardcode và không kiểm chứng đủ file; không dùng làm bằng chứng clone hoàn chỉnh.
- Dữ liệu trang có điều khoản riêng tại <https://valheimcheats.com/terms>; cần quyền rõ ràng nếu muốn tái xuất bản toàn bộ.
