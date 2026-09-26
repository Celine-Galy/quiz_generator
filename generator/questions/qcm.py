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

from generator.config import QUESTION_DURATION

def creer_question_qcm(
    question,
    titre,
    numero,
    width,
    height,
    font
):

    texte_question = question["question"]
    reponses = question["reponses"]
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
        font_size=65,
        color="white",
        size=(1600, 180),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=QUESTION_DURATION
    ).with_position(
        (160, 160)
    )

    # --------------------------------------------------
    # Réponses
    # --------------------------------------------------

    positions = [
        (180, 430),
        (1000, 430),
        (180, 650),
        (1000, 650)
    ]

    reponses_clips = []

    for i, reponse in enumerate(reponses):

        lettre = chr(65 + i)

        texte = f"{lettre}. {reponse}"

        boite = ColorClip(
            size=(700, 130),
            color=(50, 60, 80),
            duration=QUESTION_DURATION
        ).with_position(
            positions[i]
        )

        texte_clip = TextClip(
            text=texte,
            font=font,
            font_size=45,
            color="white",
            size=(660, 100),
            method="caption",
            text_align="center",
            vertical_align="center",
            duration=QUESTION_DURATION
        ).with_position(
            (
                positions[i][0] + 20,
                positions[i][1] + 15
            )
        )

        reponses_clips.append(boite)
        reponses_clips.append(texte_clip)

    # --------------------------------------------------
    # Bonne réponse
    # --------------------------------------------------

    bonne_position = positions[bonne_reponse]

    bonne_reponse_fond, bonne_reponse_texte = creer_revelation(
        f"{chr(65 + bonne_reponse)}. {reponses[bonne_reponse]}",
        bonne_position,
        700,
        130,
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

    elements.extend(reponses_clips)

    elements.extend(compteurs)

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

