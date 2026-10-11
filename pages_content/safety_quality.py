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
