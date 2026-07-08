import streamlit as st
from utils.excel import ler_cadastro, salvar_cadastro

st.set_page_config(
    page_title="Cadastro",
    page_icon="📝",
    layout="wide"
)

if "paciente" not in st.session_state:
    st.warning("Nenhum paciente selecionado.")
    st.stop()

nome_original = st.session_state["paciente"]

dados = ler_cadastro(nome_original)

st.title("📝 Editar Cadastro")

st.divider()

col1, col2 = st.columns(2)

with col1:

    nome = st.text_input("Nome", dados["Nome"])

    cpf = st.text_input("CPF", dados["CPF"])

    nascimento = st.text_input("Nascimento", dados["Nascimento"])

    sexo = st.selectbox(
        "Sexo",
        ["Masculino", "Feminino"],
        index=0 if dados["Sexo"] == "Masculino" else 1
    )

with col2:

    telefone = st.text_input("Telefone", dados["Telefone"])

    responsavel = st.text_input("Responsável", dados["Responsável"])

    escola = st.text_input("Escola", dados["Escola"])

    diagnostico = st.text_input("Diagnóstico", dados["Diagnóstico"])

st.divider()

c1, c2 = st.columns(2)

with c1:

    if st.button("💾 Salvar Cadastro", width="stretch"):

        salvar_cadastro(

            nome_original,

            {

                "Nome": nome,

                "CPF": cpf,

                "Nascimento": nascimento,

                "Sexo": sexo,

                "Telefone": telefone,

                "Responsável": responsavel,

                "Escola": escola,

                "Diagnóstico": diagnostico

            }

        )

        st.success("Cadastro atualizado com sucesso!")

with c2:

    if st.button("⬅ Voltar", width="stretch"):

        st.switch_page("pages/06_Paciente.py")