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
    Proposal penelitian lengkap dan spesifikasi produk alat bantu *WA2Net (WhatsApp to NodeXL Converter)* tersedia di repositori:  
    👉 [`Proposal Penelitian dan PRD Analisis Jaringan WhatsApp dengan NodeXL.md`](file:///Users/jevin/pt-global/Proposal%20Penelitian%20dan%20PRD%20Analisis%20Jaringan%20WhatsApp%20dengan%20NodeXL.md)
    """)
