from moviepy import (
    ColorClip,
    TextClip,
    CompositeVideoClip
)

from generator.config import (
    QUESTION_DURATION,
    COUNTDOWN_DURATION,
    COLOR_WHITE,
    COLOR_ACCENT,
    FONT_SIZE_QUESTION
)

from generator.elements import (
    creer_fond,
    creer_titre,
    creer_numero,
    creer_compte_a_rebours
)


def creer_question_completer(
    question,
    titre,
    numero,
    width,
    height,
    font
):
    avant = question["avant"]
    apres = question["apres"]
    reponse = question["reponse"]

    # Éléments communs
    background = creer_fond(width, height)
    titre_clip = creer_titre(titre, width, font)
    numero_clip = creer_numero(numero, font)
    compteurs = creer_compte_a_rebours(font)

    # Consigne
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
    ).with_position((160, 200))

    # Texte AVANT
    texte_avant = TextClip(
        text=avant,
        font=font,
        font_size=FONT_SIZE_QUESTION,
        color=COLOR_WHITE,
        size=(1600, 100),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=QUESTION_DURATION
    ).with_position((160, 380))

    # Ligne représentant le mot manquant
    ligne = ColorClip(
        size=(350, 5),
        color=COLOR_WHITE,
        duration=COUNTDOWN_DURATION
    ).with_position(
        (
            (width - 350) // 2,
            500
        )
    )

    # Réponse
    reponse_clip = TextClip(
        text=reponse,
        font=font,
        font_size=FONT_SIZE_QUESTION,
        color=COLOR_ACCENT,
        size=(600, 80),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=QUESTION_DURATION - COUNTDOWN_DURATION
    ).with_position(
        (
            (width - 600) // 2,
            460
        )
    ).with_start(COUNTDOWN_DURATION)

    # Texte APRÈS
    texte_apres = TextClip(
        text=apres,
        font=font,
        font_size=FONT_SIZE_QUESTION,
        color=COLOR_WHITE,
        size=(1600, 180),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=QUESTION_DURATION
    ).with_position((160, 510))

    elements = [
        background,
        titre_clip,
        numero_clip,
        question_clip,
        texte_avant,
        texte_apres,
        ligne,
        reponse_clip
    ]

    elements.extend(compteurs)

    return CompositeVideoClip(
        elements,
        size=(width, height)
    )