import streamlit as st
import pandas as pd
from database import Database

def profit_management_page():
    st.header("利益管理")

    # データ取得
    sales_data = Database.fetch_data("SELECT revenue FROM sales")
    cost_data = Database.fetch_data("SELECT cost FROM costs")
    sg_a_cost_data = Database.fetch_data("SELECT amount FROM sg_a_costs")

    total_revenue = sum([x[0] for x in sales_data])
    total_cost = sum([x[0] for x in cost_data])
    total_sg_a_cost = sum([x[0] for x in sg_a_cost_data])
    profit = total_revenue - (total_cost + total_sg_a_cost)

    # 利益表示
    st.metric("総売上", f"{total_revenue}円")
    st.metric("総原価", f"{total_cost}円")
    st.metric("販管費", f"{total_sg_a_cost}円")
    st.metric("利益", f"{profit}円")

    # グラフ
    profit_df = pd.DataFrame({
        "項目": ["総売上", "総原価", "販管費", "利益"],
        "金額": [total_revenue, total_cost, total_sg_a_cost, profit]
    })
    st.bar_chart(profit_df.set_index("項目"))

    # SQLダウンロード
    if st.button("SQLファイルをダウンロード"):
        with open("profit_data.sql", "w") as f:
            for line in Database.fetch_data("SELECT * FROM profits"):
                f.write(str(line) + "\n")
        st.success("SQLファイルをダウンロードしました！")
