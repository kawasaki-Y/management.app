import streamlit as st
import pandas as pd
import altair as alt
from database import Database

def cost_management_page():
    st.header("原価管理")

    # 原価登録フォーム
    with st.form("cost_form"):
        project = st.text_input("案件名")
        cost = st.number_input("原価（円）", min_value=0, step=1000)
        date = st.date_input("日付")
        submitted = st.form_submit_button("登録")
        if submitted:
            Database.execute_query(
                "INSERT INTO costs (project, cost, date) VALUES (?, ?, ?)",
                (project, cost, str(date))
            )
            st.success("原価を登録しました！")

    # データ表示
    data = Database.fetch_data("SELECT project, cost, date FROM costs")
    df = pd.DataFrame(data, columns=["案件名", "原価", "日付"])
    if not df.empty:
        st.dataframe(df)

        # グラフ表示
        chart = alt.Chart(df).mark_bar(color="#ff7f7f").encode(
            x="案件名:N",
            y="原価:Q",
            tooltip=["案件名", "原価", "日付"]
        )
        st.altair_chart(chart, use_container_width=True)

        # 集計
        total_cost = df["原価"].sum()
        st.metric("総原価", f"{total_cost}円")

    # SQLダウンロード
    if st.button("SQLファイルをダウンロード"):
        with open("cost_data.sql", "w") as f:
            for line in Database.fetch_data("SELECT * FROM costs"):
                f.write(str(line) + "\n")
        st.success("SQLファイルをダウンロードしました！")
