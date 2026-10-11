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
