import streamlit as st

# フォーム内でテキストボックス、ボタンを配置
with st.form(key='form'):
    name = st.text_input("名前")
    email = st.text_input("メールアドレス")

    # セレクトボックス
    gender = st.selectbox("性別", ("男性", "女性", "選択しない"))

    # ラジオボタン
    age = st.radio("年齢", ("10~20", "20~30", "30~40", "40~50", "50~60", "60~"))

    # 複数選択ボタン リストで格納
    source_to_know = st.multiselect(
        "このサービスをどこで知りましたか？",
        ("Webサイト", "広告", "YouTube", "家族・友人", "それ以外")
        )

    submit_btn = st.form_submit_button("送信")
    cancel_btn = st.form_submit_button("キャンセル")

    if submit_btn:
        st.text(f"次のユーザー情報で新規登録しました： {name} | {email} | {gender} | {age} | {source_to_know}")