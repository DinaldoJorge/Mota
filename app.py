import streamlit as st
from pathlib import Path

# ============================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================

st.set_page_config(
    page_title="NeuroAvalia PRO",
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

st.title("🧠 NeuroAvalia PRO")

st.caption("Sistema Inteligente de Avaliação Neuropsicológica")

st.divider()

# ============================================
# DASHBOARD
# ============================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="👤 Pacientes",
        value=total_pacientes
    )

with col2:
    st.metric(
        label="📋 Modelos",
        value="1"
    )

with col3:
    st.metric(
        label="🚀 Versão",
        value="2.0"
    )

st.divider()

# ============================================
# BOAS-VINDAS
# ============================================

st.subheader("Bem-vindo ao NeuroAvalia PRO")

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
    "© 2026 NeuroAvalia PRO | Desenvolvido por Professor Dinaldo Jorge"
)
