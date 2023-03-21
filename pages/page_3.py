#  csv読み込み用
import pandas as pd

#  import matplotlib.pyplot as plt

import streamlit as st

#  データ分析菅れ
df = pd.read_csv('./data/data.csv', index_col='a')
#  st.dataframe(df)
#  st.table(df)
st.line_chart(df)
st.bar_chart(df['2021'])

#  matplotlib
#  fig, ax = plt.subplots()
#  ax.plot(df.index, df['2021'])
#  ax.set_title('matplotlib graph')
#  st.pyplot(fig)
