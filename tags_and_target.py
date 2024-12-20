import streamlit as st
from database import Database

def tags_and_target_page():
    st.header("タグと目標売上の登録")

    # タグ登録フォーム
    st.subheader("タグ登録")
    with st.form("tag_form"):
        new_tag = st.text_input("新しいタグを登録")
        submitted_tag = st.form_submit_button("登録")
        if submitted_tag and new_tag:
            Database.execute_query("INSERT INTO tags (tag_name) VALUES (?)", (new_tag,))
            st.success(f"タグ '{new_tag}' を登録しました！")

    # 登録済みタグ表示
    tags_data = Database.fetch_data("SELECT tag_name FROM tags")
    tags = [row[0] for row in tags_data]
    if tags:
        st.subheader("登録済みタグ")
        st.write(", ".join(tags))
    else:
        st.info("まだタグが登録されていません。")

    # 目標売上登録フォーム
    st.subheader("目標売上登録")
    with st.form("target_form"):
        target_revenue = st.number_input("年間目標売上高（千円単位）", min_value=0, step=100)
        submitted_target = st.form_submit_button("登録")
        if submitted_target:
            # 既存の目標売上を削除して新規登録
            Database.execute_query("DELETE FROM target_revenue")
            Database.execute_query("INSERT INTO target_revenue (amount) VALUES (?)", (target_revenue,))
            st.success(f"年間目標売上高を {target_revenue:,} 千円に設定しました！")

    # 登録済み目標売上表示
    target_data = Database.fetch_data("SELECT amount FROM target_revenue")
    if target_data:
        st.subheader("登録済み目標売上")
        st.write(f"{target_data[0][0]:,} 千円")
    else:
        st.info("まだ目標売上が登録されていません。")
