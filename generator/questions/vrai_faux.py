from moviepy import (
    ColorClip,
    TextClip,
    CompositeVideoClip
)

from generator.elements import (
    creer_fond,
    creer_titre,
    creer_numero,
    creer_compte_a_rebours,
    creer_revelation
)

from generator.config import (
    QUESTION_DURATION,
    COLOR_BOX,
    COLOR_WHITE,
    FONT_SIZE_QUESTION,
    FONT_SIZE_OPTION
)

def creer_question_vrai_faux(
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

    background = creer_fond(
        width,
        height
    )

    titre_clip = creer_titre(
        titre,
        width,
        font
    )

    numero_clip = creer_numero(
        numero,
        font
    )

    compteurs = creer_compte_a_rebours(
        font
    )

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
    ).with_position(
        (160, 180)
    )

    # --------------------------------------------------
    # Réponses
    # --------------------------------------------------

    positions = [
        (300, 550),
        (1020, 550)
    ]

    reponses = [
        "VRAI",
        "FAUX"
    ]

    reponses_clips = []

    for i, reponse in enumerate(reponses):

        boite = ColorClip(
            size=(600, 160),
            color=COLOR_BOX,
            duration=QUESTION_DURATION
        ).with_position(
            positions[i]
        )

        texte_clip = TextClip(
            text=reponse,
            font=font,
            font_size=FONT_SIZE_OPTION,
            color=COLOR_WHITE,
            size=(560, 120),
            method="caption",
            text_align="center",
            vertical_align="center",
            duration=QUESTION_DURATION
        ).with_position(
            (
                positions[i][0] + 20,
                positions[i][1] + 20
            )
        )

        reponses_clips.append(boite)
        reponses_clips.append(texte_clip)

    # --------------------------------------------------
    # Bonne réponse
    # --------------------------------------------------

    bonne_index = 0 if bonne_reponse is True else 1

    bonne_position = positions[bonne_index]

    bonne_reponse_fond, bonne_reponse_texte = creer_revelation(
        reponses[bonne_index],
        bonne_position,
        600,
        160,
        font
    )

    # --------------------------------------------------
    # Assemblage
    # --------------------------------------------------

    elements = [
        background,
        titre_clip,
        numero_clip,
        question_clip
    ]

    elements.extend(
        reponses_clips
    )

    elements.extend(
        compteurs
    )

    elements.append(
        bonne_reponse_fond
    )

    elements.append(
        bonne_reponse_texte
    )

    return CompositeVideoClip(
        elements,
        size=(width, height)
    )