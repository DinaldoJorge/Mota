import streamlit as st
from utils.excel import ler, escrever, calcular_scoring

st.set_page_config(
    page_title="MOTAS",
    page_icon="🧠",
    layout="wide"
)

if "paciente" not in st.session_state:
    st.warning("Selecione um paciente.")
    st.stop()

nome = st.session_state["paciente"]

st.title("🧠 Avaliação MOTAS")
st.success(nome)

st.divider()

col1, col2 = st.columns(2)

with col1:

    motricidade_fina = st.number_input(
        "Motricidade Fina",
        value=int(ler(nome, "MOTAS", "B2") or 0)
    )

    motricidade_global = st.number_input(
        "Motricidade Global",
        value=int(ler(nome, "MOTAS", "B3") or 0)
    )

    equilibrio = st.number_input(
        "Equilíbrio",
        value=int(ler(nome, "MOTAS", "B4") or 0)
    )

    lateralidade = st.number_input(
        "Lateralidade",
        value=int(ler(nome, "MOTAS", "B5") or 0)
    )

    organizacao_espacial = st.number_input(
        "Organização Espacial",
        value=int(ler(nome, "MOTAS", "B6") or 0)
    )

    organizacao_temporal = st.number_input(
        "Organização Temporal",
        value=int(ler(nome, "MOTAS", "B7") or 0)
    )

with col2:

    esquema_corporal = st.number_input(
        "Esquema Corporal",
        value=int(ler(nome, "MOTAS", "B8") or 0)
    )

    coordenacao_bilateral = st.number_input(
        "Coordenação Bilateral",
        value=int(ler(nome, "MOTAS", "B9") or 0)
    )

    coordenacao_oculo = st.number_input(
        "Coordenação Óculo-manual",
        value=int(ler(nome, "MOTAS", "B10") or 0)
    )

    atencao = st.number_input(
        "Atenção",
        value=int(ler(nome, "MOTAS", "B11") or 0)
    )

    planejamento = st.number_input(
        "Planejamento Motor",
        value=int(ler(nome, "MOTAS", "B12") or 0)
    )

observacoes = st.text_area(
    "Observações",
    value=ler(nome, "MOTAS", "B13") or ""
)

st.divider()

if st.button("💾 Salvar Avaliação", width="stretch"):

    escrever(nome,"MOTAS","B2",motricidade_fina)
    escrever(nome,"MOTAS","B3",motricidade_global)
    escrever(nome,"MOTAS","B4",equilibrio)
    escrever(nome,"MOTAS","B5",lateralidade)
    escrever(nome,"MOTAS","B6",organizacao_espacial)
    escrever(nome,"MOTAS","B7",organizacao_temporal)
    escrever(nome,"MOTAS","B8",esquema_corporal)
    escrever(nome,"MOTAS","B9",coordenacao_bilateral)
    escrever(nome,"MOTAS","B10",coordenacao_oculo)
    escrever(nome,"MOTAS","B11",atencao)
    escrever(nome,"MOTAS","B12",planejamento)
    escrever(nome,"MOTAS","B13",observacoes)

    total = calcular_scoring(nome)

    st.success("Avaliação salva com sucesso!")

    st.metric("Pontuação Total", total)