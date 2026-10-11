import streamlit as st
import json
from pathlib import Path
from pages_content.contact_service import save_contact_submission

ROOT = Path(__file__).resolve().parent.parent

def render_contact_maps():
    with open(ROOT / "data" / "company_profile.json", "r", encoding="utf-8") as f:
        profile = json.load(f)

    st.title("📍 Hubungi Kami & Lokasi Kantor Pusat")
    st.caption("Kantor Pusat PT Globalindo Buana — Jalan Penjernihan 1, Jakarta Pusat")

    col_info, col_form = st.columns([1, 1.2])

    with col_info:
        st.subheader("Informasi Kontak Resmi")
        st.markdown(f"""
        🏢 **{profile['name']}**  
        📍 **Alamat:** {profile['address']}  
        📮 **Kode Pos:** {profile['postal_code']}  
        📞 **Telepon:** `{profile['phone']}`  
        ✉️ **Email:** `{profile['email']}`  
        🌐 **Website:** [{profile['website']}]({profile['website']})
        """)
        st.markdown("---")
        st.markdown("**Media Sosial Resmi:**")
        soc = profile.get("social_media", {})
        st.markdown(f"• [Facebook]({soc.get('facebook')}) | [Instagram]({soc.get('instagram')}) | [LinkedIn]({soc.get('linkedin')}) | [YouTube]({soc.get('youtube')})")

    with col_form:
        st.subheader("Kirimkan Pesan / Inquiry Proyek")
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Nama Lengkap (*)")
            email = st.text_input("Email Perusahaan (*)")
            phone = st.text_input("Nomor Telepon / WhatsApp (*)")
            subject = st.text_input("Subjek Permintaan (*)")
            message = st.text_area("Pesan / Keterangan Kebutuhan Teknis (*)", height=120)
            submitted = st.form_submit_button("🚀 Kirim Pesan Sekarang")

            if submitted:
                res = save_contact_submission(name, email, phone, subject, message)
                if res.get("success"):
                    st.success(f"✅ {res.get('message')}")
                else:
                    st.error(f"⚠️ {res.get('message')}")

    st.markdown("---")
    st.subheader("Peta Interaktif Kantor Pusat (Jl. Penjernihan 1 Jakarta Pusat)")
    
    # Embed Google Maps Iframe (Bendungan Hilir, Tanah Abang, Jakarta Pusat 10210)
    map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3966.452668383818!2d106.80931557499026!3d-6.203867693783982!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e69f697424ea4b1%3A0xe543ec682c3f81e!2sJl.%20Penjernihan%20I%20No.12B%2C%20RT.9%2FRW.6%2C%20Bend.%20Hilir%2C%20Kecamatan%20Tanah%20Abang%2C%20Kota%20Jakarta%20Pusat%2C%20Daerah%20Khusus%20Ibukota%20Jakarta%2010210!5e0!3m2!1sid!2sid!4v1700000000000!5m2!1sid!2sid"
    
    st.components.v1.iframe(map_url, height=380, scrolling=False)
