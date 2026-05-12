import streamlit as st

st.title("🎈 Perhitungan pH")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# Input bilangan
angka = st.number_input("Masukkan bilangan bulat positif",min_value=0,step=1)
# Tombol hitung
if st.button("Hitung Faktorial"):
    faktorial = 1
# Perhitungan faktorial
for i in range(1, angka + 1):
    faktorial *= i
# Menampilkan hasil
st.success(f"Faktorial dari {angka} adalah {faktorial}")
