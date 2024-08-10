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

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

