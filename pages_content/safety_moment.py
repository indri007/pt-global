import streamlit as st

def classify_risk(score: int) -> tuple[str, str, str]:
    """
    Mengklasifikasikan skor risiko 5x5:
    - 1-4   : RENDAH (hijau) -> st.success
    - 5-9   : SEDANG (kuning) -> st.warning
    - 10-16 : TINGGI (oranye) -> st.warning
    - 17-25 : EKSTREM (merah) -> st.error
    Mengembalikan: (callout_type, label_level, tindakan_disarankan)
    """
    if score <= 4:
        return (
            "success",
            "RENDAH",
            "Risiko dapat diterima. Lanjutkan pekerjaan dengan menerapkan SOP baku dan gunakan APD standar."
        )
    elif score <= 9:
        return (
            "warning",
            "SEDANG",
            "Diperlukan tindakan mitigasi tambahan. Lakukan peninjauan JSA (Job Safety Analysis) dan pastikan pengawasan berkala oleh Supervisor."
        )
    elif score <= 16:
        return (
            "warning",
            "TINGGI",
            "Bahaya signifikan! Pekerjaan memerlukan izin kerja khusus (Permit-to-Work), tindakan mitigasi teknis, dan pengawasan ketat sebelum dimulai."
        )
    else:
        return (
            "error",
            "EKSTREM",
            "Kondisi kritis! Hentikan atau jangan mulai pekerjaan (Stop Work Authority berlaku mutlak). Wajib modifikasi metode kerja dan evaluasi ulang hingga tingkat risiko turun."
        )


def render_safety_moment():
    st.title("⚡ Safety Moment & Edukasi K3 Harian")
    st.caption("Materi panduan keselamatan kerja sebelum memulai shift harian")

    topic = st.selectbox(
        "Pilih Topik Safety Moment Hari Ini:",
        ["Bekerja di Ketinggian (Working at Heights)", "Izin Kerja Panas (Hot Work Permit)", "Ruang Terbatas (Confined Space)", "Alat Pelindung Diri (PPE)"]
    )

    if topic == "Bekerja di Ketinggian (Working at Heights)":
        st.warning("⚠️ **Aturan Emas:** Gunakan Full Body Harness dengan double lanyard berpengait besar yang tertambat pada anchor point kokoh pada ketinggian > 1.8 meter.")
        st.caption("📋 **Rujukan Regulasi:** Permenaker No. 9 Tahun 2016 tentang Keselamatan dan Kesehatan Kerja dalam Pekerjaan pada Ketinggian.")
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

    callout_type, level_name, action_rec = classify_risk(score)
    badge = "🟢" if level_name == "RENDAH" else ("🟡" if level_name == "SEDANG" else ("🟠" if level_name == "TINGGI" else "🔴"))
    msg = f"{badge} **Skor Risiko: {score} — {level_name}**\n\n**Tindakan yang Disarankan:** {action_rec}"

    if callout_type == "success":
        st.success(msg)
    elif callout_type == "warning":
        st.warning(msg)
    else:
        st.error(msg)
