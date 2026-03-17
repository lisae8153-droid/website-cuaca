# website-cimport streamlit as st
import random

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Website Cuaca",
    page_icon="🌦️",
    layout="centered"
)

# =========================
# STYLE CSS SEDERHANA
# =========================
st.markdown("""
    <style>
    .main {
        background-color: #eaf6ff;
    }
    .judul {
        text-align: center;
        color: #1f4e79;
        font-size: 36px;
        font-weight: bold;
    }
    .subjudul {
        text-align: center;
        color: #4a4a4a;
        font-size: 18px;
        margin-bottom: 20px;
    }
    .hasil-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# =========================
# JUDUL
# =========================
st.markdown('<div class="judul">🌦️ Website Cuaca Sederhana</div>', unsafe_allow_html=True)
st.markdown('<div class="subjudul">Masukkan nama kota untuk melihat informasi cuaca</div>', unsafe_allow_html=True)

# =========================
# INPUT KOTA
# =========================
kota = st.text_input("📍 Masukkan Nama Kota:")

# =========================
# DATA CUACA DUMMY
# =========================
kondisi_cuaca = [
    "Cerah ☀️",
    "Berawan ☁️",
    "Hujan 🌧️",
    "Mendung 🌥️",
    "Badai ⛈️"
]

# =========================
# TOMBOL CEK CUACA
# =========================
if st.button("🔍 Cek Cuaca"):
    if kota.strip() == "":
        st.warning("⚠️ Silakan masukkan nama kota terlebih dahulu!")
    else:
        suhu = random.randint(20, 35)
        kelembapan = random.randint(50, 95)
        kondisi = random.choice(kondisi_cuaca)
        angin = random.randint(5, 30)

        st.markdown(f"""
        <div class="hasil-box">
            <h3>📍 Cuaca di {kota}</h3>
            <p><b>Kondisi:</b> {kondisi}</p>
            <p><b>Suhu:</b> {suhu}°C</p>
            <p><b>Kelembapan:</b> {kelembapan}%</p>
            <p><b>Kecepatan Angin:</b> {angin} km/jam</p>
        </div>
        """, unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("Dibuat dengan Python + Streamlit")uaca
