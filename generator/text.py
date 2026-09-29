import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy import ImageClip


def mesurer_texte(texte, font, taille_police):
    police = ImageFont.truetype(
        font,
        taille_police
    )

    boite = police.getbbox(texte)

    largeur = boite[2] - boite[0]
    hauteur = boite[3] - boite[1]

    return largeur, hauteur

def decouper_texte(
    texte,
    font,
    taille_police,
    largeur_max
):
    police = ImageFont.truetype(
        font,
        taille_police
    )

    mots = texte.split()
    lignes = []
    ligne = ""

    for mot in mots:
        nouvelle_ligne = (
            f"{ligne} {mot}".strip()
        )

        boite = police.getbbox(nouvelle_ligne)
        largeur = boite[2] - boite[0]

        if largeur <= largeur_max:
            ligne = nouvelle_ligne
        else:
            if ligne:
                lignes.append(ligne)

            ligne = mot

    if ligne:
        lignes.append(ligne)

    return "\n".join(lignes)

def trouver_taille_police(
    texte,
    font,
    largeur,
    hauteur,
    taille_police,
    taille_minimale
):
    taille = taille_police

    while taille >= taille_minimale:
        texte_decoupe = decouper_texte(
            texte=texte,
            font=font,
            taille_police=taille,
            largeur_max=largeur
        )

        police = ImageFont.truetype(
            font,
            taille
        )

        lignes = texte_decoupe.split("\n")

        hauteur_totale = 0
        texte_trop_large = False

        for ligne in lignes:
            boite = police.getbbox(ligne)

            largeur_ligne = boite[2] - boite[0]
            hauteur_ligne = boite[3] - boite[1]

            if largeur_ligne > largeur:
                texte_trop_large = True
                break

            hauteur_totale += hauteur_ligne

        if not texte_trop_large and hauteur_totale <= hauteur:
            return taille

        taille -= 1

    return taille_minimale

def creer_texte_adapte(
    texte,
    font,
    largeur,
    hauteur,
    taille_police,
    couleur,
    taille_minimale=None
):
    if taille_minimale is None:
        taille_minimale = 10

    taille = trouver_taille_police(
        texte=texte,
        font=font,
        largeur=largeur,
        hauteur=hauteur,
        taille_police=taille_police,
        taille_minimale=taille_minimale
    )

    texte_decoupe = decouper_texte(
        texte=texte,
        font=font,
        taille_police=taille,
        largeur_max=largeur
    )

    image = creer_image_texte(
        texte=texte_decoupe,
        font=font,
        largeur=largeur,
        hauteur=hauteur,
        taille_police=taille,
        couleur=couleur
    )

    return ImageClip(
        np.array(image)
    )

def creer_image_texte(
    texte,
    font,
    largeur,
    hauteur,
    taille_police,
    couleur
):
    image = Image.new(
        "RGBA",
        (largeur, hauteur),
        (0, 0, 0, 0)
    )

    dessin = ImageDraw.Draw(image)

    police = ImageFont.truetype(
        font,
        taille_police
    )

    lignes = texte.split("\n")

    hauteurs = []

    for ligne in lignes:
        boite = dessin.textbbox(
            (0, 0),
            ligne,
            font=police
        )

        hauteurs.append(
            boite[3] - boite[1]
        )

    hauteur_totale = sum(hauteurs)

    y = (hauteur - hauteur_totale) / 2

    for ligne, hauteur_ligne in zip(lignes, hauteurs):
        boite = dessin.textbbox(
            (0, 0),
            ligne,
            font=police
        )

        largeur_ligne = boite[2] - boite[0]

        x = (
            (largeur - largeur_ligne) / 2
            - boite[0]
        )

        y_position = y - boite[1]

        dessin.text(
            (x, y_position),
            ligne,
            font=police,
            fill=couleur
        )

        y += hauteur_ligne

    return image