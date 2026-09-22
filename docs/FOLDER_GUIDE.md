# Giải thích cấu trúc `valheim-vietnamese-community`

Tài liệu này mô tả các thành phần cốt lõi của kho dự án **Valheim Việt Hóa Cộng Đồng** (cập nhật ngày 22/09/2026). Dự án tập trung duy nhất vào việc bản địa hóa chuẩn mực cho **Phiên bản Game Valheim mới nhất (Patch 1.0.15 / Steam Build `25390630`)** và hệ sinh thái các bản mod đi kèm.

---

## 1. Thành phần Cốt Lõi của Dự Án

| Thư mục / Tệp tin | Nội dung và vai trò thực tế | Trạng thái trên GitHub |
| --- | --- | --- |
| [`data/`](../data/README.md) | Kho dữ liệu JSONL chuẩn hóa gồm **10.736 bản ghi**: Game gốc (6.038 key) và 18 bản mod lớn (4.698 key). Đảm bảo 100% chữ ký token signature. | Có (Public). |
| [`sources/`](../sources/local_sources.json) | Metadata chính thức của bản game mục tiêu: [`sources/game_build_25390630.json`](../sources/game_build_25390630.json) và danh mục nguồn cục bộ hợp lệ. | Có (Public). |
| [`docs/`](STATUS.md) | Tài liệu kỹ thuật, cẩm nang 74 mod ([MODS_GUIDE.md](MODS_GUIDE.md)), trạng thái kiểm định QA ([STATUS.md](STATUS.md)) và hợp nhất dữ liệu ([INTEGRATION.md](INTEGRATION.md)). | Có (Public). |
| `tools/` | Bộ kịch bản dòng lệnh CLI tự động hóa trích xuất, thẩm định token (`validate.py`), kiểm tra an toàn repo (`check_public_files.py`) và triển khai 1-click vào game (`deploy_translations.py`). | Có (Public). |
| `tests/` | Bộ kiểm thử đơn vị tự động (Unit Tests) xác thực thuật toán chữ ký token và quy chuẩn schema bắt buộc. | Có (Public). |
| `.github/` | Cấu hình GitHub Actions CI chạy tự động kiểm tra cú pháp và tính toàn vẹn mỗi khi có commit/pull request. | Có (Public). |
| `licenses/` | Giấy phép ghi nhận công sức bản dịch gốc của monokaijs theo chuẩn MIT License. | Có (Public). |
| `local/` | Vùng làm việc nội bộ trên máy cá nhân: chuỗi trích xuất nguyên bản từ `resources.assets`, tài nguyên Manifest Resource từ 74 DLL mod, cơ sở dữ liệu đối soát. | **Không** (Bị `.gitignore` loại trừ). |
| `mods/` | Kho lưu trữ 74 thư mục mod cục bộ làm nguyên liệu trích xuất và đóng gói. | **Không** (Bị `.gitignore` loại trừ). |
| `Lich_Su_Truy_Van/` | Nhật ký truy vấn và bối cảnh hoạt động của Agent trên máy cá nhân. | **Không** (Bị `.gitignore` loại trừ). |

---

## 2. Các Tệp Quản Trị ở Thư Mục Gốc

| Tệp tin | Vai trò | Trạng thái trên GitHub |
| --- | --- | --- |
| [`README.md`](../README.md) | Trang giới thiệu tổng quan dự án, bảng chỉ số, phân tích 18 mod và hướng dẫn sử dụng. | Có (Public). |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md) | Quy chuẩn đóng góp, nguyên tắc giữ nguyên token placeholder và quy trình rà soát. | Có (Public). |
| [`LICENSE`](../LICENSE) | Giấy phép mã nguồn mở MIT bảo vệ quyền lợi của cộng đồng. | Có (Public). |
| [`.gitignore`](../.gitignore) | Thiết lập loại trừ nghiêm ngặt các thư mục nhạy cảm, bản chụp cũ, file nhị phân (DLL, ZIP, EXE). | Có (Public). |

---

## 3. Quy Tắc Trích Dẫn Duy Nhất

Dự án tuân thủ nguyên tắc: **Chỉ tồn tại duy nhất trích dẫn của phiên bản game mới nhất** (Steam Build `25390630` / Patch 1.0.15). Toàn bộ các công cụ dịch ngược bên thứ ba, crawler tải trang web và các bản sao website không chính thức đều bị loại bỏ hoàn toàn khỏi kiến trúc và tài liệu của dự án.
