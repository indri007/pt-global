import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pages_content.safety_quality import render_safety_quality
from pages_content.portfolio import render_portfolio
from pages_content.safety_moment import render_safety_moment, classify_risk

class TestSafetyPortfolio(unittest.TestCase):
    def test_callables(self):
        self.assertTrue(callable(render_safety_quality))
        self.assertTrue(callable(render_portfolio))
        self.assertTrue(callable(render_safety_moment))

    def test_risk_classification_thresholds(self):
        # 1-4: RENDAH (success)
        callout, label, action = classify_risk(1)
        self.assertEqual(label, "RENDAH")
        self.assertEqual(callout, "success")
        callout, label, action = classify_risk(4)
        self.assertEqual(label, "RENDAH")
        self.assertEqual(callout, "success")

        # 5-9: SEDANG (warning)
        callout, label, action = classify_risk(5)
        self.assertEqual(label, "SEDANG")
        self.assertEqual(callout, "warning")
        callout, label, action = classify_risk(9)
        self.assertEqual(label, "SEDANG")
        self.assertEqual(callout, "warning")

        # 10-16: TINGGI (warning)
        callout, label, action = classify_risk(10)
        self.assertEqual(label, "TINGGI")
        self.assertEqual(callout, "warning")
        callout, label, action = classify_risk(16)
        self.assertEqual(label, "TINGGI")
        self.assertEqual(callout, "warning")

        # 17-25: EKSTREM (error)
        callout, label, action = classify_risk(17)
        self.assertEqual(label, "EKSTREM")
        self.assertEqual(callout, "error")
        callout, label, action = classify_risk(25)
        self.assertEqual(label, "EKSTREM")
        self.assertEqual(callout, "error")

    def test_permenaker_reference_in_safety_moment_source(self):
        src_file = ROOT / "pages_content" / "safety_moment.py"
        content = src_file.read_text(encoding="utf-8")
        self.assertIn("Permenaker No. 9 Tahun 2016", content)

if __name__ == "__main__":
    unittest.main()
