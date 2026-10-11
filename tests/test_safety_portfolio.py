import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pages_content.safety_quality import render_safety_quality
from pages_content.portfolio import render_portfolio
from pages_content.safety_moment import render_safety_moment

class TestSafetyPortfolio(unittest.TestCase):
    def test_callables(self):
        self.assertTrue(callable(render_safety_quality))
        self.assertTrue(callable(render_portfolio))
        self.assertTrue(callable(render_safety_moment))

if __name__ == "__main__":
    unittest.main()
