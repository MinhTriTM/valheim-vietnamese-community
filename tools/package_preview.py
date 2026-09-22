"""Đóng gói preview BepInEx cục bộ để QA; không sửa game và không công bố."""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream", type=Path, required=True, help="Checkout monokaijs/valheim-viet-hoa có plugin và font")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    source = root / "local" / "game_sources.jsonl"
    manifest = json.loads((root / "sources" / "game_build_25390630.json").read_text(encoding="utf-8"))
    subprocess.run([sys.executable, str(root / "tools" / "build_translation.py"), "--namespace", "valheim", "--source-catalog", str(source), "--preview"], check=True)
    upstream = args.upstream.resolve()
    plugin_root = "plugins/ValheimVietHoa/"
    members = {
        upstream / "artifacts" / "ValheimVietnameseFont.dll": plugin_root + "ValheimVietnameseFont.dll",
        upstream / "SVN-Norse Regular.otf": plugin_root + "SVN-Norse Regular.otf",
        upstream / "SVN-Norse Bold.otf": plugin_root + "SVN-Norse Bold.otf",
        upstream / "ValheimVN-Sans-Regular.ttf": plugin_root + "ValheimVN-Sans-Regular.ttf",
        upstream / "ValheimVN-Serif-Regular.ttf": plugin_root + "ValheimVN-Serif-Regular.ttf",
        upstream / "licenses" / "OFL-Averia.txt": plugin_root + "OFL-Averia.txt",
        upstream / "licenses" / "OFL-Noto.txt": plugin_root + "OFL-Noto.txt",
        upstream / "LICENSE": "LICENSE-monokaijs.txt",
        root / "LICENSE": "LICENSE-project.txt",
        root / "local" / "export" / "valheim.preview.json": plugin_root + "Translations/Vietnamese/ValheimVietHoa.json",
    }
    missing = [str(path) for path in members if not path.is_file()]
    if missing:
        raise FileNotFoundError("Thiếu thành phần preview: " + ", ".join(missing))
    output = root / "local" / "valheim-preview-25390630.zip"
    temporary = output.with_suffix(".zip.tmp")
    notice = ("PREVIEW CHỈ ĐỂ QA - 6038 bản dịch draft, chưa rà soát nghĩa toàn bộ hoặc chạy Valheim 1.0.15.\n"
              f"Nguồn game: build {manifest['game_build']}, resources.assets SHA-256 {manifest['resources_sha256']}.\n"
              "Loader/font từ monokaijs/valheim-viet-hoa; xem LICENSE-monokaijs.txt và các giấy phép font.\n"
              "Không ghi đè hồ sơ chơi chính. Sao lưu plugin và game trước khi cài trong hồ sơ test.\n")
    with ZipFile(temporary, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path, target in members.items():
            archive.write(path, target)
        archive.writestr("README_QA.txt", notice)
    os.replace(temporary, output)
    print(f"Gói QA cục bộ: {output} ({output.stat().st_size} byte)")


if __name__ == "__main__":
    main()
