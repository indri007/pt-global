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
