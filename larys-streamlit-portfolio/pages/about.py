import streamlit as st
from streamlit_timeline import timeline

st.set_page_config(
    page_title="Home",
    layout="wide",
    initial_sidebar_state="auto"
)
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Lê o JSON
with open('timeline.json', "r") as f: 
    data = f.read()        

# Altura ajustada
timeline(data, height=700)

