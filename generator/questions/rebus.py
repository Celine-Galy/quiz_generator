import os

from moviepy import (
    ImageClip,
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
    FONT_SIZE_QUESTION,
    COLOR_WHITE
)

def creer_question_rebus(
    question,
    titre,
    numero,
    width,
    height,
    font
):

    texte_question = question["question"]
    images = question["images"]
    bonne_reponse = question["bonne_reponse"]

    # Vérification des images
    for image_path in images:
        if not os.path.exists(image_path):
            raise FileNotFoundError(
                f"Image de rébus introuvable : {image_path}"
            )

    # Éléments communs
    background = creer_fond(width, height)
    titre_clip = creer_titre(titre, width, font)
    numero_clip = creer_numero(numero, font)
    compteurs = creer_compte_a_rebours(font)
    question_clip = TextClip(
        text=texte_question,
        font=font,
        font_size=FONT_SIZE_QUESTION,
        color=COLOR_WHITE,
        size=(1600, 100),
        method="caption",
        text_align="center",
        vertical_align="center",
        duration=QUESTION_DURATION
    ).with_position((160, 190))

    # Images du rébus
    images_clips = []

    largeur_image = 400
    espace = 80

    largeur_totale = (
        len(images) * largeur_image
        + (len(images) - 1) * espace
    )

    x_depart = (width - largeur_totale) // 2

    for i, image_path in enumerate(images):

        image_clip = (
            ImageClip(image_path)
            .resized(width=largeur_image)
            .with_duration(QUESTION_DURATION)
            .with_position(
                (
                    x_depart + i * (largeur_image + espace),
                    320
                )
            )
        )

        images_clips.append(image_clip)

    # Révélation de la réponse
    bonne_reponse_fond, bonne_reponse_texte = creer_revelation(
        bonne_reponse,
        (460, 800),
        1000,
        120,
        font
    )

    elements = [
        background,
        titre_clip,
        numero_clip,
        question_clip
    ]

    elements.extend(images_clips)
    elements.extend(compteurs)

    elements.append(bonne_reponse_fond)
    elements.append(bonne_reponse_texte)

    return CompositeVideoClip(
        elements,
        size=(width, height)
    )