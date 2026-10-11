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
