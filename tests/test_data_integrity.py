import unittest
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

class TestDataIntegrity(unittest.TestCase):
    def test_company_profile_exists_and_valid(self):
        profile_path = ROOT / "data" / "company_profile.json"
        self.assertTrue(profile_path.exists(), "data/company_profile.json must exist")
        with open(profile_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data.get("name"), "PT. Globalindo Buana")
        self.assertIn("Penjernihan", data.get("address", ""))
        self.assertEqual(data.get("phone"), "021-2524915")
        self.assertEqual(data.get("email"), "marketing@globalbuana.com")
        self.assertIn("10210", data.get("postal_code", ""))

    def test_services_catalog_contains_7_sectors(self):
        services_path = ROOT / "data" / "services.json"
        self.assertTrue(services_path.exists(), "data/services.json must exist")
        with open(services_path, "r", encoding="utf-8") as f:
            services = json.load(f)
        self.assertIsInstance(services, list)
        self.assertGreaterEqual(len(services), 7, "Must contain at least 7 key industry sectors")
        sector_names = [s.get("title", "") for s in services]
        self.assertTrue(any("Minyak" in s or "Oil" in s for s in sector_names))
        self.assertTrue(any("Kilang" in s or "Refinery" in s for s in sector_names))
        self.assertTrue(any("Pembangkit" in s or "Power" in s for s in sector_names))
        self.assertTrue(any("Semen" in s or "Cement" in s for s in sector_names))
        self.assertTrue(any("Pertambangan" in s or "Mining" in s for s in sector_names))
        self.assertTrue(any("Penerbangan" in s or "Aviation" in s for s in sector_names))
        self.assertTrue(any("EPC" in s for s in sector_names))

if __name__ == "__main__":
    unittest.main()
