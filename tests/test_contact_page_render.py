import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pages_content.contact_maps import render_contact_maps

class TestContactPageRender(unittest.TestCase):
    def test_callable(self):
        self.assertTrue(callable(render_contact_maps))

if __name__ == "__main__":
    unittest.main()
