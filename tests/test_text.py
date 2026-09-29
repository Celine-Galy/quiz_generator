from generator.text import (
    creer_texte_adapte,
    mesurer_texte,
    trouver_taille_police,
    creer_image_texte
)

def test_mesurer_texte():
    largeur, hauteur = mesurer_texte(
        texte="Texte de test",
        font="assets/fonts/arial.ttf",
        taille_police=40
    )

    assert largeur > 0
    assert hauteur > 0

def test_creer_texte_adapte():
    clip = creer_texte_adapte(
        texte="Texte de test",
        font="assets/fonts/arial.ttf",
        largeur=800,
        hauteur=200,
        taille_police=40,
        couleur=(255, 255, 255)
    )

    assert clip.w == 800
    assert clip.h == 200

def test_texte_long():
    clip = creer_texte_adapte(
        texte=(
            "Ceci est un texte volontairement très long "
            "pour vérifier que la taille de police est adaptée "
            "automatiquement à la zone disponible."
        ),
        font="assets/fonts/arial.ttf",
        largeur=400,
        hauteur=100,
        taille_police=55,
        couleur=(255, 255, 255),
        taille_minimale=25
    )

    assert clip.w == 400
    assert clip.h == 100

def test_trouver_taille_police():
    taille = trouver_taille_police(
        texte="Texte très long qui doit être réduit",
        font="assets/fonts/arial.ttf",
        largeur=300,
        hauteur=100,
        taille_police=55,
        taille_minimale=25
    )

    assert 25 <= taille < 55

def test_texte_long_taille_reduite():
    taille = trouver_taille_police(
        texte=(
            "Ceci est un texte volontairement très long "
            "pour vérifier que la taille de police est adaptée "
            "automatiquement à la zone disponible."
        ),
        font="assets/fonts/arial.ttf",
        largeur=400,
        hauteur=100,
        taille_police=55,
        taille_minimale=25
    )

    assert taille < 55

def test_creer_image_texte():
    image = creer_image_texte(
        texte="Première ligne\nDeuxième ligne",
        font="assets/fonts/arial.ttf",
        largeur=400,
        hauteur=200,
        taille_police=40,
        couleur=(255, 255, 255)
    )

    assert image.size == (400, 200)

def test_taille_police_texte_long():
    taille = trouver_taille_police(
        texte=(
            "Ceci est un texte volontairement très long "
            "pour vérifier que la taille de police est adaptée "
            "automatiquement à la zone disponible."
        ),
        font="assets/fonts/arial.ttf",
        largeur=400,
        hauteur=100,
        taille_police=55,
        taille_minimale=25
    )

    assert taille < 55
    assert taille >= 25