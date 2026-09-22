# Hợp nhất nguồn dữ liệu cục bộ

## Kết quả kiểm kê 22/09/2026

Thư mục dự án từng mất `.git` và `.gitignore` sau khi thêm các bản chụp. Đã kết nối lại `origin/main` mà không ghi đè file làm việc. Các thư mục nguồn vẫn nằm nguyên vị trí nhưng bị Git bỏ qua. Danh sách và chính sách công bố nằm tại [`sources/local_sources.json`](../sources/local_sources.json).

| Nhóm | Dữ liệu hiện có | Cách dùng |
| --- | --- | --- |
| Game | `local/imported.jsonl`: 8.164 key cũ `quarantine`; `local/game_sources.jsonl`: 6.056 key từ bản 1.0.15 | Nguồn hiện hành và 37 ngôn ngữ nằm trong `local/`; 6.038 ứng viên ở `data/valheim` đều là `draft`. |
| Website | `valheimcheats.com`: 7.440 file; `valheimcheats_clone`: 488 HTML; thêm ZIP 58,9 MB | Chỉ dùng cục bộ để tra cứu. 488 đường dẫn bản clone nhỏ đều có trong bản lớn; chưa so hash nội dung và chưa chứng minh clone đầy đủ. |
| Framework/mod | Jotunn, ValheimLib, ModSettings, các example/stub và tool khác | Dùng để tìm schema/key và viết adapter; giữ giấy phép, phiên bản và provenance riêng cho từng dự án. |
| Công cụ | AssetRipper, CommonPackages | Dùng cục bộ; dữ liệu `AssetRipper/Localizations` dịch giao diện công cụ, không phải Valheim. |

## Cổng nhập dữ liệu

Chạy `python tools/build_local_corpus.py` để lập `local/corpus.sqlite3` từ các bản chụp; tìm file bằng `python tools/search_local.py 'từ khóa'`. Corpus gồm metadata mọi file và văn bản có thể tìm kiếm từ HTML, JSON, mã nguồn và tài liệu. Nó chỉ dùng offline và bị Git bỏ qua.

Với JSON website đã có trên máy, chạy `python tools/normalize_site_local.py` để tạo `local/site_entities.jsonl`. Hiện 1.965 JSON parse thành công, gồm cả dữ kiện và lời giải thích gốc của website; file này không được công bố. Chỉ đưa dữ kiện vào repo public sau khi xác minh độc lập với game và xem xét quyền phân phối.

1. Xác định nguồn gốc chính xác của từng file: URL, phiên bản/commit, giấy phép, game/mod build.
2. Tách dữ liệu theo `namespace` (`valheim`, `jotunn`, tên mod cụ thể). Không gộp chỉ vì key trùng tên.
3. Đối chiếu `key + source_sha256 + technical_signature`. Key đổi nguồn hoặc token phải quay lại `draft`/rà soát; key biến mất được ghi là retired trong nhật ký cập nhật.
4. Kiểm tra bản dịch bằng `tools/validate.py`, sau đó kiểm tra ngữ cảnh trong game. Chỉ công bố bản dịch do người đóng góp có quyền phân phối.
5. Với website, tạo các mục tham chiếu gồm URL, chủ đề và nguồn gốc; không sao chép hàng loạt trang, ảnh, JS, lời giải thích hoặc bản tuyển chọn vào repo public khi chưa có quyền riêng.

## Việc còn lại

- Chưa xác định commit gốc của các source snapshot; chúng không có `.git`.
- Đã có ứng viên `draft` công khai, nhưng chưa có bản ghi `reviewed`, adapter runtime cho mọi mod hay kiểm thử Valheim 1.0.15. Xem [STATUS.md](STATUS.md).
- Script `clone_12_threads.py` là bản chụp cục bộ, có đường dẫn hardcode và không kiểm chứng đủ file; không dùng làm bằng chứng clone hoàn chỉnh.
- Dữ liệu trang có điều khoản riêng tại <https://valheimcheats.com/terms>; cần quyền rõ ràng nếu muốn tái xuất bản toàn bộ.
