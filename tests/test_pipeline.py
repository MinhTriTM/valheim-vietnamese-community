"""Kiểm tra các cổng an toàn có thể làm hỏng bản dịch khi cập nhật."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from extract_game import extract_rows
from import_local import signature
from validate import main as validate


class PipelineTests(unittest.TestCase):
    def test_numeric_placeholder_changes_signature(self):
        self.assertNotEqual(signature("Đã tải $1"), signature("Đã tải $2"))
        self.assertEqual(signature("Version $1, $2"), signature("Phiên bản $1, $2"))

    def test_duplicate_source_occurrences_are_preserved(self):
        base = "key,English,German\nfoo,Old,Alt\n"
        update = "key,English,German\nfoo,New,Neu\n"
        keys, count, languages = extract_rows([("localization", base), ("localization_update", update)])
        self.assertEqual(count, 2)
        self.assertEqual(len(keys["foo"]), 2)
        self.assertIn("German", languages)

    def test_reviewed_requires_reviewer_and_matching_tokens(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "translations.jsonl"
            row = {"namespace": "test", "key": "greeting", "source_sha256": hashlib.sha256(b"Hello $1").hexdigest(), "technical_signature": signature("Hello $1"), "vi": "Chào $1", "status": "reviewed", "origin": "test", "game_build": "1", "mod_version": "", "reviewer": ""}
            path.write_text(json.dumps(row) + "\n", encoding="utf-8")
            self.assertEqual(validate(Path(folder)), 1)
            row["reviewer"] = "tester"
            row["vi"] = "Chào $2"
            path.write_text(json.dumps(row) + "\n", encoding="utf-8")
            self.assertEqual(validate(Path(folder)), 1)
            row["vi"] = "Chào $1"
            path.write_text(json.dumps(row) + "\n", encoding="utf-8")
            self.assertEqual(validate(Path(folder)), 0)


if __name__ == "__main__":
    unittest.main()
