# 🏭 PT Globalindo Buana — Corporate Web Portal & NodeXL Intelligence Hub

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)]()

Portal korporat interaktif dan pusat intelegensi jaringan untuk **PT. Globalindo Buana**, penyedia solusi rekayasa industri terintegrasi untuk Minyak & Gas, Kilang, Pembangkit Listrik, Semen, Pertambangan, Penerbangan, Petrokimia, dan layanan EPC & Maintenance.

---

## 📌 Identitas Perusahaan

* **Nama Resmi:** PT. Globalindo Buana
* **Kantor Pusat:** Jl. Penjernihan 1 No. 12B, RT.9/RW.6, Bendungan Hilir, Kecamatan Tanah Abang, Kota Jakarta Pusat, DKI Jakarta 10210
* **Telepon:** `021-2524915`
* **Email:** `marketing@globalbuana.com`
* **Situs Web:** [PT GLOBALINDO BUANA](https://globalbuana.com)
* **Hak Cipta:** © Copyright 2025 PT. Globalindo Buana. All Right Reserved | Dev by WebNesia

---

## 🧭 Peta Situs & Fitur Web Portal

1. 🏠 **Home (Beranda):** Hero showcase profil teknik rekayasa industri, key metrics, dan sektor unggulan.
2. 🏢 **About Us (Tentang Kami):** Sejarah entitas di Jalan Penjernihan 1, visi, misi, dan nilai-nilai inti (*Core Values*).
3. ⚙️ **Our Services (Layanan Kami):** Katalog 7 sektor strategis terintegrasi (*Well Services, Refinery, Power, Cement, Mining, Aviation, EPC*).
4. 🛡️ **Safety & Quality (HSE):** Kebijakan Target Zero dan kepatuhan standar mutu ISO 9001, ISO 14001, dan ISO 45001.
5. 💼 **Portfolio:** Riwayat penanganan proyek rekayasa dan pemeliharaan industri strategis dengan catatan Zero LTI.
6. ⚡ **Safety Moment:** Edukasi keselamatan kerja harian dan evaluasi matriks risiko 5x5 interaktif.
7. 📍 **Contact Us & Google Maps:** Formulir kontak interaktif tervalidasi dan sematan peta lokasi kantor Jl. Penjernihan 1 Jakarta Pusat.
8. 🕸️ **NodeXL Network Intelligence:** Dashboard interaktif topologi jaringan komunikasi organisasi dengan integrasi NodeXL Cloud Gallery (`token=c1d8d71236e1cae9628f0b5c7a55b581`).

---

## 📚 Riset Akademis & Spesifikasi WA2Net

Repositori ini juga menyertakan dokumen riset akademik lengkap:
* 📄 [`Proposal Penelitian dan PRD Analisis Jaringan WhatsApp dengan NodeXL.md`](./Proposal%20Penelitian%20dan%20PRD%20Analisis%20Jaringan%20WhatsApp%20dengan%20NodeXL.md) — Mengkaji struktur jaringan komunikasi organisasi, structural holes, modal sosial, dan spesifikasi teknis *WA2Net Converter*.

---

## 🚀 Panduan Menjalankan Portal Lokal

```bash
# 1. Masuk ke direktori repositori
cd /Users/jevin/pt-global

# 2. Instal dependensi
pip install -r requirements.txt

# 3. Jalankan rangkaian pengujian unit (Pytest)
pytest

# 4. Jalankan aplikasi Streamlit
streamlit run app.py
```

---

## 🏗️ Struktur Direktori

```
pt-global/
├── .streamlit/
│   └── config.toml                  # Konfigurasi tema industrial Streamlit
├── data/
│   ├── company_profile.json         # Data profil korporat, alamat Jl. Penjernihan 1, kontak
│   ├── services.json                # Katalog 7 sektor industri strategis
│   └── contact_submissions.csv      # Penyimpanan log formulir kontak masuk
├── pages_content/
│   ├── __init__.py
│   ├── about.py                     # Modul profil, visi, misi, nilai inti
│   ├── contact_maps.py              # Modul formulir kontak & iframe Google Maps
│   ├── contact_service.py           # Validasi & pemrosesan form kontak
│   ├── home.py                      # Modul Beranda & metrik utama
│   ├── nodexl_network.py            # Modul integrasi NodeXL Cloud Gallery
│   ├── portfolio.py                 # Modul rekam jejak proyek industri
│   ├── safety_moment.py             # Modul Safety Moment harian & matriks risiko
│   ├── safety_quality.py            # Modul K3/HSE (ISO 9001/14001/45001)
│   └── services.py                  # Modul katalog rinci 7 sektor industri
├── tests/
│   ├── test_contact_page_render.py  # Test renderer halaman kontak
│   ├── test_contact_workflow.py     # Test validasi & persistensi data form
│   ├── test_core_pages.py           # Test renderer Beranda, Tentang, Layanan
│   ├── test_data_integrity.py       # Test keutuhan data profil & layanan
│   ├── test_full_app_integration.py # Test integrasi router master app.py
│   ├── test_nodexl_page.py          # Test renderer NodeXL & integritas token
│   └── test_safety_portfolio.py     # Test renderer K3, Portofolio, Safety Moment
├── app.py                           # Master Streamlit entrypoint
├── requirements.txt                 # Dependensi Python
└── README.md                        # Dokumentasi komprehensif
```