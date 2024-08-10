import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png', use_column_width=True)

with col2:
    st.title("Francesco Zerbato")
    content = """ Francesco e' un campione"""

    st.info(content)
st.write("This content follows a single-column format. Please notice it")

data = pd.read_csv('data.csv', sep=";")

col3, col4 = st.columns(2)

with col3:
    for index, row in data[:10].iterrows():
        st.write(row["title"])

with col4:
    for index, row in data[10:].iterrows():
        st.write(row["title"])

