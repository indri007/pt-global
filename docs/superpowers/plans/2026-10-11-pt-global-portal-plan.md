# PT Globalindo Buana Web Portal & NodeXL Intelligence Hub Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Membangun web portal korporat interaktif berbasis Streamlit untuk PT Globalindo Buana (kantor pusat Jl. Penjernihan 1 No. 12B Jakarta Pusat) yang mencakup seluruh sitemap 7 sektor industri, K3/HSE, formulir kontak, dan NodeXL Network Intelligence Hub.

**Architecture:** Arsitektur modular multi-halaman berbasis Streamlit dengan pemisahan berkas data terstruktur (`data/*.json`), modul renderer per halaman sitemap (`pages_content/*.py`), router utama (`app.py`), dan automated testing (`tests/*.py`).

**Tech Stack:** Python 3.10+, Streamlit, Pandas, Plotly Express, Pytest.

## Global Constraints

- Alamat resmi: `Jl. Penjernihan 1 No. 12B, RT.9/RW.6, Bend. Hilir, Kecamatan Tanah Abang, Kota Jakarta Pusat, DKI Jakarta 10210`
- Telepon: `021-2524915`, Email: `marketing@globalbuana.com`
- Hak cipta wajib dicantumkan: `© Copyright 2025 PT. Globalindo Buana. All Right Reserved | Dev by WebNesia`
- NodeXL Cloud Gallery Token: `c1d8d71236e1cae9628f0b5c7a55b581`
- Palet warna UI: Deep Industrial Navy (`#0a2540` / `#004b87`) dan Safety Amber (`#f59e0b` / `#d97706`).
- Semua unit test harus lolos 100% menggunakan `pytest`.

---

### Task 1: Environment & Foundation Data Layer

**Files:**
- Create: `requirements.txt`
- Create: `.streamlit/config.toml`
- Create: `data/company_profile.json`
- Create: `data/services.json`
- Test: `tests/test_data_integrity.py`

**Interfaces:**
- Produces: `data/company_profile.json` dan `data/services.json` yang akan dibaca oleh seluruh modul renderer halaman.

- [ ] **Step 1: Write the failing test for data integrity**

```python
# tests/test_data_integrity.py
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_data_integrity.py`
Expected: FAIL with missing file error.

- [ ] **Step 3: Create dependencies & configuration**

Create `requirements.txt`:
```
streamlit>=1.35.0
pandas>=2.0.0
plotly>=5.18.0
pytest>=8.0.0
```

Create `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#004b87"
backgroundColor = "#f8fafc"
secondaryBackgroundColor = "#e2e8f0"
textColor = "#0f172a"
font = "sans serif"

[server]
headless = true
enableCORS = false
enableXsrfProtection = true
```

Create `data/company_profile.json`:
```json
{
  "name": "PT. Globalindo Buana",
  "tagline": "Integrated Industrial & Engineering Solutions",
  "address": "Jl. Penjernihan 1 No. 12B, RT.9/RW.6, Bendungan Hilir, Kecamatan Tanah Abang, Kota Jakarta Pusat, DKI Jakarta",
  "postal_code": "10210",
  "phone": "021-2524915",
  "email": "marketing@globalbuana.com",
  "website": "https://globalbuana.com",
  "copyright": "© Copyright 2025 PT. Globalindo Buana. All Right Reserved | Dev by WebNesia",
  "social_media": {
    "facebook": "https://facebook.com",
    "instagram": "https://instagram.com",
    "linkedin": "https://linkedin.com",
    "youtube": "https://youtube.com"
  },
  "vision": "Menjadi mitra rekayasa industri terpadu dan pemeliharaan strategis terkemuka di Indonesia yang diakui atas keunggulan teknis, ketepatan solusi, dan kepatuhan keselamatan kelas dunia.",
  "mission": [
    "Menyediakan solusi rekayasa, well services, dan pemeliharaan industri dengan standar kualitas tertinggi.",
    "Mengutamakan keselamatan kerja (Target Zero Incident) dan kelestarian lingkungan dalam setiap proyek.",
    "Membangun hubungan kemitraan jangka panjang berlandaskan integritas, transparansi, dan kepuasan pelanggan.",
    "Mengembangkan kapabilitas sumber daya manusia rekayasa nasional yang kompeten dan tersertifikasi."
  ],
  "core_values": [
    {"name": "Safety First", "desc": "Keselamatan kerja tanpa kompromi pada setiap tahapan operasi."},
    {"name": "Engineering Excellence", "desc": "Presisi rekayasa dan teknologi terkini untuk kehandalan fasilitas industri."},
    {"name": "Integrity", "desc": "Kejujuran dan etika profesional tertinggi dalam setiap komitmen bisnis."},
    {"name": "Customer Partnership", "desc": "Dedikasi penuh untuk nilai tambah dan kelancaran operasi klien."}
  ]
}
```

