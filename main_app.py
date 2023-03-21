import datetime

import streamlit as st
from PIL import Image
#  csv読み込み用
import pandas as pd

import matplotlib.pyplot as plt


st.title('さぶーアプリ')
st.caption('これはさぷーの動画用のテストアプリです')
image = Image.open('./data/picture.png')
st.image(image, width=200)
