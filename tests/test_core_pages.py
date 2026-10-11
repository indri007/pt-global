import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pages_content.home import render_home
from pages_content.about import render_about
from pages_content.services import render_services

class TestCorePages(unittest.TestCase):
    def test_functions_callable(self):
        self.assertTrue(callable(render_home))
        self.assertTrue(callable(render_about))
        self.assertTrue(callable(render_services))

if __name__ == "__main__":
    unittest.main()
