import re
import csv
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "contact_submissions.csv"


def validate_contact_payload(name: str, email: str, phone: str, subject: str, message: str) -> tuple[bool, str]:
    if not name or not name.strip():
        return False, "Nama lengkap tidak boleh kosong."
    if not email or not email.strip() or not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email.strip()):
        return False, "Format Email tidak valid."
    if not phone or not phone.strip():
        return False, "Nomor telepon/ponsel tidak boleh kosong."
    if not subject or not subject.strip():
        return False, "Subjek permintaan tidak boleh kosong."
    if not message or not message.strip():
        return False, "Pesan tidak boleh kosong."
    return True, ""


def save_contact_submission(name: str, email: str, phone: str, subject: str, message: str) -> dict:
    valid, err_msg = validate_contact_payload(name, email, phone, subject, message)
    if not valid:
        return {"success": False, "message": err_msg}

    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    wib = timezone(timedelta(hours=7))
    timestamp_str = datetime.now(wib).strftime("%Y-%m-%d %H:%M:%S")

    file_exists = CSV_PATH.exists() and CSV_PATH.stat().st_size > 0
    with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp (WIB)", "Name", "Email", "Phone", "Subject", "Message"])
        writer.writerow([timestamp_str, name.strip(), email.strip(), phone.strip(), subject.strip(), message.strip()])

    return {
        "success": True,
        "message": "Pesan Anda telah berhasil dikirimkan ke tim marketing PT Globalindo Buana."
    }
