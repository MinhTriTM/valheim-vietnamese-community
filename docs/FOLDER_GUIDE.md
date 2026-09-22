# Giải thích cấu trúc `valheim-vietnamese-community`

Tài liệu này mô tả các mục đang có trong thư mục dự án tại `E:\SteamLibrary\steamapps\common\valheim-vietnamese-community` (kiểm tra ngày 22/09/2026).

**Hai trạng thái cần phân biệt:** “Có trên máy” không có nghĩa “đã đưa lên GitHub”. Các bản chụp website, mã nguồn bên thứ ba và dữ liệu đang rà soát được [.gitignore](../.gitignore) bỏ qua. Repo public chứa bản dịch nháp có nguồn gốc/giấy phép, metadata, tài liệu và công cụ của dự án.

## 1. Bản chụp website và công cụ tải

| Mục | Là gì / dùng để làm gì | GitHub |
| --- | --- | --- |
| `valheimcheats.com/` | Bản chụp lớn của website tham khảo Valheim: 7.440 file, gồm HTML, JSON, ảnh WebP và JavaScript. Dùng để tra cứu offline; 1.965 file JSON đã được chuẩn hóa vào `local/site_entities.jsonl`. | Không; chỉ ở máy. |
| `valheimcheats_clone/` | Bản chụp HTML nhỏ hơn gồm 488 file. Cả 488 đường dẫn đều có trong bản lớn; chưa kết luận nội dung từng file giống hệt. | Không; chỉ ở máy. |
| `valheimcheats.com.zip` | File ZIP của bản chụp website, 58,9 MB, có 7.473 mục kể cả thư mục. Dùng làm bản lưu trữ cục bộ. | Không. |
| `clone_12_threads.py` | Script tải trang cũ với tối đa 12 luồng. Nó dùng đường dẫn tuyệt đối, trông chờ `urls.txt` và ghi vào `valheim_clone`; hiện không thuộc pipeline được kiểm chứng. | Không. |

