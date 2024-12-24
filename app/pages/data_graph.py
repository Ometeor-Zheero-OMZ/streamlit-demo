import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("嫁ランキング！")

# CSVの読み込み
df = pd.read_csv("./public/csv/best_your_yome_ranking.csv", index_col="キャラクター名")

if not df.empty:
    # データフレーム
    st.dataframe(df)

    # テーブル
    st.table(df)

    # 折れ線グラフ
    st.line_chart(df)

    # 棒線グラフ
    st.bar_chart(df)
else:
    st.error("データがありません。")


df = pd.read_csv("./public/csv/per_year_ranking.csv", index_col="年")
def convert_to_numeric_with_comma(value):
    # カンマを削除して数値に変換
    if isinstance(value, str):
        value = value.replace(',', '')
    return pd.to_numeric(value, errors="coerce")

# 数値型に変換
df["2023"] = df["2023"].apply(convert_to_numeric_with_comma)


# 欠損値を削除
df = df.dropna(subset=["2023"])

if not df.empty:
    # データフレーム
    st.dataframe(df)

    # テーブル
    st.table(df)

    # 折れ線グラフ
    st.line_chart(df)

    # 棒線グラフ
    st.bar_chart(df)

    if "2023" in df.columns:
        # figure, axis
        fig, ax = plt.subplots()
        ax.plot(df.index, df["2023"])
        ax.set_title("投票数")
        ax.set_ylabel("年別")
        ax.set_xlabel("投票数")
        st.pyplot(fig)
else:
    st.error("データがありません。")

st.write(df["2023"])