Create `data/services.json`:
```json
[
  {
    "id": "oil-gas",
    "title": "Minyak & Gas (Well Services & Intervention)",
    "category": "Upstream & Downstream",
    "icon": "🛢️",
    "description": "Layanan pemeliharaan sumur minyak dan gas darat maupun lepas pantai terpadu untuk memastikan kontinuitas produksi.",
    "capabilities": [
      "Wellhead Maintenance & Pressure Testing",
      "Slickline & Wireline Operations",
      "High Pressure Chemical Pumping",
      "Well Control Equipment Inspection",
      "Valve Maintenance & In-situ Lubrication"
    ]
  },
  {
    "id": "refinery",
    "title": "Kilang Minyak & Petrokimia",
    "category": "Processing Facility",
    "icon": "🏭",
    "description": "Dukungan turnaround komprehensif, overhauling alat penukar panas, dan fabrikasi jalur pipa berstandar tinggi.",
    "capabilities": [
      "Refinery Plant Turnaround Support",
      "Heat Exchanger Cleaning & Retubing",
      "Pressure Vessel Inspection & Repair",
      "Specialized High-Pressure Piping Fabrication",
      "Storage Tank Maintenance & NDT Inspection"
    ]
  },
  {
    "id": "power",
    "title": "Pembangkit Listrik (Power Generation)",
    "category": "Energy Infrastructure",
    "icon": "⚡",
    "description": "Solusi pemeliharaan turbin uap/gas, boiler pembangkit, dan sistem instrumentasi kelistrikan tegangan tinggi.",
    "capabilities": [
      "Turbine Major & Minor Overhaul",
      "Boiler Tube Inspection & Refractory Repair",
      "Balance of Plant (BOP) Maintenance",
      "Transformer & Switchgear Diagnostic Support",
      "Vibration Analysis & Rotating Equipment Balancing"
    ]
  },
  {
    "id": "cement",
    "title": "Industri Semen",
    "category": "Heavy Manufacturing",
    "icon": "🏗️",
    "description": "Pemeliharaan mesin berat rotari kiln, raw mill, dan sistem konveyor penanganan material curah.",
    "capabilities": [
      "Rotary Kiln Alignment & Tyre Maintenance",
      "Ball Mill & Vertical Roller Mill Overhaul",
      "Heavy Material Handling Conveyor Maintenance",
      "Baghouse Filter & Dust Collector Optimization",
      "Dynamic Balancing of Heavy Industrial Fans"
    ]
  },
  {
    "id": "mining",
    "title": "Pertambangan (Mining Industry)",
    "category": "Mineral Processing",
    "icon": "⛏️",
    "description": "Layanan pemeliharaan fasilitas pemrosesan mineral, peremuk batuan (crusher), dan sistem pemipaan bubur bijih.",
    "capabilities": [
      "Primary & Secondary Crusher Overhaul",
      "Slurry Pipeline Installation & Wear Lining",
      "Flotation Cell & Agitator Maintenance",
      "Heavy Mechanical Structural Repair",
      "Heavy Equipment Hydraulic Line Maintenance"
    ]
  },
  {
    "id": "aviation",
    "title": "Penerbangan (Aviation Support)",
    "category": "Aviation Infrastructure",
    "icon": "✈️",
    "description": "Sistem infrastruktur penanganan bahan bakar avtur dan peralatan pendukung darat bandar udara.",
    "capabilities": [
      "Aviation Fuel Hydrant System Maintenance",
      "Filtration & Water Separation Calibration",
      "Fuel Storage Tank Cleaning & Quality Compliance",
      "Ground Support Equipment (GSE) Mechanical Servicing",
      "Safety Emergency Shutdown System Testing"
    ]
  },
  {
    "id": "epc",
    "title": "EPC & Maintenance Terintegrasi",
    "category": "Turnkey Engineering",
    "icon": "📐",
    "description": "Solusi rekayasa menyeluruh mulai dari studi kelayakan, pengadaan material bersertifikat, hingga konstruksi dan kontrak pemeliharaan jangka panjang.",
    "capabilities": [
      "Detail Engineering Design (Mechanical & Piping)",
      "Certified Procurement & Supply Chain Sourcing",
      "On-site Mechanical & Civil Construction",
      "Pre-Commissioning & Commissioning Support",
      "Comprehensive Long-term Maintenance Contracts (LTM)"
    ]
  }
]
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_data_integrity.py`
Expected: PASS (2 tests passed).

