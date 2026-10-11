import sys
import unittest
import importlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

class TestFullAppIntegration(unittest.TestCase):
    def test_app_imports_cleanly(self):
        app = importlib.import_module("app")
        self.assertTrue(hasattr(app, "main") or hasattr(app, "PAGES"))

    def test_all_pages_registered(self):
        import app
        self.assertIn("Home", app.PAGES)
        self.assertIn("About Us", app.PAGES)
        self.assertIn("Our Services", app.PAGES)
        self.assertIn("Safety & Quality", app.PAGES)
        self.assertIn("Portfolio", app.PAGES)
        self.assertIn("Safety Moment", app.PAGES)
        self.assertIn("Contact & Maps", app.PAGES)
        self.assertIn("NodeXL Intelligence", app.PAGES)

if __name__ == "__main__":
    unittest.main()
