import streamlit as st
from ffi import code

# コードベース
st.code(code.code, language='rust')

# 動画
vid_file = open("./public/videos/pbs.mp4", "rb")
vid_bytes = vid_file.read()
st.video(vid_bytes)