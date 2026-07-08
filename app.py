import streamlit as st
from pathlib import Path

    with open("styles.css") as f:

        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ============================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================

st.set_page_config(
    page_title="NeuroAvalia PRO",
    page_icon="🧠",
    layout="wide"
)

def carregar_css():

    with open("styles.css") as f:

        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

carregar_css()

# ============================================
# CRIA PASTAS NECESSÁRIAS
# ============================================

pastas = [
    "pacientes",
    "modelos",
    "relatorios",
    "graficos",
    "assets"
]

for pasta in pastas:
    Path(pasta).mkdir(exist_ok=True)

# ============================================
# CSS
# ============================================

st.markdown("""
<style>

.main{
    background:#f4f7fa;
}

h1{
    color:#0f766e;
}

.stButton>button{
    background:#0f766e;
    color:white;
    border-radius:10px;
    border:none;
    height:50px;
    font-size:18px;
}

.stButton>button:hover{
    background:#115e59;
}

</style>
""", unsafe_allow_html=True)

# ============================================
# TELA PRINCIPAL
# ============================================

st.title("🧠 NeuroAvalia PRO")

st.markdown("---")

st.subheader("Sistema de Avaliação Neuropsicológica")

st.write("Bem-vindo ao NeuroAvalia PRO.")

st.info(
"""
Utilize o menu lateral para acessar os módulos do sistema.

✔ Pacientes

✔ Avaliações

✔ Dashboard

✔ Relatórios

✔ Configurações
"""
)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Pacientes", len(list(Path("pacientes").glob("*.xlsx"))))

with col2:
    st.metric("Modelo", "1")

with col3:
    st.metric("Versão", "1.0")

st.success("Sistema carregado com sucesso.")
