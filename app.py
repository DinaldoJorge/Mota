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
# TOTAL DE PACIENTES
# ============================================

total_pacientes = len(list(Path("pacientes").glob("*.xlsx")))

# ============================================
# CABEÇALHO
# ============================================

st.markdown("""
<div style="text-align:center;padding-top:15px;padding-bottom:10px;">
<h1 style="margin-bottom:0px;">🧠 NeuroAvaliaMota</h1>
<p style="font-size:18px;color:#9ca3af;">
Sistema Inteligente de Avaliação Neuropsicológica
</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ============================================
# CARD PRINCIPAL
# ============================================

st.markdown(f"""
<div style="
background:#1e293b;
padding:20px;
border-radius:18px;
border:1px solid #334155;
text-align:center;
margin-bottom:20px;
">

<h3 style="margin-bottom:10px;">👥 Pacientes Cadastrados</h3>

<h1 style="font-size:50px;color:#4ade80;margin-top:5px;">
{total_pacientes}
</h1>

</div>
""", unsafe_allow_html=True)

# ============================================
# BOAS VINDAS
# ============================================

st.subheader("👋 Bem-vindo!")

st.write(
"""
Utilize o menu lateral para acessar rapidamente todas as funcionalidades do sistema.
"""
)

# ============================================
# RECURSOS
# ============================================

st.info("""
### Recursos Disponíveis

👤 Cadastro de Pacientes

📝 Avaliações Neuropsicológicas

📊 Dashboard Estatístico

📄 Relatórios Automáticos

⚙️ Configurações do Sistema

💾 Backup dos Pacientes
""")

# ============================================
# STATUS
# ============================================

st.success("✅ Sistema pronto para utilização.")

st.divider()

# ============================================
# RODAPÉ
# ============================================

st.markdown("""
<div style="text-align:center;color:gray;font-size:14px;padding:15px;">
© 2026 <b>NeuroAvaliaMota PRO</b><br>
Desenvolvido por <b>Professor Dinaldo Jorge</b>
</div>
""", unsafe_allow_html=True)
