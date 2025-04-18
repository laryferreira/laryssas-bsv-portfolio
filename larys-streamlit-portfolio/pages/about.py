import os
import streamlit as st
from streamlit_timeline import timeline

# Obtém o diretório base do projeto (um nível acima do diretório pages)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(
    page_title="Home",
    layout="wide",
    initial_sidebar_state="auto"
)

# Carregar CSS externo usando caminho absoluto
css_path = os.path.join(BASE_DIR, "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Carregar JSON usando caminho absoluto
json_path = os.path.join(BASE_DIR, "timeline.json")
with open(json_path, "r") as f:
    data = f.read()

# Altura ajustada
timeline(data, height=700)