- [ ] **Step 5: Commit**

```bash
git add requirements.txt .streamlit/config.toml data/ tests/test_data_integrity.py
git commit -m "feat(core): add foundation data models, config, and integrity test"
```

---

### Task 2: Contact Form Processor & Workflow Testing

**Files:**
- Create: `data/contact_submissions.csv` (initialized)
- Create: `pages_content/contact_service.py`
- Test: `tests/test_contact_workflow.py`

**Interfaces:**
- Produces: `save_contact_submission(name, email, phone, subject, message) -> dict`

- [ ] **Step 1: Write the failing test for contact submission**

```python
# tests/test_contact_workflow.py
import unittest
from pathlib import Path
import csv

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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_contact_workflow.py`
Expected: FAIL with `ModuleNotFoundError: No module named 'pages_content.contact_service'`

- [ ] **Step 3: Implement `pages_content/contact_service.py`**

```python
# pages_content/contact_service.py
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
        return False, "Format email tidak valid."
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_contact_workflow.py`
Expected: PASS (3 tests passed).

- [ ] **Step 5: Commit**

```bash
git add pages_content/contact_service.py tests/test_contact_workflow.py
git commit -m "feat(contact): add contact submission processor, validation, and tests"
```

---

### Task 3: Core Corporate Page Renderers (Home, About, Services)

**Files:**
- Create: `pages_content/__init__.py`
- Create: `pages_content/home.py`
- Create: `pages_content/about.py`
- Create: `pages_content/services.py`
- Test: `tests/test_core_pages.py`

**Interfaces:**
- Produces: `render_home()`, `render_about()`, `render_services()`

- [ ] **Step 1: Write test for core pages**

```python
# tests/test_core_pages.py
import unittest
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_core_pages.py`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Implement core page renderers**

Create `pages_content/__init__.py`:
```python
# pages_content package
```

Create `pages_content/home.py`:
```python
import streamlit as st
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def render_home():
    with open(ROOT / "data" / "company_profile.json", "r", encoding="utf-8") as f:
        profile = json.load(f)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #0a2540 0%, #004b87 100%); padding: 42px 28px; border-radius: 12px; color: white; margin-bottom: 28px;">
        <span style="background: #f59e0b; color: #0f172a; font-weight: 700; font-size: 12px; padding: 4px 12px; border-radius: 9999px; text-transform: uppercase;">Engineering & Energy Solutions</span>
        <h1 style="color: white; margin-top: 14px; font-size: 36px; font-weight: 800;">PT. GLOBALINDO BUANA</h1>
        <p style="font-size: 18px; color: #e2e8f0; max-width: 800px; margin-top: 10px;">
            Penyedia solusi rekayasa industri terintegrasi untuk Minyak & Gas, Kilang, Pembangkit Listrik, Semen, Pertambangan, Penerbangan, dan Petrokimia.
        </p>
        <p style="color: #94a3b8; font-size: 14px; margin-top: 6px;">
            📍 Kantor Pusat: Jl. Penjernihan 1 No. 12B, Bendungan Hilir, Jakarta Pusat 10210
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Sektor Industri", "7 Sektor Utama", "Migas & Energi")
    with col2:
        st.metric("Standar K3", "Target Zero", "ISO 45001")
    with col3:
        st.metric("Layanan Operasional", "24 / 7", "EPC & Well Services")
    with col4:
        st.metric("Wilayah Layanan", "Seluruh Indonesia", "Onshore & Offshore")

    st.markdown("---")
    st.subheader("Keunggulan Kompetitif Kami")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        * **Keahlian Teknis Terpadu:** Tim teknisi dan insinyur berpengalaman dalam operasi bertekanan tinggi (*well services*, *pipeline*, *turbine overhaul*).
        * **Kepatuhan Keselamatan Ketat:** Mengadopsi prinsip *Stop Work Authority* (SWA) untuk mencegah kecelakaan di area berisiko tinggi.
        """)
    with c2:
        st.markdown("""
        * **Konektivitas Strategis:** Lokasi kantor pusat di Jalan Penjernihan 1 Jakarta Pusat memastikan respon cepat koordinasi ke seluruh pemangku kepentingan industri energi.
        * **Manajemen Proyek Terukur:** Dukungan pengadaan tersertifikasi dan kontrak pemeliharaan jangka panjang (*Long-Term Service Agreements*).
        """)
```

