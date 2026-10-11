import streamlit as st
from datetime import datetime
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

    # Render selected page
    page_title, renderer_func = PAGES[selected_key]
    renderer_func()

    # Footer
    current_year = datetime.now().year
    st.markdown("---")
    st.markdown(
        f"<div style='text-align: center; color: #64748b; font-size: 13px; padding: 12px;'>"
        f"© Copyright {current_year} PT. Globalindo Buana. All Right Reserved | Dev by WebNesia<br>"
        f"Kantor Pusat: Jl. Penjernihan 1 No. 12B, Bendungan Hilir, Tanah Abang, Jakarta Pusat 10210"
        f"</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
