import streamlit as st

st.set_page_config(page_title="European Excise Observatory", layout="wide")

with open("index.html", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=2000, scrolling=True)
