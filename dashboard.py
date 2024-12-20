import streamlit as st
from sales_management import sales_management_page
from cost_management import cost_management_page
from sg_a_costs import sg_a_costs_page
from profit_management import profit_management_page
from cashflow_management import cashflow_management_page
from tags_and_target import tags_and_target_page  # タグと目標売上登録をインポート
from database import Database

# ページ設定
st.set_page_config(page_title="経営ダッシュボード", layout="wide")

# データベース初期化
Database.init_db()

# サイドバー
st.sidebar.header("メニュー")
menu = st.sidebar.radio("ページを選択してください", [
    "初期設定登録",  
    "売上管理", 
    "原価管理", 
    "販管費管理", 
    "利益管理", 
    "資金管理"
])

# ページ分岐
if menu == "初期設定登録":
    tags_and_target_page()  # タグと目標売上登録ページを表示
elif menu == "売上管理":
    sales_management_page()
elif menu == "原価管理":
    cost_management_page()
elif menu == "販管費管理":
    sg_a_costs_page()
elif menu == "利益管理":
    profit_management_page()
elif menu == "資金管理":
    cashflow_management_page()
