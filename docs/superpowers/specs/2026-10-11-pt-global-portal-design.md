# Design Specification: Web Portal PT Globalindo Buana & NodeXL Intelligence Hub

**Tanggal:** 2026-10-11  
**Penyusun:** Antigravity AI Pair Programmer & Indri Kartikasari  
**Status:** Validated & Approved  
**Repositori Target:** `https://github.com/indri007/pt-global` (`/Users/jevin/pt-global`)

---

## 1. Ringkasan Eksekutif & Tujuan Produk

Web Portal PT Globalindo Buana adalah aplikasi korporat interaktif berbasis **Python Streamlit** yang dirancang untuk mempresentasikan profil kredibilitas, 7 sektor solusi rekayasa terintegrasi, komitmen keselamatan kerja (HSE/K3), serta pusat visualisasi analisis jaringan komunikasi (NodeXL Graph Gallery).

Aplikasi ini mengintegrasikan seluruh struktur *sitemap* resmi perusahaan dengan lokasi kantor pusat di **Jl. Penjernihan 1 No. 12B, Bendungan Hilir, Jakarta Pusat**, sekaligus menghubungkan repositori ini dengan riset analisis jaringan WhatsApp (NodeXL Cloud Gallery).

---

## 2. Identitas Perusahaan & Data Kontak Resmi

* **Nama Perusahaan:** PT Globalindo Buana
* **Alamat Kantor Pusat:** Jl. Penjernihan 1 No. 12B, RT.9/RW.6, Bendungan Hilir, Kecamatan Tanah Abang, Kota Jakarta Pusat, DKI Jakarta 10210
* **Telepon:** 021-2524915
* **Email:** `marketing@globalbuana.com`
* **Situs Web:** PT GLOBALINDO BUANA
* **Bidang Usaha Utama:** Penyedia solusi terintegrasi untuk Minyak & Gas, Kilang, Pembangkit Listrik, Semen, Pertambangan, Penerbangan, Petrokimia (layanan *Well Services*, EPC, dan *Industrial Maintenance*).
* **Hak Cipta:** `© Copyright 2025 PT. Globalindo Buana. All Right Reserved | Dev by WebNesia`

---

## 3. Arsitektur Sistem & Struktur Direktori

Sistem dirancang modular dengan pemisahan antara data terstruktur (JSON/CSV) dan modul penampil antarmuka (Python Streamlit):

```
pt-global/
├── app.py                                   # Entrypoint aplikasi, konfigurasi halaman, & router menu
├── requirements.txt                         # Dependensi pustaka Python
├── README.md                                # Dokumentasi profil perusahaan dan panduan instalasi
├── .streamlit/
│   └── config.toml                          # Tema visual korporat (Industrial Navy & Clean Slate)
├── data/
│   ├── company_profile.json                 # Data profil, kontak, visi-misi, nilai inti, legalitas
│   ├── services.json                        # Katalog 7 sektor solusi industri dan detail layanan
│   └── contact_submissions.csv             # Arsip pesan masuk dari formulir kontak
├── pages_content/                           # Modul renderer per halaman sitemap
│   ├── __init__.py
│   ├── home.py                              # Beranda: Hero banner, ringkasan keunggulan, metrik kunci
│   ├── about.py                             # Tentang Kami: Sejarah, visi, misi, legalitas Jl. Penjernihan 1
│   ├── services.py                          # Layanan: Well services, EPC, maintenance, kilang, pembangkit
│   ├── safety_quality.py                    # HSE: Kebijakan Target Zero, sertifikasi ISO (9001, 14001, 45001)
│   ├── portfolio.py                         # Portfolio: Galeri rekam jejak proyek rekayasa industri
│   ├── safety_moment.py                     # Safety Moment: Edukasi K3 harian, toolbox checklist, matriks risiko
│   ├── contact_maps.py                      # Kontak & Peta: Form interaktif + Peta lokasi Jl. Penjernihan 1
│   └── nodexl_network.py                    # NodeXL Intelligence: Visualisasi jaringan komunikasi & Cloud Gallery
└── tests/
    ├── __init__.py
    └── test_portal.py                       # Unit test otomatis integritas data, form, & rendering modul
```

