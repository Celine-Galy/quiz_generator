from moviepy import (
    ColorClip,
    TextClip,
    CompositeVideoClip
)

from generator.config import (
    QUESTION_DURATION,
    COUNTDOWN_DURATION
)

from generator.elements import (
    creer_fond,
    creer_titre,
    creer_numero,
    creer_compte_a_rebours
)


def creer_question_association(
    question,
    titre,
    numero,
    width,
    height,
    font
):
    gauche = question["gauche"]
    droite = question["droite"]
    associations = question["associations"]

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
        font_size=55,
        color="white",
        size=(1600, 120),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=QUESTION_DURATION
    ).with_position((160, 180))

    # --------------------------------------------------
    # Colonnes
    # --------------------------------------------------

    largeur = 550
    hauteur = 100

    x_gauche = 180
    x_droite = 1190
    y_depart = 380
    espace = 130

    elements = [
        background,
        titre_clip,
        numero_clip,
        question_clip
    ]

    # --------------------------------------------------
    # Affichage des éléments
    # --------------------------------------------------

    for i, element in enumerate(gauche):

        y = y_depart + i * espace

        fond = ColorClip(
            size=(largeur, hauteur),
            color=(50, 60, 80),
            duration=QUESTION_DURATION
        ).with_position((x_gauche, y))

        texte = TextClip(
            text=f"{chr(65 + i)}. {element}",
            font=font,
            font_size=40,
            color="white",
            size=(largeur - 40, hauteur - 20),
            method="caption",
            text_align="center",
            vertical_align="center",
            duration=QUESTION_DURATION
        ).with_position(
            (x_gauche + 20, y + 10)
        )

        elements.append(fond)
        elements.append(texte)

    for i, element in enumerate(droite):

        y = y_depart + i * espace

        fond = ColorClip(
            size=(largeur, hauteur),
            color=(50, 60, 80),
            duration=QUESTION_DURATION
        ).with_position((x_droite, y))

        texte = TextClip(
            text=f"{i + 1}. {element}",
            font=font,
            font_size=40,
            color="white",
            size=(largeur - 40, hauteur - 20),
            method="caption",
            text_align="center",
            vertical_align="center",
            duration=QUESTION_DURATION
        ).with_position(
            (x_droite + 20, y + 10)
        )

        elements.append(fond)
        elements.append(texte)

    # --------------------------------------------------
    # Révélation des associations
    # --------------------------------------------------

    for lettre, numero_droite in associations.items():

        index_gauche = ord(lettre.upper()) - 65
        index_droite = numero_droite - 1

        y_gauche = y_depart + index_gauche * espace
        y_droite = y_depart + index_droite * espace

        # Ligne de liaison
        ligne = ColorClip(
            size=(460, 8),
            color=(30, 140, 70),
            duration=QUESTION_DURATION - COUNTDOWN_DURATION
        ).with_position(
            (
                x_gauche + largeur,
                y_gauche + hauteur // 2
            )
        ).with_start(COUNTDOWN_DURATION)

        elements.append(ligne)

        # Mise en évidence à gauche
        fond_gauche = ColorClip(
            size=(largeur, hauteur),
            color=(30, 140, 70),
            duration=QUESTION_DURATION - COUNTDOWN_DURATION
        ).with_position(
            (x_gauche, y_gauche)
        ).with_start(COUNTDOWN_DURATION)

        elements.append(fond_gauche)

        # Mise en évidence à droite
        fond_droite = ColorClip(
            size=(largeur, hauteur),
            color=(30, 140, 70),
            duration=QUESTION_DURATION - COUNTDOWN_DURATION
        ).with_position(
            (x_droite, y_droite)
        ).with_start(COUNTDOWN_DURATION)

        elements.append(fond_droite)

    elements.extend(compteurs)

    return CompositeVideoClip(
        elements,
        size=(width, height)
    )