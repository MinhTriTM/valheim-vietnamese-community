# Hợp nhất nguồn dữ liệu phiên bản game mới nhất

## Kết quả kiểm kê 22/09/2026

Dự án đã thanh lọc toàn bộ các bản chụp website và công cụ dịch ngược bên ngoài không cần thiết. Hiện tại, **trích dẫn duy nhất được duy trì và theo dõi là phiên bản game Valheim mới nhất**:

- **Bản Client Game Mới Nhất:** Steam build `25390630`, tương ứng Patch **1.0.15** chính thức (18/09/2026).
- **Metadata chính thức:** Được lưu trữ tại [`sources/game_build_25390630.json`](../sources/game_build_25390630.json) với chữ ký SHA-256 nguyên bản từ `resources.assets`.
- **Dữ liệu trích xuất chuẩn:** Gồm 6.056 key và 37 ngôn ngữ song song phục vụ đối soát.

| Nhóm | Dữ liệu nguồn | Cách dùng |
| --- | --- | --- |
| **Game Patch 1.0.15** | `local/game_sources.jsonl`: 6.056 key gốc từ bản 1.0.15 | Nguồn chân lý đối chiếu; toàn bộ bản dịch `data/valheim` đối soát 1:1 với bản này. |
| **Kho 74 Mod** | `mods/`: 74 thư mục mod cục bộ trên máy | Trích xuất tài nguyên ngôn ngữ qua Reflection và triển khai trực tiếp vào `Valheim_Mod`. |
| **Bộ nạp BepInEx** | Mã nguồn sạch C# `ValheimVietnamese` | Nạp ngôn ngữ Tiếng Việt trực tiếp vào menu game của phiên bản 1.0.15. |

## Nguyên tắc đối soát

1. **Chân lý duy nhất từ bản 1.0.15:** Mọi key dịch thuật bắt buộc phải đối chiếu với bộ chuỗi trích xuất từ Steam build `25390630`.
2. **Không phụ thuộc website bên ngoài:** Không sử dụng dữ liệu clone hay crawl website thứ ba; mọi thuật ngữ game bám sát bản dịch chuẩn gốc của game và văn hóa Viking.
3. **Bảo toàn Token:** Áp dụng thuật toán chữ ký SHA-256 kiểm soát token, không cho phép sai lệch placeholder.