---

## 4. Spesifikasi Modul Halaman (Sitemap Resmi)

### 4.1 Home (Beranda)
* **Hero Section:** Banner industri bertema teknik rekayasa terpadu dengan headline *"PT Globalindo Buana — Integrated Industrial Engineering Solutions"*.
* **Highlight Sektor:** Grid kartu interaktif untuk 7 sektor utama.
* **Key Performance Indicators (KPI):**
  * 7 Sektor Industri Strategis
  * Standar Keselamatan Kerja *Zero Lost Time Incident*
  * Dukungan Teknis & Layanan Darurat 24/7
  * Kantor Pusat Strategis di Segitiga Bisnis Jakarta Pusat
* **Call-to-Action (CTA):** Tombol cepat menuju katalog layanan dan pengiriman pesan.

### 4.2 About Us (Tentang Kami)
* **Profil Entitas:** Pengenalan PT Globalindo Buana yang berkedudukan di Jl. Penjernihan 1 No. 12B, Bendungan Hilir, Tanah Abang, Jakarta Pusat.
* **Visi:** Menjadi penyedia solusi rekayasa dan pemeliharaan industri terkemuka di Indonesia yang diakui atas keunggulan operasional, kehandalan teknis, dan kepatuhan keselamatan tertinggi.
* **Misi:** Memberikan layanan rekayasa industri bermutu tinggi, menerapkan standar keselamatan kerja tanpa kompromi, dan membangun kemitraan strategis jangka panjang.
* **Nilai-Nilai Inti:** *Safety First*, *Integrity*, *Technical Excellence*, *Customer Commitment*, dan *Continuous Improvement*.

### 4.3 Our Services (Layanan Kami)
Katalog mendalam untuk 7 sektor industri dengan deskripsi teknis dan lingkup pekerjaan:
1. **Minyak & Gas (Oil & Gas):** *Well Services, Well Intervention, Wellhead Maintenance, High Pressure Pumping*.
2. **Kilang & Petrokimia (Refinery & Petrochemical):** *Plant Turnaround, Heat Exchanger Overhaul, Piping Fabrication, Storage Tank Inspection*.
3. **Pembangkit Listrik (Power Generation):** *Turbine Overhaul, Boiler Maintenance, Balance of Plant (BOP) Services, Electrical & Instrumentation*.
4. **Industri Semen (Cement Industry):** *Kiln Drive Alignment, Heavy Mechanical Maintenance, Material Handling Systems*.
5. **Pertambangan (Mining Sector):** *Crushing Plant Support, Heavy Structural Repair, Slurry Pumping & Piping Solutions*.
6. **Penerbangan (Aviation Support):** *Aviation Fuel Handling Systems, Ground Support Equipment Maintenance*.
7. **EPC & Maintenance Terintegrasi:** Layanan terpadu *Engineering, Procurement, Construction*, dan *Long-Term Maintenance Contracts*.

### 4.4 Safety & Quality (HSE / K3 & Mutu)
* **Kebijakan K3LL (HSE Policy):** Komitmen *Target Zero* (Nol Insiden Kerja, Nol Penyakit Akibat Kerja, Nol Dampak Lingkungan).
* **Kepatuhan Sertifikasi:**
  * ISO 9001: Sistem Manajemen Mutu (*Quality Management System*)
  * ISO 14001: Sistem Manajemen Lingkungan (*Environmental Management System*)
  * ISO 45001: Sistem Manajemen Keselamatan dan Kesehatan Kerja (*Occupational Health & Safety*)
* **Prosedur HSE Lapangan:** *Stop Work Authority (SWA)* bagi seluruh personil di lapangan.

