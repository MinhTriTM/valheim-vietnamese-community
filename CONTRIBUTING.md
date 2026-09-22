# Đóng góp

Mỗi dòng trong `data/*.jsonl` có `namespace`, `key`, `source_sha256`, `technical_signature`, `vi`, `status`, `origin`, `game_build`, `mod_version`, `reviewer`. `source_sha256` là SHA-256 của chuỗi nguồn UTF-8; `technical_signature` là chữ ký placeholder/token dùng để phát hiện thay đổi kỹ thuật. Không commit nguyên văn chuỗi nguồn khi thiếu quyền phân phối.

Chỉ gửi bản dịch tự viết hoặc có giấy phép cho phép. Ghi rõ nguồn và giấy phép trong `origin`. Dùng `draft` cho bản chưa được kiểm chứng; `reviewed` cần tên người rà soát, đối chiếu nghĩa/ngữ cảnh và kiểm tra placeholder. Khi game/mod cập nhật, không tự đánh dấu bản dịch cũ là còn đúng. Bản dịch MIT tái sử dụng từ monokaijs có ghi công và bản sao giấy phép riêng trong `licenses/`.

Phạm vi kiểm tra: chính tả, nghĩa theo ngữ cảnh, tên riêng, markup, token `$name`, `$1`, `{0}`, xuống dòng và độ dài giao diện. Chạy `python tools/validate.py data`; công cụ sẽ chặn hash sai, token sai và mục `reviewed` thiếu người rà soát. Kiểm tra static không thay thế QA trong game.
