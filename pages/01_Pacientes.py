import streamlit as st
import pandas as pd

from utils.excel import *

st.set_page_config(
    page_title="Pacientes",
    page_icon="👤",
    layout="wide"
)

st.title("👤 Pacientes")

st.divider()

# =========================================================
# NOVO PACIENTE
# =========================================================

with st.expander("➕ Novo Paciente", expanded=False):

    c1, c2 = st.columns(2)

    with c1:

        nome = st.text_input("Nome")

        cpf = st.text_input("CPF")

        nascimento = st.text_input("Nascimento")

        sexo = st.selectbox(
            "Sexo",
            [
                "Masculino",
                "Feminino"
            ]
        )

    with c2:

        telefone = st.text_input("Telefone")

        responsavel = st.text_input("Responsável")

        escola = st.text_input("Escola")

        diagnostico = st.text_input("Diagnóstico")

    if st.button("💾 Criar Paciente", use_container_width=True):

        ok = criar_paciente(

            nome,
            cpf,
            nascimento,
            sexo,
            telefone,
            responsavel,
            escola,
            diagnostico

        )

        if ok:

            st.success("Paciente criado.")

            st.rerun()

        else:

            st.error("Paciente já existe.")

st.divider()

# =========================================================
# PESQUISA
# =========================================================

pesquisa = st.text_input("🔍 Pesquisar paciente")

lista = listar_pacientes()

if pesquisa != "":

    lista = [

        p

        for p in lista

        if pesquisa.lower() in p.lower()

    ]

# =========================================================
# TABELA
# =========================================================

dados = []

for paciente in lista:

    info = ler_cadastro(paciente)

    dados.append(info)

if len(dados):

    df = pd.DataFrame(dados)

    st.dataframe(

        df,

        hide_index=True,

        use_container_width=True

    )

else:

    st.warning("Nenhum paciente encontrado.")

st.divider()

# =========================================================
# ABRIR
# =========================================================

if len(lista):

    paciente = st.selectbox(

        "Paciente",

        lista

    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button("📂 Abrir", width="stretch"):

            st.session_state["paciente"] = paciente

            st.switch_page("pages/06_Paciente.py")

    with c2:

        if st.button("🗑 Excluir", use_container_width=True):

            excluir_paciente(paciente)

            st.success("Paciente excluído.")

            st.rerun()
