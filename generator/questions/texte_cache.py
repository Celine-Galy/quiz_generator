from moviepy import (
    TextClip,
    CompositeVideoClip
)

from generator.config import (
    QUESTION_DURATION,
    COUNTDOWN_DURATION,
    COLOR_WHITE,
    FONT_SIZE_QUESTION
)

from generator.elements import (
    creer_fond,
    creer_titre,
    creer_numero,
    creer_compte_a_rebours
)


def creer_question_texte_cache(
    question,
    titre,
    numero,
    width,
    height,
    font
):
    texte = question["texte"]
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
        text=question["question"],
        font=font,
        font_size=FONT_SIZE_QUESTION,
        color=COLOR_WHITE,
        size=(1600, 120),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=QUESTION_DURATION
    ).with_position((160, 220))

    # --------------------------------------------------
    # Texte à compléter
    # --------------------------------------------------

    texte_clip = TextClip(
        text=texte,
        font=font,
        font_size=90,
        color=COLOR_WHITE,
        size=(1600, 180),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=COUNTDOWN_DURATION
    ).with_position((160, 450))

    # --------------------------------------------------
    # Réponse
    # --------------------------------------------------

    reponse_clip = TextClip(
        text=texte.replace("_", bonne_reponse),
        font=font,
        font_size=90,
        color=COLOR_WHITE,
        size=(1600, 180),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=QUESTION_DURATION - COUNTDOWN_DURATION
    ).with_position((160, 450)).with_start(
        COUNTDOWN_DURATION
    )

    # --------------------------------------------------
    # Composition
    # --------------------------------------------------

    elements = [
        background,
        titre_clip,
        numero_clip,
        question_clip,
        texte_clip
    ]

    elements.extend(compteurs)

    elements.append(reponse_clip)

    return CompositeVideoClip(
        elements,
        size=(width, height)
    )