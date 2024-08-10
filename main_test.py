import streamlit as st
import pandas as pd

data = pd.read_csv('data.csv', sep=";")
# print(data)
for index, row in data[:10].iterrows():
    print(index)
    print (row["title"])
    print("\n")