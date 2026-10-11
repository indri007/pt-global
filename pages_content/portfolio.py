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
