import datetime

import streamlit as st

with st.form(key='profile_form'):
    # 　テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')
    # 　セレクトボックス
    age_category = st.selectbox(
        '年齢層',
        ('子ども（１８歳未満）', '大人（１８歳以上）')
    )
    #  ラジオボタン
    age_category2 = st.radio(
        '年齢層',
        ('子ども（１８歳未満）2', '大人（１８歳以上）2')
    )

    # 　　複数選択
    hobby = st.multiselect(
        '趣味',
        ('スポーツ', '読書', '釣り')
    )

    #  チェックボックス

    mail_subscribe = st.checkbox('メールマガジンを購読する')
    #  スライダー
    height = st.slider('身長', min_value=110, max_value=210)

    #  日付
    start_date = st.date_input(
        '開始日',
        datetime.date(2023, 3, 21)
    )

    #  カラーピッカー
    color = st.color_picker('テーマカラー', '#00f900')

    #   ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'ようこそ!{name}さん!{address}に書籍をおくりました!')
        st.text(f'年齢層：{age_category}')
        st.text(f'年齢層：{age_category2}')
        st.text(f'趣味:{", ".join(hobby)}')
    #  Streamlit inputウィジェット ▶︎https://docs.streamlit.io/library/api-reference/
    #  charts#chart-elements
    #  Streamlit グラフウィジェット ▶︎ https://docs.streamlit.io/library/api-reference/
    #  widgets#input-widgets