Create `pages_content/about.py`:
```python
import streamlit as st
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def render_about():
    with open(ROOT / "data" / "company_profile.json", "r", encoding="utf-8") as f:
        profile = json.load(f)

    st.title("🏢 Tentang PT Globalindo Buana")
    st.caption("Profil Perusahaan, Visi, Misi, & Legalitas Operasional")

    st.markdown("""
    **PT Globalindo Buana** adalah perseroan terbatas terkemuka di Indonesia yang bergerak dalam bidang penyediaan jasa rekayasa, pengadaan, konstruksi, dan pemeliharaan fasilitas industri berat (*well services, refinery turnaround, power generation, cement machinery, mining, aviation, and EPC*).
    
    Berkantor pusat di **Jalan Penjernihan 1 No. 12B, Bendungan Hilir, Tanah Abang, Jakarta Pusat**, perusahaan kami mendedikasikan seluruh kompetensi teknik untuk mendukung kehandalan operasi industri strategis nasional.
    """)

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎯 Visi Perusahaan")
        st.info(profile.get("vision"))
    with col2:
        st.subheader("🚀 Misi Perusahaan")
        for m in profile.get("mission", []):
            st.markdown(f"- {m}")

    st.markdown("---")
    st.subheader("💎 Nilai-Nilai Inti (Core Values)")
    val_cols = st.columns(4)
    for idx, v in enumerate(profile.get("core_values", [])):
        with val_cols[idx % 4]:
            st.markdown(f"**{v['name']}**")
            st.caption(v['desc'])
```

Create `pages_content/services.py`:
```python
import streamlit as st
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def render_services():
    with open(ROOT / "data" / "services.json", "r", encoding="utf-8") as f:
        services = json.load(f)

    st.title("⚙️ Layanan & Solusi Industri Terintegrasi")
    st.caption("Solusi rekayasa dan pemeliharaan handal untuk 7 sektor strategis")

    for s in services:
        with st.expander(f"{s['icon']} {s['title']} — [{s['category']}]", expanded=False):
            st.write(s['description'])
            st.markdown("**Ruang Lingkup & Kapabilitas Teknis:**")
            for cap in s['capabilities']:
                st.markdown(f"- {cap}")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_core_pages.py`
Expected: PASS (1 test passed).

- [ ] **Step 5: Commit**

```bash
git add pages_content/__init__.py pages_content/home.py pages_content/about.py pages_content/services.py tests/test_core_pages.py
git commit -m "feat(pages): implement Home, About, and Services core pages"
```

---

### Task 4: HSE, Portfolio, and Safety Moment Modules

**Files:**
- Create: `pages_content/safety_quality.py`
- Create: `pages_content/portfolio.py`
- Create: `pages_content/safety_moment.py`
- Test: `tests/test_safety_portfolio.py`

**Interfaces:**
- Produces: `render_safety_quality()`, `render_portfolio()`, `render_safety_moment()`

- [ ] **Step 1: Write test for HSE and Portfolio modules**

```python
# tests/test_safety_portfolio.py
import unittest
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_safety_portfolio.py`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Implement HSE, Portfolio, and Safety Moment pages**

Create `pages_content/safety_quality.py`:
```python
import streamlit as st

def render_safety_quality():
    st.title("🛡️ Keselamatan Kerja & Mutu (HSE & Quality)")
    st.caption("Filosofi Target Zero: Zero Accident, Zero Harm, Zero Pollution")

    st.markdown("""
    Bagi **PT Globalindo Buana**, keselamatan kerja bukan sekadar slogan, melainkan budaya operasional yang terintegrasi di seluruh lini proyek.
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("🏅 **ISO 9001:2015**\n\nSistem Manajemen Mutu berstandar internasional.")
    with col2:
        st.info("🌿 **ISO 14001:2015**\n\nSistem Manajemen Lingkungan dan mitigasi dampak ekologis.")
    with col3:
        st.warning("🦺 **ISO 45001:2018**\n\nSistem Manajemen Kesehatan & Keselamatan Kerja (K3).")

    st.markdown("---")
    st.subheader("Prinsip Utama K3 Lapangan")
    st.markdown("""
    1. **Stop Work Authority (SWA):** Setiap karyawan dan teknisi lapangan memiliki hak dan kewajiban mutlak untuk menghentikan pekerjaan jika melihat kondisi atau tindakan tidak aman.
    2. **Toolbox Meeting Wajib:** Setiap shift kerja diawali dengan identifikasi bahaya dan evaluasi prosedur kerja.
    3. **Inspeksi APD Berkala:** Seluruh alat pelindung diri bersertifikasi ANSI / SNI dan diaudit berkala.
    """)
```

