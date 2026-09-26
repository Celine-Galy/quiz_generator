from moviepy import (
    ColorClip,
    TextClip,
    CompositeVideoClip
)

from generator.config import QUESTION_DURATION, COUNTDOWN_DURATION

from generator.elements import (
    creer_fond,
    creer_titre,
    creer_numero,
    creer_compte_a_rebours
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

    background = creer_fond(width, height)
    titre_clip = creer_titre(titre, width, font)
    numero_clip = creer_numero(numero, font)
    compteurs = creer_compte_a_rebours(font)

    # --------------------------------------------------
    # QUESTION
    # --------------------------------------------------

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

    # --------------------------------------------------
    # PROPOSITIONS
    # Affichées uniquement pendant les 5 premières secondes
    # --------------------------------------------------

    positions = [
        (180, 400),
        (1000, 400),
        (180, 580),
        (1000, 580)
    ]

    propositions = []

    for i, element in enumerate(elements_question):

        fond = ColorClip(
            size=(700, 120),
            color=(50, 60, 80),
            duration=COUNTDOWN_DURATION
        ).with_position(
            positions[i]
        )

        texte = TextClip(
            text=f"{chr(65 + i)}. {element}",
            font=font,
            font_size=42,
            color="white",
            size=(660, 90),
            method="caption",
            text_align="center",
            vertical_align="center",
            duration=COUNTDOWN_DURATION
        ).with_position(
            (
                positions[i][0] + 20,
                positions[i][1] + 15
            )
        )

        propositions.append(fond)
        propositions.append(texte)

    # --------------------------------------------------
    # RÉVÉLATION DU CLASSEMENT
    # Affichée uniquement de 5 à 8 secondes
    # --------------------------------------------------

    classement_x = 460
    classement_y = 390

    largeur = 1000
    hauteur_ligne = 105

    revelation = []

    for position, index in enumerate(
        ordre_correct,
        start=1
    ):

        y = classement_y + (position - 1) * hauteur_ligne

        fond = ColorClip(
            size=(largeur, hauteur_ligne - 5),
            color=(30, 140, 70),
            duration=QUESTION_DURATION - COUNTDOWN_DURATION
        ).with_position(
            (classement_x, y)
        ).with_start(
            COUNTDOWN_DURATION
        )

        texte = TextClip(
            text=f"{position}. {elements_question[index]}",
            font=font,
            font_size=40,
            color="white",
            size=(largeur - 40, hauteur_ligne - 25),
            method="caption",
            text_align="center",
            vertical_align="center",
            duration=QUESTION_DURATION - COUNTDOWN_DURATION
        ).with_position(
            (
                classement_x + 20,
                y + 10
            )
        ).with_start(
            COUNTDOWN_DURATION
        )

        revelation.append(fond)
        revelation.append(texte)

    # --------------------------------------------------
    # COMPOSITION
    # --------------------------------------------------

    elements = [
        background,
        titre_clip,
        numero_clip,
        question_clip
    ]

    elements.extend(propositions)
    elements.extend(compteurs)
    elements.extend(revelation)

    return CompositeVideoClip(
        elements,
        size=(width, height)
    )