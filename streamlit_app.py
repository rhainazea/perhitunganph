import streamlit as st

st.title("🎈 Perhitungan pH")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
#input bilangan
n=int(input("Masukkan bilangan:"))
#nilai awal faktorial
faktorial=1
#perhitungan faktorial
for i in range(1,n+1):
    faktorial *=i
#output hasil 
print("Faktorial dari",n,"adalah",faktorial)