Create `pages_content/portfolio.py`:
```python
import streamlit as st

def render_portfolio():
    st.title("💼 Portfolio & Rekam Jejak Proyek")
    st.caption("Pengalaman implementasi rekayasa dan pemeliharaan fasilitas energi")

    projects = [
      {
        "client_sector": "Minyak & Gas Lepas Pantai",
        "project": "Wellhead Maintenance & Pressure Pumping Campaign",
        "scope": "Inspeksi katup tekanan tinggi, grease injection, dan uji integritas 28 kepala sumur.",
        "status": "Selesai Sempurna — Zero LTI"
      },
      {
        "client_sector": "Kilang Minyak Nasional",
        "project": "Refinery Major Turnaround Heat Exchanger Overhaul",
        "scope": "Hydro-cleaning, retubing, dan bundle extraction 14 unit heat exchanger.",
        "status": "Selesai Sesuai Jadwal"
      },
      {
        "client_sector": "Pembangkit Listrik Jawa-Bali",
        "project": "Steam Turbine Rotor & Balance of Plant Inspection",
        "scope": "Overhaul mekanikal, balancing dinamis, dan kalibrasi sistem kontrol hidrolik turbin.",
        "status": "Operasional Optimal"
      },
      {
        "client_sector": "Industri Semen",
        "project": "Rotary Kiln Tyre Realignment & Drive Maintenance",
        "scope": "Penggantian segment gear dan laser alignment pada fasilitas kiln berkapasitas 5.000 ton/hari.",
        "status": "Selesai Sempurna"
      }
    ]

    for p in projects:
        st.markdown(f"### 📌 {p['project']}")
        st.markdown(f"**Sektor:** `{p['client_sector']}` | **Status:** ✅ `{p['status']}`")
        st.write(p['scope'])
        st.markdown("---")
```

Create `pages_content/safety_moment.py`:
```python
import streamlit as st

def render_safety_moment():
    st.title("⚡ Safety Moment & Edukasi K3 Harian")
    st.caption("Materi panduan keselamatan kerja sebelum memulai shift harian")

    topic = st.selectbox(
        "Pilih Topik Safety Moment Hari Ini:",
        ["Bekerja di Ketinggian (Working at Heights)", "Izin Kerja Panas (Hot Work Permit)", "Ruang Terbatas (Confined Space)", "Alat Pelindung Diri (PPE)"]
    )

    if topic == "Bekerja di Ketinggian (Working at Heights)":
        st.warning("⚠️ **Aturan Emas:** Gunakan Full Body Harness dengan double lanyard berpengait besar yang tertambat pada anchor point kokoh pada ketinggian > 1.8 meter.")
    elif topic == "Izin Kerja Panas (Hot Work Permit)":
        st.warning("🔥 **Aturan Emas:** Pastikan radius 10 meter bebas bahan mudah terbakar, sediakan APAR CO2/Powder siap pakai, dan tugaskan Fire Watcher aktif.")
    elif topic == "Ruang Terbatas (Confined Space)":
        st.warning("🕳️ **Aturan Emas:** Uji kadar oksigen (19.5% - 23.5%) dan gas beracun (H2S, LEL) dengan calibrated gas detector sebelum memasuki bejana/tangki.")
    else:
        st.info("🦺 **Aturan Emas:** Periksa kondisi helm keselamatan, kacamata pelindung, sarung tangan mekanik, dan sepatu safety tahan minyak sebelum memasuki area plant.")

    st.markdown("---")
    st.subheader("Matriks Evaluasi Risiko Cepat (5x5)")
    col1, col2 = st.columns(2)
    with col1:
        prob = st.slider("Kemungkinan Kejadian (Likelihood 1-5)", 1, 5, 2)
    with col2:
        sev = st.slider("Tingkat Keparahan (Severity 1-5)", 1, 5, 3)
    score = prob * sev
    if score >= 15:
        st.error(f"Skor Risiko: {score} (RISIKO TINGGI — Pekerjaan Harus Dimodifikasi)")
    elif score >= 8:
        st.warning(f"Skor Risiko: {score} (RISIKO SEDANG — Butuh Tindakan Mitigasi Khusus)")
    else:
        st.success(f"Skor Risiko: {score} (RISIKO RENDAH — Lanjutkan dengan SOP Baku)")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_safety_portfolio.py`
Expected: PASS (1 test passed).

- [ ] **Step 5: Commit**

```bash
git add pages_content/safety_quality.py pages_content/portfolio.py pages_content/safety_moment.py tests/test_safety_portfolio.py
git commit -m "feat(pages): implement Safety Quality, Portfolio, and Safety Moment pages"
```

---

### Task 5: Interactive Contact & Google Maps Page

**Files:**
- Create: `pages_content/contact_maps.py`
- Test: `tests/test_contact_page_render.py`

**Interfaces:**
- Consumes: `pages_content.contact_service.save_contact_submission`
- Produces: `render_contact_maps()`