### 4.5 Portfolio & Proyek
* Showcase proyek industri mencakup:
  * Proyek Pemeliharaan Fasilitas Sumur Minyak Lepas Pantai & Darat (*Well Services*)
  * Proyek Turnaround Unit Kilang Minyak Nasional
  * Pemeliharaan Sistem Boiler & Turbin Pembangkit Listrik Jawa-Sumatera
  * Instalasi Jalur Pemipaan Tekanan Tinggi Pabrik Petrokimia

### 4.6 Safety Moment & Edukasi K3
* Modul interaktif keselamatan kerja harian:
  * Panduan topik *Toolbox Meeting* harian (*Working at Heights, Hot Work, Confined Space Entry, PPE Inspection*)
  * Matriks Penilaian Risiko (*Risk Assessment Matrix*) 5x5 interaktif
  * Prosedur Izin Kerja Aman (*Permit to Work System*)

### 4.7 Hubungi Kami & Peta Interaktif
* **Formulir Kontak Berfungsi Penuh:**
  * Input: *Nama Lengkap*, *Email Perusahaan*, *Nomor Telepon*, *Subjek Permintaan*, *Pesan Detail*.
  * Validasi: Pemeriksaan format email dan isian wajib.
  * Penyimpanan: Otomatis dicatat ke file lokal `data/contact_submissions.csv`.
* **Detail Kontak Resmi:**
  * Alamat: Jl. Penjernihan 1 No. 12B, Bendungan Hilir, Tanah Abang, Jakarta Pusat 10210
  * Telepon: `021-2524915`
  * Email: `marketing@globalbuana.com`
* **Peta Interaktif:** Sematan koordinat Google Maps interaktif yang mengarah langsung ke kantor pusat di Jl. Penjernihan 1 Jakarta Pusat.
* **Tautan Media Sosial:** Facebook, Instagram, LinkedIn, YouTube.

### 4.8 NodeXL Network Intelligence Hub
* **Koneksi NodeXL Cloud Graph Gallery:**
  * Token Integrasi Resmi: `c1d8d71236e1cae9628f0b5c7a55b581`
  * Tautan Langsung: `https://www.nodexlgraphgallery.org/Pages/Cloud.aspx?token=c1d8d71236e1cae9628f0b5c7a55b581`
* **Analisis Graf Komunikasi Organisasi:**
  * Penjelasan struktur jaringan koordinasi operasional (manajemen pusat Jl. Penjernihan vs tim lapangan teknis).
  * Metrik interaktif: *Degree Centrality*, *Betweenness Centrality* (jembatan informasi), *Closeness*, dan deteksi komunitas algoritma Louvain.

---

## 5. Tema Visual & Styling UI

* **Warna Primer:** Deep Industrial Navy (`#0a2540` / `#004b87`)
* **Warna Aksen:** Safety Amber / Gold (`#f59e0b` / `#d97706`)
* **Warna Latar:** Clean Slate (`#f8fafc` / `#ffffff`)
* **Tipografi:** Sans-serif modern dan bersih dengan sistem kartu responsif (*CSS styling injection* pada Streamlit).

---

## 6. Strategi Pengujian (Testing & Verification)

Pengujian otomatis dengan `pytest` di `tests/test_portal.py` mencakup:
1. `test_company_data_integrity`: Memastikan data profil, alamat Jl. Penjernihan 1, dan kontak termuat tanpa kegagalan.
2. `test_services_catalog`: Memverifikasi ketersediaan 7 sektor industri lengkap dengan detail deskripsinya.
3. `test_contact_submission_workflow`: Memverifikasi alur validasi dan pencatatan formulir kontak ke `data/contact_submissions.csv`.
4. `test_page_renderers`: Memverifikasi seluruh modul halaman di folder `pages_content/` dapat diimpor dan dieksekusi tanpa sintaks error.
5. `test_nodexl_token_configuration`: Memverifikasi token NodeXL Cloud `c1d8d71236e1cae9628f0b5c7a55b581` terkonfigurasi dengan benar.
