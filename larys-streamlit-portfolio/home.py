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

# Cores personalizadas
bg_color = "#ffffff"
secondary_bg_color = "#ffe4ec"
text_color = "#AB4E68"
primary_color = "#D282A6"

# CSS para forçar o tema claro mesmo com base="dark"
st.markdown(f"""
    <style>
        /* Fundo geral do app */
        html, body, .stApp, [data-testid="stAppViewContainer"] {{
            background-color: {bg_color} !important;
            color: {text_color} !important;
        }}

        /* Corrige o fundo preto vindo do tema dark */
        div[class^="st-emotion-cache"] {{
            background-color: {bg_color} !important;
            color: {text_color} !important;
        }}

        /* Sidebar, header e outros blocos */
        [data-testid="stSidebar"] {{
            background-color: {secondary_bg_color} !important;
        }}

        [data-testid="stHeader"] {{
            background-color: {bg_color} !important;
        }}

        .block-container {{
            background-color: {bg_color} !important;
        }}

        /* Botões padrão */
        .stButton>button {{
            background-color: {primary_color} !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.5rem 1rem !important;
        }}

        /* Textos */
        h1, h2, h3, h4, h5, h6, p, span, label {{
            color: {text_color} !important;
        }}
    </style>
""", unsafe_allow_html=True)

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

st.markdown("""
    <div class="button-container">
        <a href="https://www.linkedin.com/in/laryssaoliferreira/" target="_blank" class="custom-button">LinkedIn</a>
        <a href="https://docs.google.com/document/d/1QU_sA-QAw4vpcptW4G_EPXNuqMqIzJxh/edit" target="_blank" class="custom-button">Curriculum</a>
    </div>
    """, unsafe_allow_html=True)

# Carregar imagem usando caminho absoluto
image_path = os.path.join(CURRENT_DIR, "assets", "profile.png")
image = Image.open(image_path)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
        <div class="profile-image-container">
    """, unsafe_allow_html=True)
    st.image(image, use_container_width=False, width=800)

for _ in range(24):
    for text in texts:
        subtitle.markdown(f"**{text}**")
        time.sleep(2)
