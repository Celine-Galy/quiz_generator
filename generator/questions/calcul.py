from moviepy import (
    TextClip,
    CompositeVideoClip
)

from generator.config import (
    QUESTION_DURATION,
    COLOR_WHITE,
    FONT_SIZE_QUESTION
)

from generator.elements import (
    creer_fond,
    creer_titre,
    creer_numero,
    creer_compte_a_rebours,
    creer_revelation
)


def creer_question_calcul(
    question,
    titre,
    numero,
    width,
    height,
    font
):
    texte_question = question["question"]
    bonne_reponse = question["bonne_reponse"]

    # --------------------------------------------------
    # Éléments communs
    # --------------------------------------------------

    background = creer_fond(width, height)
    titre_clip = creer_titre(titre, width, font)
    numero_clip = creer_numero(numero, font)
    compteurs = creer_compte_a_rebours(font)

    # --------------------------------------------------
    # Question
    # --------------------------------------------------

    question_clip = TextClip(
        text=texte_question,
        font=font,
        font_size=FONT_SIZE_QUESTION,
        color=COLOR_WHITE,
        size=(1600, 220),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=QUESTION_DURATION
    ).with_position((160, 280))

    # --------------------------------------------------
    # Révélation
    # --------------------------------------------------

    bonne_reponse_fond, bonne_reponse_texte = creer_revelation(
        str(bonne_reponse),
        (460, 600),
        1000,
        140,
        font
    )

    # --------------------------------------------------
    # Composition
    # --------------------------------------------------

    elements = [
        background,
        titre_clip,
        numero_clip,
        question_clip
    ]

    elements.extend(compteurs)

    elements.append(bonne_reponse_fond)
    elements.append(bonne_reponse_texte)

    return CompositeVideoClip(
        elements,
        size=(width, height)
    )