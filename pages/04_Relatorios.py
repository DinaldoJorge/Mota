import streamlit as st
from pathlib import Path

from utils.relatorios import gerar_pdf

st.set_page_config(
    page_title="Relatórios",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Relatórios")

if "paciente" not in st.session_state:
    st.warning("Selecione um paciente primeiro.")
    st.stop()

nome = st.session_state["paciente"]

st.success(f"Paciente: {nome}")

st.divider()

st.subheader("Gerar Relatório em PDF")

if st.button("📄 Gerar PDF", use_container_width=True):

    arquivo = gerar_pdf(nome)

    st.success("PDF gerado com sucesso!")

    with open(arquivo, "rb") as pdf:

        st.download_button(
            "⬇ Baixar PDF",
            pdf,
            file_name=f"{nome}.pdf",
            mime="application/pdf",
            use_container_width=True
        )

st.divider()

pasta = Path("relatorios")

if pasta.exists():

    arquivos = sorted(pasta.glob("*.pdf"))

    if len(arquivos):

        st.subheader("Relatórios Gerados")

        for pdf in arquivos:

            col1, col2 = st.columns([5,1])

            with col1:
                st.write("📄", pdf.name)

            with col2:

                with open(pdf, "rb") as f:

                    st.download_button(
                        "⬇",
                        f,
                        file_name=pdf.name,
                        mime="application/pdf",
                        key=pdf.name
                    )

    else:

        st.info("Nenhum relatório foi gerado ainda.")