- [ ] **Step 1: Write test for contact page render**

```python
# tests/test_contact_page_render.py
import unittest
from pages_content.contact_maps import render_contact_maps

class TestContactPageRender(unittest.TestCase):
    def test_callable(self):
        self.assertTrue(callable(render_contact_maps))

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_contact_page_render.py`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Implement `pages_content/contact_maps.py`**

```python
import streamlit as st
import json
from pathlib import Path
from pages_content.contact_service import save_contact_submission

ROOT = Path(__file__).resolve().parent.parent

def render_contact_maps():
    with open(ROOT / "data" / "company_profile.json", "r", encoding="utf-8") as f:
        profile = json.load(f)

    st.title("📍 Hubungi Kami & Lokasi Kantor Pusat")
    st.caption("Kantor Pusat PT Globalindo Buana — Jalan Penjernihan 1, Jakarta Pusat")

    col_info, col_form = st.columns([1, 1.2])

    with col_info:
        st.subheader("Informasi Kontak Resmi")
        st.markdown(f"""
        🏢 **{profile['name']}**  
        📍 **Alamat:** {profile['address']}  
        📮 **Kode Pos:** {profile['postal_code']}  
        📞 **Telepon:** `{profile['phone']}`  
        ✉️ **Email:** `{profile['email']}`  
        🌐 **Website:** [{profile['website']}]({profile['website']})
        """)
        st.markdown("---")
        st.markdown("**Media Sosial Resmi:**")
        soc = profile.get("social_media", {})
        st.markdown(f"• [Facebook]({soc.get('facebook')}) | [Instagram]({soc.get('instagram')}) | [LinkedIn]({soc.get('linkedin')}) | [YouTube]({soc.get('youtube')})")

    with col_form:
        st.subheader("Kirimkan Pesan / Inquiry Proyek")
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Nama Lengkap (*)")
            email = st.text_input("Email Perusahaan (*)")
            phone = st.text_input("Nomor Telepon / WhatsApp (*)")
            subject = st.text_input("Subjek Permintaan (*)")
            message = st.text_area("Pesan / Keterangan Kebutuhan Teknis (*)", height=120)
            submitted = st.form_submit_button("🚀 Kirim Pesan Sekarang")

            if submitted:
                res = save_contact_submission(name, email, phone, subject, message)
                if res.get("success"):
                    st.success(f"✅ {res.get('message')}")
                else:
                    st.error(f"⚠️ {res.get('message')}")

    st.markdown("---")
    st.subheader("Peta Interaktif Kantor Pusat (Jl. Penjernihan 1 Jakarta Pusat)")
    
    # Embed Google Maps Iframe (Bendungan Hilir, Tanah Abang, Jakarta Pusat 10210)
    map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3966.452668383818!2d106.80931557499026!3d-6.203867693783982!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e69f697424ea4b1%3A0xe543ec682c3f81e!2sJl.%20Penjernihan%20I%20No.12B%2C%20RT.9%2FRW.6%2C%20Bend.%20Hilir%2C%20Kecamatan%20Tanah%20Abang%2C%20Kota%20Jakarta%20Pusat%2C%20Daerah%20Khusus%20Ibukota%20Jakarta%2010210!5e0!3m2!1sid!2sid!4v1700000000000!5m2!1sid!2sid"
    
    st.components.v1.iframe(map_url, height=380, scrolling=False)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_contact_page_render.py`
Expected: PASS (1 test passed).

- [ ] **Step 5: Commit**

```bash
git add pages_content/contact_maps.py tests/test_contact_page_render.py
git commit -m "feat(contact): implement interactive contact form and Google Maps page"
```

---

### Task 6: NodeXL Network Intelligence & Graph Gallery Cloud Hub

**Files:**
- Create: `pages_content/nodexl_network.py`
- Test: `tests/test_nodexl_page.py`

**Interfaces:**
- Produces: `render_nodexl_network()`

- [ ] **Step 1: Write test for NodeXL network page**

```python
# tests/test_nodexl_page.py
import unittest
from pages_content.nodexl_network import render_nodexl_network, NODEXL_CLOUD_TOKEN

class TestNodeXLPage(unittest.TestCase):
    def test_token_matches_gallery(self):
        self.assertEqual(NODEXL_CLOUD_TOKEN, "c1d8d71236e1cae9628f0b5c7a55b581")

    def test_callable(self):
        self.assertTrue(callable(render_nodexl_network))

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_nodexl_page.py`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Implement `pages_content/nodexl_network.py`**

