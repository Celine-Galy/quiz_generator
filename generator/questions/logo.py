import os

from moviepy import (
    ImageClip,
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
    creer_compte_a_rebours,
    creer_revelation
)


def creer_question_logo(
    question,
    titre,
    numero,
    width,
    height,
    font
):
    image_path = question["image"]
    bonne_reponse = question["bonne_reponse"]

    # Vérification de l'image
    if not os.path.exists(image_path):
        raise FileNotFoundError(
            f"Logo introuvable : {image_path}"
        )

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
        text="Quel est ce logo ?",
        font=font,
        font_size=FONT_SIZE_QUESTION,
        color=COLOR_WHITE,
        size=(1600, 100),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=QUESTION_DURATION
    ).with_position((160, 180))

    # --------------------------------------------------
    # Logo
    # --------------------------------------------------

    logo_clip = (
        ImageClip(image_path)
        .resized(height=400)
        .with_duration(QUESTION_DURATION)
        .with_position(("center", 320))
    )

    # --------------------------------------------------
    # Révélation
    # --------------------------------------------------

    bonne_reponse_fond, bonne_reponse_texte = creer_revelation(
        bonne_reponse,
        (460, 800),
        1000,
        120,
        font
    )

    # --------------------------------------------------
    # Composition
    # --------------------------------------------------

    elements = [
        background,
        titre_clip,
        numero_clip,
        question_clip,
        logo_clip
    ]

    elements.extend(compteurs)

    elements.append(bonne_reponse_fond)
    elements.append(bonne_reponse_texte)

    return CompositeVideoClip(
        elements,
        size=(width, height)
    )