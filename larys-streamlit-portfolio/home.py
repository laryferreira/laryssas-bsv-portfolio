import os
import streamlit as st
from PIL import Image
import time

# Obtém o diretório do arquivo atual
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(
    page_title="Laryssa Ferreira | Portfólio",
    layout="wide",
    initial_sidebar_state="auto"
)
st.title("I'm Laryssa Ferreira")

# Carregar CSS externo usando caminho absoluto
css_path = os.path.join(CURRENT_DIR, "assets", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

texts = [
    "curious girl that works in tech",
    "creating inclusive tech spaces",
    "exploring AI through research",
    "building a better future through code"
    ]
subtitle = st.empty()

# Carregar imagem usando caminho absoluto
image_path = os.path.join(CURRENT_DIR, "assets", "profile.png")
image = Image.open(image_path)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(image, use_container_width=True)

st.markdown("""
    <div class="button-container">
        <a href="https://www.linkedin.com/in/laryssaoliferreira/" target="_blank" class="custom-button">LinkedIn</a>
        <a href="https://docs.google.com/document/d/1QU_sA-QAw4vpcptW4G_EPXNuqMqIzJxh/edit" target="_blank" class="custom-button">Curriculum</a>
    </div>
    """, unsafe_allow_html=True)

for _ in range(1):
    for text in texts:
        subtitle.markdown(f"**{text}**")
        time.sleep(2)

st.markdown("""
    <div class="footer">
        Made with ❤️ by Laryssa Ferreira | <a href="https://github.com/laryssaoliveira" target="_blank">GitHub</a>
    </div>
    """, unsafe_allow_html=True)