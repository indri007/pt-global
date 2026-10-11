import unittest
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from pages_content.contact_service import save_contact_submission, validate_contact_payload

class TestContactWorkflow(unittest.TestCase):
    def test_validation_rejects_empty_fields(self):
        valid, err = validate_contact_payload("", "test@globalbuana.com", "021-2524915", "Test", "Msg")
        self.assertFalse(valid)
        self.assertIn("Nama", err)

    def test_validation_rejects_invalid_email(self):
        valid, err = validate_contact_payload("Budi", "invalid-email", "021-2524915", "Test", "Msg")
        self.assertFalse(valid)
        self.assertIn("Email", err)

    def test_save_contact_submission_success(self):
        res = save_contact_submission(
            name="Testing Person",
            email="engineer@pertamina.com",
            phone="08123456789",
            subject="Inquiry Well Services EPC",
            message="Mohon penawaran jasa perawatan wellhead."
        )
        self.assertTrue(res.get("success"))
        self.assertIn("berhasil", res.get("message", "").lower())

if __name__ == "__main__":
    unittest.main()