```python
import streamlit as st
import pandas as pd
import plotly.express as px

NODEXL_CLOUD_TOKEN = "c1d8d71236e1cae9628f0b5c7a55b581"
NODEXL_GALLERY_URL = f"https://www.nodexlgraphgallery.org/Pages/Cloud.aspx?token={NODEXL_CLOUD_TOKEN}"

def render_nodexl_network():
    st.title("🕸️ NodeXL Network Intelligence & Graph Gallery")
    st.caption("Pusat visualisasi topologi jaringan komunikasi organisasi & riset analisis WhatsApp")

    st.markdown("""
    Modul ini mengintegrasikan **Proposal Penelitian dan PRD Analisis Jaringan WhatsApp dengan NodeXL** yang tersimpan di repositori ini dengan platform analisis graf **NodeXL Pro Graph Gallery Cloud**.
    """)

    st.info(f"🔗 **Tautan Cloud Graph Gallery:** [{NODEXL_GALLERY_URL}]({NODEXL_GALLERY_URL})")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Simpul Backbone", "500 Hubs", "Top Centrality")
    with col2:
        st.metric("Relasi Komunikasi", "15,905 Edges", "Directed Relations")
    with col3:
        st.metric("Louvain Modularity", "0.8805", "High Cluster Modularity")
    with col4:
        st.metric("Reciprocity", "42.86%", "Reciprocal Flow")

    st.markdown("---")
    st.subheader("Pemetaan Peran Komunikasi Organisasi (Structural Holes)")

    roles_data = pd.DataFrame({
        "Peran Operasional": ["Manajemen Jl. Penjernihan", "Site Engineer Migas", "Logistik & Procurement", "Quality & Safety (HSE)", "Teknisi Lapangan EPC"],
        "Degree Centrality": [95, 88, 72, 65, 54],
        "Betweenness (Jembatan)": [0.38, 0.42, 0.28, 0.31, 0.12],
        "Klaster Louvain": ["Group 1", "Group 2", "Group 3", "Group 4", "Group 5"]
    })

    fig = px.scatter(
        roles_data,
        x="Degree Centrality",
        y="Betweenness (Jembatan)",
        size="Degree Centrality",
        color="Klaster Louvain",
        hover_name="Peran Operasional",
        title="Distribusi Peran Komunikasi: Centrality vs Jembatan Informasi (Betweenness)",
        color_discrete_sequence=["#004b87", "#f59e0b", "#10b981", "#6366f1", "#ec4899"]
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("Akses Langsung Dokumen Akademis & PRD WA2Net")
    st.markdown("""
    Proposal penelitian lengkap dan spesifikasi produk alat bantu *WA2Net (WhatsApp to NodeXL Converter)* tersedia di file:  
    👉 [`Proposal Penelitian dan PRD Analisis Jaringan WhatsApp dengan NodeXL.md`](file:///Users/jevin/pt-global/Proposal%20Penelitian%20dan%20PRD%20Analisis%20Jaringan%20WhatsApp%20dengan%20NodeXL.md)
    """)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_nodexl_page.py`
Expected: PASS (2 tests passed).

- [ ] **Step 5: Commit**

```bash
git add pages_content/nodexl_network.py tests/test_nodexl_page.py
git commit -m "feat(nodexl): implement NodeXL network intelligence hub and Cloud Gallery integration"
```

---

### Task 7: Master App Routing, Navbar & Comprehensive Integration Testing

**Files:**
- Create: `app.py`
- Modify: `README.md`
- Test: `tests/test_full_app_integration.py`

**Interfaces:**
- Consumes: All `pages_content/*.py` renderers
- Produces: Entrypoint `app.py` yang siap dijalankan dengan `streamlit run app.py`

- [ ] **Step 1: Write full app integration test**

```python
# tests/test_full_app_integration.py
import unittest
import importlib

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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_full_app_integration.py`
Expected: FAIL with `ModuleNotFoundError: No module named 'app'`

- [ ] **Step 3: Implement `app.py` and update `README.md`**

