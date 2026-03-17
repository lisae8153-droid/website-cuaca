            import streamlit as st
import random

st.set_page_config(
    page_title="Website Cuaca",
    page_icon="🌦️",
    layout="centered"
)

st.title("🌦️ Website Cuaca Sederhana")
st.write("Masukkan nama kota untuk melihat informasi cuaca.")

kota = st.text_input("📍 Masukkan Nama Kota:")

kondisi_cuaca = [
    "Cerah ☀️",
    "Berawan ☁️",
    "Hujan 🌧️",
    "Mendung 🌥️",
    "Badai ⛈️"
]

if st.button("🔍 Cek Cuaca"):
    if kota.strip() == "":
        st.warning("⚠️ Silakan masukkan nama kota terlebih dahulu!")
    else:
        suhu = random.randint(20, 35)
        kelembapan = random.randint(50, 95)
        kondisi = random.choice(kondisi_cuaca)
        angin = random.randint(5, 30)

        st.success(f"📍 Cuaca di {kota}")
        st.write(f"**Kondisi:** {kondisi}")
        st.write(f"**Suhu:** {suhu}°C")
        st.write(f"**Kelembapan:** {kelembapan}%")
        st.write(f"**Kecepatan Angin:** {angin} km/jam")

st.write("---")
st.caption("Dibuat dengan Python + Streamlit")
