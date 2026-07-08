import streamlit as st
from utils.excel import ler, calcular_scoring

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard do Paciente")

if "paciente" not in st.session_state:
    st.warning("Selecione um paciente.")
    st.stop()

nome = st.session_state["paciente"]

st.success(nome)

st.divider()

cpf = ler(nome, "Cadastro", "B4")
nascimento = ler(nome, "Cadastro", "B6")
sexo = ler(nome, "Cadastro", "B7")
telefone = ler(nome, "Cadastro", "B8")
responsavel = ler(nome, "Cadastro", "B9")
escola = ler(nome, "Cadastro", "B10")
diagnostico = ler(nome, "Cadastro", "B11")

try:
    total = calcular_scoring(nome)
except:
    total = 0

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Pontuação Total", total)

with c2:
    st.metric("Paciente", nome)

with c3:
    st.metric("Diagnóstico", diagnostico)

st.divider()

st.subheader("📋 Dados do Paciente")

col1, col2 = st.columns(2)

with col1:
    st.write("**CPF:**", cpf)
    st.write("**Nascimento:**", nascimento)
    st.write("**Sexo:**", sexo)
    st.write("**Telefone:**", telefone)

with col2:
    st.write("**Responsável:**", responsavel)
    st.write("**Escola:**", escola)
    st.write("**Diagnóstico:**", diagnostico)

st.divider()

st.subheader("🧠 Resultado MOTAS")

itens = [
    ("Motricidade Fina", "B2"),
    ("Motricidade Global", "B3"),
    ("Equilíbrio", "B4"),
    ("Lateralidade", "B5"),
    ("Organização Espacial", "B6"),
    ("Organização Temporal", "B7"),
    ("Esquema Corporal", "B8"),
    ("Coordenação Bilateral", "B9"),
    ("Coordenação Óculo-manual", "B10"),
    ("Atenção", "B11"),
    ("Planejamento Motor", "B12"),
]

for titulo, celula in itens:

    valor = ler(nome, "MOTAS", celula)

    if valor is None:
        valor = 0

    st.progress(min(float(valor) / 20, 1.0), text=f"{titulo}: {valor}")

st.divider()

st.success("Dashboard carregado com sucesso.")