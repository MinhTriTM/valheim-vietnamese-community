"""Chặn việc đưa bản chụp cục bộ hoặc binary vào repo public."""
import subprocess
import sys
from pathlib import Path

BLOCKED_PREFIXES = (
    "local/", "mods/", "valheimcheats.com/", "valheimcheats_clone/", "AssetRipper/",
    "CommonPackages/", "ExampleMod/", "Jotunn/", "JotunnModExample/",
    "JotunnModStub/", "ModSettings/", "Valheim.DisplayBepInExInfo/",
    "ValheimLib/", "Wiki/", "Tài Liệu/", "Lich_Su_Truy_Van/",
)
BLOCKED_SUFFIXES = (".dll", ".exe", ".zip", ".assets", ".bundle", ".pak")
BLOCKED_NAMES = {"valheimcheats.com.zip", "clone_12_threads.py"}


def main():
    root = Path(__file__).resolve().parents[1]
    tracked = subprocess.check_output(["git", "-C", str(root), "ls-files", "-z"]).decode("utf-8").split("\0")
    forbidden = [path for path in tracked if path and (path in BLOCKED_NAMES or path.startswith(BLOCKED_PREFIXES) or path.lower().endswith(BLOCKED_SUFFIXES))]
    if forbidden:
        print("File không được công bố:", file=sys.stderr)
        for path in forbidden:
            print(path, file=sys.stderr)
        return 1
    print(f"PASS: {len([path for path in tracked if path])} file được Git theo dõi, không có bản chụp/binary bị cấm")
    return 0


if __name__ == "__main__":
    sys.exit(main())
