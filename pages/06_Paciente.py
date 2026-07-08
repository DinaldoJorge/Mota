import streamlit as st
from utils.excel import ler_cadastro

st.set_page_config(
    page_title="Paciente",
    page_icon="👤",
    layout="wide"
)

if "paciente" not in st.session_state:
    st.warning("Nenhum paciente selecionado.")
    st.stop()

nome = st.session_state["paciente"]

dados = ler_cadastro(nome)

st.title("👤 Prontuário do Paciente")

st.divider()

col1, col2 = st.columns([1,3])

with col1:

    st.image(
        "https://img.icons8.com/color/240/user.png",
        width=150
    )

with col2:

    st.subheader(dados["Nome"])

    st.write("**CPF:**", dados["CPF"])
    st.write("**Nascimento:**", dados["Nascimento"])
    st.write("**Sexo:**", dados["Sexo"])
    st.write("**Telefone:**", dados["Telefone"])
    st.write("**Responsável:**", dados["Responsável"])
    st.write("**Escola:**", dados["Escola"])
    st.write("**Diagnóstico:**", dados["Diagnóstico"])

st.divider()

c1,c2,c3,c4 = st.columns(4)

with c1:

    if st.button("📝 Cadastro",width="stretch"):

        st.switch_page("pages/07_Cadastro.py")

with c2:

    if st.button("🧠 Avaliações",width="stretch"):

        st.switch_page("pages/02_Avaliacoes.py")

with c3:

    if st.button("📊 Dashboard",width="stretch"):

        st.switch_page("pages/03_Dashboard.py")

with c4:

    if st.button("📄 Relatórios",width="stretch"):

        st.switch_page("pages/04_Relatorios.py")

st.divider()

st.subheader("Resumo")

col1,col2,col3=st.columns(3)

col1.metric("Avaliações",4)
col2.metric("Relatórios",4)
col3.metric("Status","Ativo")