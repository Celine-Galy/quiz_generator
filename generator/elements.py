
from moviepy import ColorClip, TextClip
from generator.config import (
    QUESTION_DURATION,
    COUNTDOWN_DURATION,
    COLOR_BACKGROUND,
    COLOR_REVEAL,
    COLOR_WHITE
)

def creer_fond(width, height):
    return ColorClip(
        size=(width, height),
        color=COLOR_BACKGROUND,
        duration=QUESTION_DURATION
    )


def creer_titre(titre, width, font):
    return TextClip(
        text=titre,
        font=font,
        font_size=45,
        color=COLOR_WHITE,
        size=(width, 70),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=QUESTION_DURATION
    ).with_position((0, 40))


def creer_numero(numero, font):
    return TextClip(
        text=f"Question {numero}",
        font=font,
        font_size=40,
        color=COLOR_WHITE,
        size=(400, 60),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=QUESTION_DURATION
    ).with_position((760, 115))


def creer_compte_a_rebours(font):
    compteurs = []

    for chiffre in range(5, 0, -1):

        compteur = TextClip(
            text=str(chiffre),
            font=font,
            font_size=70,
            color=COLOR_WHITE,
            size=(150, 100),
            method="caption",
            text_align="center",
            vertical_align="center",
            duration=1
        ).with_position(
            (885, 800)
        ).with_start(
            5 - chiffre
        )

        compteurs.append(compteur)

    return compteurs


def creer_revelation(
    texte,
    position,
    largeur,
    hauteur,
    font
):

    fond = ColorClip(
        size=(largeur, hauteur),
        color=COLOR_REVEAL,
        duration=QUESTION_DURATION - COUNTDOWN_DURATION
    ).with_position(
        position
    ).with_start(
        COUNTDOWN_DURATION
    )

    texte_clip = TextClip(
        text=texte,
        font=font,
        font_size=45,
        color=COLOR_WHITE,
        size=(largeur - 40, hauteur - 40),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=QUESTION_DURATION - COUNTDOWN_DURATION
    ).with_position(
        (
            position[0] + 20,
            position[1] + 20
        )
    ).with_start(
        COUNTDOWN_DURATION
    )

    return fond, texte_clip

def creer_revelation_liste(
    elements,
    position,
    largeur,
    hauteur,
    font
):
    clips = []

    hauteur_element = hauteur // len(elements)

    for i, element in enumerate(elements):

        y = position[1] + i * hauteur_element

        fond = ColorClip(
            size=(largeur, hauteur_element - 10),
            color=COLOR_REVEAL,
            duration=QUESTION_DURATION - COUNTDOWN_DURATION
        ).with_position(
            (position[0], y)
        ).with_start(COUNTDOWN_DURATION)

        texte = TextClip(
            text=element,
            font=font,
            font_size=40,
            color=COLOR_WHITE,
            size=(largeur - 40, hauteur_element - 30),
            method="caption",
            text_align="center",
            vertical_align="center",
            duration=QUESTION_DURATION - COUNTDOWN_DURATION
        ).with_position(
            (
                position[0] + 20,
                y + 10
            )
        ).with_start(COUNTDOWN_DURATION)

        clips.append(fond)
        clips.append(texte)

    return clips