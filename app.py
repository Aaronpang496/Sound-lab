from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Sound Lab", page_icon="🔊", layout="wide")

st.markdown("<style>.block-container {padding-top: 1rem; padding-bottom: 0;}</style>", unsafe_allow_html=True)

try:
    html = Path(__file__).with_name("sound_lab.html").read_text(encoding="utf-8")
    components.html(html, height=800, scrolling=False)
except FileNotFoundError:
    st.error("Error: sound_lab.html not found.")
