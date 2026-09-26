import os

from moviepy import (
    TextClip,
    ImageClip,
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

def creer_question_image(
    question,
    titre,
    numero,
    width,
    height,
    font
):

    image_path = question["image"]
    bonne_reponse = question["bonne_reponse"]

    # --------------------------------------------------
    # Vérification de l'image
    # --------------------------------------------------

    if not os.path.exists(image_path):
        raise FileNotFoundError(
            f"Image introuvable : {image_path}"
        )

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
    # Consigne
    # --------------------------------------------------

    question_clip = TextClip(
        text="Quelle est cette image ?",
        font=font,
        font_size=55,
        color="white",
        size=(1600, 100),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=QUESTION_DURATION
    ).with_position(
        (160, 180)
    )

    # --------------------------------------------------
    # Image
    # --------------------------------------------------

    image_clip = (
        ImageClip(image_path)
        .resized(height=450)
        .with_duration(QUESTION_DURATION)
        .with_position(("center", 300))
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
    # Assemblage
    # --------------------------------------------------

    elements = [
        background,
        titre_clip,
        numero_clip,
        question_clip,
        image_clip
    ]

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