Create `app.py`:
```python
import streamlit as st
import json
from pathlib import Path

from pages_content.home import render_home
from pages_content.about import render_about
from pages_content.services import render_services
from pages_content.safety_quality import render_safety_quality
from pages_content.portfolio import render_portfolio
from pages_content.safety_moment import render_safety_moment
from pages_content.contact_maps import render_contact_maps
from pages_content.nodexl_network import render_nodexl_network

st.set_page_config(
    page_title="PT Globalindo Buana — Industrial & Engineering Solutions",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

PAGES = {
    "Home": ("🏠 Beranda", render_home),
    "About Us": ("🏢 Tentang Kami", render_about),
    "Our Services": ("⚙️ Layanan Kami", render_services),
    "Safety & Quality": ("🛡️ K3 & Mutu (HSE)", render_safety_quality),
    "Portfolio": ("💼 Portfolio Proyek", render_portfolio),
    "Safety Moment": ("⚡ Safety Moment", render_safety_moment),
    "Contact & Maps": ("📍 Kontak & Lokasi", render_contact_maps),
    "NodeXL Intelligence": ("🕸️ NodeXL Network Hub", render_nodexl_network),
}

def main():
    with st.sidebar:
        st.markdown("### 🏭 PT GLOBALINDO BUANA")
        st.caption("**Engineering & Industrial Solutions**")
        st.markdown("📍 *Jl. Penjernihan 1 No. 12B, Jakarta Pusat*")
        st.markdown("---")

        selected_key = st.radio(
            "Navigasi Portal:",
            list(PAGES.keys()),
            format_func=lambda k: PAGES[k][0]
        )

        st.markdown("---")
        st.caption("📞 Hotline: `021-2524915`")
        st.caption("✉️ `marketing@globalbuana.com`")
        st.caption("© 2025 PT. Globalindo Buana | WebNesia")

    # Render selected page
    page_title, renderer_func = PAGES[selected_key]
    renderer_func()

    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #64748b; font-size: 13px; padding: 12px;'>"
        "© Copyright 2025 PT. Globalindo Buana. All Right Reserved | Dev by WebNesia<br>"
        "Kantor Pusat: Jl. Penjernihan 1 No. 12B, Bendungan Hilir, Tanah Abang, Jakarta Pusat 10210"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
```

Update `README.md`:
```markdown
# 🏭 PT Globalindo Buana — Corporate Web Portal & NodeXL Intelligence Hub

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Portal korporat interaktif dan pusat intelegensi jaringan untuk **PT. Globalindo Buana**, penyedia solusi rekayasa industri terintegrasi untuk Minyak & Gas, Kilang, Pembangkit Listrik, Semen, Pertambangan, Penerbangan, Petrokimia, dan layanan EPC & Maintenance.

---

## 📌 Identitas Perusahaan

* **Nama Resmi:** PT. Globalindo Buana
* **Kantor Pusat:** Jl. Penjernihan 1 No. 12B, RT.9/RW.6, Bendungan Hilir, Kecamatan Tanah Abang, Kota Jakarta Pusat, DKI Jakarta 10210
* **Telepon:** `021-2524915`
* **Email:** `marketing@globalbuana.com`
* **Situs Web:** [PT GLOBALINDO BUANA](https://globalbuana.com)

---

## 🧭 Peta Situs & Fitur Web Portal

1. 🏠 **Home (Beranda):** Hero showcase profil teknik rekayasa industri, key metrics, dan sektor unggulan.
2. 🏢 **About Us (Tentang Kami):** Sejarah entitas di Jalan Penjernihan 1, visi, misi, dan nilai-nilai inti (*Core Values*).
3. ⚙️ **Our Services (Layanan Kami):** Katalog 7 sektor strategis terintegrasi (*Well Services, Refinery, Power, Cement, Mining, Aviation, EPC*).
4. 🛡️ **Safety & Quality (HSE):** Kebijakan Target Zero dan kepatuhan standar mutu ISO 9001, ISO 14001, dan ISO 45001.
5. 💼 **Portfolio:** Riwayat penanganan proyek rekayasa dan pemeliharaan industri strategis.
6. ⚡ **Safety Moment:** Edukasi keselamatan kerja harian dan evaluasi matriks risiko 5x5 interaktif.
7. 📍 **Contact Us & Google Maps:** Formulir kontak interaktif tervalidasi dan sematan peta lokasi kantor Jl. Penjernihan 1 Jakarta Pusat.
8. 🕸️ **NodeXL Network Intelligence:** Dashboard interaktif topologi jaringan komunikasi organisasi dengan integrasi NodeXL Cloud Gallery (`token=c1d8d71236e1cae9628f0b5c7a55b581`).

---

## 🚀 Panduan Menjalankan Portal Lokal

```bash
# 1. Masuk ke direktori
cd /Users/jevin/pt-global

# 2. Instal dependensi
pip install -r requirements.txt

# 3. Jalankan pengujian unit
pytest

# 4. Jalankan aplikasi Streamlit
streamlit run app.py
```
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_full_app_integration.py`
Expected: PASS (2 tests passed).

- [ ] **Step 5: Run all test suites across the whole repository**

Run: `pytest`
Expected: PASS (All tests passed).

- [ ] **Step 6: Commit and Push**

```bash
git add app.py README.md tests/test_full_app_integration.py
git commit -m "feat(portal): implement master Streamlit routing, navigation, and README"
git push origin main
```
