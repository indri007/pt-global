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