Nội dung các bản chụp không được đưa lên repo public khi chưa có quyền tái xuất bản phù hợp. Xem [nguồn tham khảo](../sources/valheimcheats.json) và [Terms của website](https://valheimcheats.com/terms).

## 2. Mã nguồn, ví dụ và công cụ modding bên thứ ba

| Thư mục | Vai trò thực tế | Liên hệ với Việt hóa | GitHub |
| --- | --- | --- | --- |
| `Wiki/` | Bản chụp tài liệu cộng đồng Valheim Modding, gồm hướng dẫn và hình minh họa. | Tra cứu cách tạo/debug mod; bản chụp chưa rõ giấy phép gốc. | Không. |
| `ValheimLib/` | Framework mod Valheim đời cũ; README của nó chỉ sang Jotunn như hướng kế tiếp. | Tham khảo API cũ, tránh lấy làm nguồn dịch hiện hành. | Không. |
| `Valheim.DisplayBepInExInfo/` | Mod tiện ích hiển thị/thông báo thông tin BepInEx. | Hữu ích khi chẩn đoán môi trường mod, không phải bộ dịch. | Không. |
| `ModSettings/` | Mod/thư viện giao diện cài đặt cho mod. | Có bốn key English; dự án đã viết bốn ứng viên Việt hóa `draft`. | Không; chỉ bản dịch của dự án nằm trong `data/`. |
| `JotunnModStub/` | Bộ khung để bắt đầu một mod Jotunn mới. | Mẫu cấu trúc dự án, chưa có bộ nội dung dịch sản phẩm. | Không. |
| `JotunnModExample/` | Các mod ví dụ dùng Jotunn, gồm balô và bản thiết kế. | Có chín key ví dụ; đã tạo ứng viên dịch `draft`, không tính là nội dung game gốc. | Không; chỉ bản dịch của dự án nằm trong `data/`. |
| `Jotunn/` | Jötunn/JVL, framework phổ biến để mở rộng Valheim và nạp localization JSON/YAML. | Có 21 key giao diện framework; đã tạo ứng viên dịch `draft`. Các file `TestMod` chỉ là fixture. | Không; chỉ bản dịch của dự án nằm trong `data/`. |
| `ExampleMod/` | Dự án mẫu để học cấu trúc plugin/mod Valheim. | Tham khảo cách viết mod; chưa thấy bộ key dịch sản phẩm cần nhập. | Không. |
| `CommonPackages/` | Các dependency như NewtonsoftJson, YamlDotNet, UnityExplorer và bộ phát hiện tương ứng. | Hỗ trợ công cụ/mod; giấy phép thành phần khác nhau, không phải dữ liệu dịch game. | Không. |
| `AssetRipper/` | Công cụ đọc/trích xuất asset Unity. | Hỗ trợ kiểm kê dữ liệu Valheim. `AssetRipper/Localizations/vi` dịch chính giao diện AssetRipper, không phải Valheim. | Không. |

Các thư mục này là **snapshot**, không còn metadata `.git` riêng để xác định commit gốc. Giấy phép và vai trò từng nguồn được ghi trong [local_sources.json](../sources/local_sources.json). Không nên sao chép nguyên thư mục vào bản phát hành Việt hóa.

## 3. Phần lõi của repo Việt hóa

| Mục | Nội dung và cách dùng | GitHub |
| --- | --- | --- |
| [`data/`](../data/README.md) | Bản ghi JSONL Việt hóa theo `namespace`, key, hash nguồn, token, provenance và trạng thái. Hiện có 6.072 bản ghi `draft`: 6.038 game và 34 mod/ví dụ; chưa phải bản phát hành. | Có. |
| [`sources/`](../sources/local_sources.json) | Manifest build game, URL/điều kiện nguồn tham khảo và danh mục snapshot cục bộ. Đây là metadata, không chứa nguyên văn bản dump game/website. | Có. |
| [`docs/`](STATUS.md) | Hướng dẫn tích hợp, trạng thái QA và tài liệu thư mục này. | Có. |
| `tests/` | Unit tests cho token, xử lý key nguồn trùng, định dạng legacy và điều kiện `reviewed`. | Có. |
| `.github/` | GitHub Actions chạy test, kiểm tra JSONL và chặn file clone/binary trong mỗi push hoặc pull request. | Có. |
| `tools/` | Script trích nguồn game, nhập dữ liệu cũ/mod, kiểm tra bản dịch, xuất JSON, lập chỉ mục offline và tạo gói preview QA. | Có. |
| `local/` | Vùng làm việc riêng: nguồn trích từ game, 37 ngôn ngữ, bản dịch cũ `quarantine`, dữ liệu website chuẩn hóa, SQLite tìm kiếm và ZIP preview. | Không; `.gitignore` chặn. |
| `licenses/` | Bản sao giấy phép MIT của nguồn dịch monokaijs được tái sử dụng, để giữ ghi công và điều kiện giấy phép. | Có. |

## 4. File quản lý ở thư mục gốc

| Mục | Ý nghĩa | GitHub |
| --- | --- | --- |
| `.git/` | Cơ sở dữ liệu Git cục bộ: lịch sử commit, nhánh, remote và index. Không sửa/xóa thủ công. | Bản thân thư mục không được đẩy lên; GitHub nhận các commit. |
| [`.gitignore`](../.gitignore) | Quy định các đường dẫn chỉ giữ trên máy, gồm clone website, mã nguồn bên thứ ba, `local/` và file tạo tạm. CI kiểm tra riêng để chặn binary bị theo dõi. | Có. |
| [`LICENSE`](../LICENSE) | Giấy phép MIT cho phần do cộng đồng dự án tạo; quyền của website/game và các nguồn khác vẫn theo chủ sở hữu tương ứng. | Có. |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md) | Hướng dẫn đóng góp, ghi nguồn/giấy phép và chuyển bản dịch từ `draft` sang `reviewed`. | Có. |
| [`README.md`](../README.md) | Trang giới thiệu dự án, trạng thái hiện tại và các lệnh làm việc chính. | Có. |

## Nên mở mục nào trước?

- Muốn **xem trạng thái thật**: [STATUS.md](STATUS.md).
- Muốn **dịch/chỉnh câu**: [data/](../data/README.md) và [CONTRIBUTING.md](../CONTRIBUTING.md).
- Muốn **hiểu cách các nguồn được ghép**: [INTEGRATION.md](INTEGRATION.md).
- Muốn **tìm offline trong bản chụp website/mã nguồn**: chạy `python tools/search_local.py 'từ khóa'` sau khi tạo `local/corpus.sqlite3`.
