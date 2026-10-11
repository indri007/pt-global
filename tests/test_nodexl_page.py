import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pages_content.nodexl_network import render_nodexl_network, NODEXL_CLOUD_TOKEN

class TestNodeXLPage(unittest.TestCase):
    def test_token_matches_gallery(self):
        self.assertEqual(NODEXL_CLOUD_TOKEN, "c1d8d71236e1cae9628f0b5c7a55b581")

    def test_callable(self):
        self.assertTrue(callable(render_nodexl_network))

if __name__ == "__main__":
    unittest.main()
