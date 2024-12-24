import streamlit as st

st.title("好きなポケモンを選んでくれ。")

left, center, right = st.columns(3)

with left:
    # st.subheader("ほのお")
    st.markdown("<h3 style='text-align: center; color: red;'>ほのお</h3>", unsafe_allow_html=True)
    st.image("https://pokemon-irasuto-taizen.com/wp-content/uploads/2021/03/0004.png", caption="ヒトカゲ")

with center:
    # st.subheader("みず")
    st.markdown("<h3 style='text-align: center; color: blue;'>みず</h3>", unsafe_allow_html=True)
    st.image("https://pokemon-irasuto-taizen.com/wp-content/uploads/2021/03/0007.png", caption="ゼニガメ")

with right:
    # st.subheader("くさ")
    st.markdown("<h3 style='text-align: center; color: green;'>くさ</h3>", unsafe_allow_html=True)
    st.image("https://pokemon-irasuto-taizen.com/wp-content/uploads/2021/03/0001.png", caption="フシギダネ")

