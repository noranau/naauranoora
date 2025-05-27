import streamlit as st

st.title("Hello and welcome to the Fastest Bear's World.") 
st.write(
    "Yap about Oliver Bearman with Nauranora."
)
st.image("IMG_20250517_151548_895.jpg", width=200)


st.title("The Simple App") 
st.header("Aplikasi Mengecek Nilai Genap/Ganjil") 
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap") 
else: 
  st.write(f"{angka} adalah Bilangan Ganjil")              
