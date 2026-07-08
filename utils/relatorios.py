from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

from utils.excel import ler, calcular_scoring


def gerar_pdf(nome):

    pasta = Path("relatorios")
    pasta.mkdir(exist_ok=True)

    arquivo = pasta / f"{nome}.pdf"

    doc = SimpleDocTemplate(str(arquivo))
    styles = getSampleStyleSheet()

    story = []

    # =====================================================
    # TÍTULO
    # =====================================================

    story.append(
        Paragraph("NEUROAVALIA PRO", styles["Title"])
    )

    story.append(Spacer(1, 20))

    # =====================================================
    # DADOS DO PACIENTE
    # =====================================================

    story.append(
        Paragraph("DADOS DO PACIENTE", styles["Heading2"])
    )

    campos = [

        ("Nome", nome),
        ("CPF", ler(nome, "Cadastro", "B5")),
        ("Nascimento", ler(nome, "Cadastro", "B6")),
        ("Sexo", ler(nome, "Cadastro", "B7")),
        ("Telefone", ler(nome, "Cadastro", "B8")),
        ("Responsável", ler(nome, "Cadastro", "B9")),
        ("Escola", ler(nome, "Cadastro", "B10")),
        ("Diagnóstico", ler(nome, "Cadastro", "B11"))

    ]

    for titulo, valor in campos:

        if valor is None:
            valor = ""

        story.append(
            Paragraph(f"<b>{titulo}:</b> {valor}", styles["Normal"])
        )

    story.append(Spacer(1, 20))

    # =====================================================
    # RESULTADOS MOTAS
    # =====================================================

    story.append(
        Paragraph("RESULTADOS MOTAS", styles["Heading2"])
    )

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
        ("Planejamento Motor", "B12")

    ]

    for titulo, celula in itens:

        valor = ler(nome, "MOTAS", celula)

        if valor is None:
            valor = 0

        story.append(
            Paragraph(
                f"{titulo}: <b>{valor}</b>",
                styles["Normal"]
            )
        )

    story.append(Spacer(1, 20))

    total = calcular_scoring(nome)

    story.append(
        Paragraph(
            f"Pontuação Total: <b>{total}</b>",
            styles["Heading1"]
        )
    )

    story.append(Spacer(1, 20))

    obs = ler(nome, "MOTAS", "B13")

    if obs is None:
        obs = ""

    story.append(
        Paragraph("Observações", styles["Heading2"])
    )

    story.append(
        Paragraph(str(obs), styles["Normal"])
    )

    doc.build(story)

    return str(arquivo)