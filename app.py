import streamlit as st
from pathlib import Path

# ============================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================

st.set_page_config(
    page_title="NeuroAvaliaMota",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CARREGA O CSS GLOBAL
# ============================================

def carregar_css():
    try:
        with open("styles.css", "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        st.warning("⚠️ Arquivo styles.css não encontrado.")

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
# CONTA PACIENTES
# ============================================

total_pacientes = len(list(Path("pacientes").glob("*.xlsx")))

# ============================================
# TÍTULO
# ============================================

st.title("🧠 NeuroAvaliaMota")

st.caption("Sistema Inteligente de Avaliação Neuropsicológica")

st.divider()

# ============================================
# BOAS-VINDAS
# ============================================

st.subheader("Bem-vindo ao NeuroAvaliaMota")

st.write("""
Utilize o menu lateral para navegar pelo sistema.
""")

st.info("""
### Recursos disponíveis

- 👤 Cadastro de Pacientes

- 📝 Avaliações Neuropsicológicas

- 📊 Dashboard

- 📄 Relatórios

- ⚙ Configurações

""")

st.success("✅ Sistema carregado com sucesso.")

st.divider()

# ============================================
# RODAPÉ
# ============================================

st.caption(
    "© 2026 NeuroAvaliaMota | Desenvolvido por Professor Dinaldo Jorge"
)
