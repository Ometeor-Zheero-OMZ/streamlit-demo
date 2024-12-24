import streamlit as st
from PIL import Image

st.title("Datarify")
st.caption("身の回りの全てをデータ化しましょう！")

st.text("このような画像も視覚的データを抽出できます。")
img = Image.open("./public/images/ichigo-mashimaro.jpg")
st.image(img, width=300)