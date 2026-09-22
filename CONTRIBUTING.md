# Đóng góp

Mỗi dòng trong `data/*.jsonl` có `namespace`, `key`, `source_sha256`, `technical_signature`, `vi`, `status`, `origin`, `game_build`, `mod_version`, `reviewer`. `source_sha256` là SHA-256 của chuỗi nguồn UTF-8; `technical_signature` là chữ ký placeholder/token dùng để phát hiện thay đổi kỹ thuật. Không commit nguyên văn chuỗi nguồn khi thiếu quyền phân phối.

Chỉ gửi bản dịch tự viết hoặc có giấy phép cho phép. Ghi rõ nguồn và giấy phép trong `origin`. Dùng `draft` cho bản chưa được kiểm chứng; `reviewed` cần người rà soát và kiểm tra placeholder. Khi game/mod cập nhật, không tự đánh dấu bản dịch cũ là còn đúng.

Phạm vi kiểm tra: chính tả, nghĩa theo ngữ cảnh, tên riêng, markup, token `$name`, `{0}`, xuống dòng và độ dài giao diện. Kiểm tra static không thay thế QA trong game.

