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
    creer_revelation
)


def creer_question_intrus(
    question,
    titre,
    numero,
    width,
    height,
    font
):
    elements_question = question["elements"]
    intrus = question["intrus"]

    background = creer_fond(width, height)
    titre_clip = creer_titre(titre, width, font)
    numero_clip = creer_numero(numero, font)
    compteurs = creer_compte_a_rebours(font)

    question_clip = TextClip(
        text=question["question"],
        font=font,
        font_size=65,
        color="white",
        size=(1600, 180),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=QUESTION_DURATION
    ).with_position((160, 160))

    positions = [
        (180, 430),
        (1000, 430),
        (180, 650),
        (1000, 650)
    ]

    elements_clips = []

    for i, element in enumerate(elements_question):

        boite = ColorClip(
            size=(700, 130),
            color=(50, 60, 80),
            duration=QUESTION_DURATION
        ).with_position(positions[i])

        texte_clip = TextClip(
            text=f"{chr(65 + i)}. {element}",
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

        elements_clips.append(boite)
        elements_clips.append(texte_clip)

    # Position de l'intrus
    intrus_position = positions[intrus]

    intrus_fond, intrus_texte = creer_revelation(
        f"{chr(65 + intrus)}. {elements_question[intrus]}",
        intrus_position,
        700,
        130,
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

    elements.append(intrus_fond)
    elements.append(intrus_texte)

    return CompositeVideoClip(
        elements,
        size=(width, height)
    )