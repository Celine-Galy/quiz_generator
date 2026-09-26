from moviepy import (
    ColorClip,
    TextClip,
    CompositeVideoClip
)

from generator.config import QUESTION_DURATION

from generator.elements import (
    creer_fond,
    creer_titre,
    creer_numero,
    creer_compte_a_rebours,
    creer_revelation_liste
)


def creer_question_classement(
    question,
    titre,
    numero,
    width,
    height,
    font
):
    elements_question = question["elements"]
    ordre_correct = question["ordre_correct"]

    # Éléments communs
    background = creer_fond(width, height)
    titre_clip = creer_titre(titre, width, font)
    numero_clip = creer_numero(numero, font)
    compteurs = creer_compte_a_rebours(font)

    # Question
    question_clip = TextClip(
        text=question["question"],
        font=font,
        font_size=60,
        color="white",
        size=(1600, 160),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=QUESTION_DURATION
    ).with_position((160, 170))

    # Affichage des éléments dans un ordre mélangé
    positions = [
        (180, 400),
        (1000, 400),
        (180, 580),
        (1000, 580)
    ]

    elements_clips = []

    for i, element in enumerate(elements_question):

        boite = ColorClip(
            size=(700, 120),
            color=(50, 60, 80),
            duration=QUESTION_DURATION
        ).with_position(positions[i])

        texte_clip = TextClip(
            text=f"{chr(65 + i)}. {element}",
            font=font,
            font_size=42,
            color="white",
            size=(660, 90),
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

        elements_clips.append(boite)
        elements_clips.append(texte_clip)

    # Construction de la réponse correcte
    reponse_classement = []

    for position, index in enumerate(ordre_correct, start=1):
        reponse_classement.append(
            f"{position}. {elements_question[index]}"
        )

    revelation_clips = creer_revelation_liste(
        reponse_classement,
        (460, 350),
        1000,
        500,
        font
    )

    elements = [
        background,
        titre_clip,
        numero_clip,
        question_clip
    ]

    elements.extend(elements_clips)
    elements.extend(compteurs)
    elements.extend(revelation_clips)

    return CompositeVideoClip(
        elements,
        size=(width, height)
    )