from moviepy import ColorClip, CompositeVideoClip
from generator.text import creer_texte_adapte
from generator.config import COLOR_BACKGROUND, COLOR_WHITE


FONT = "assets/fonts/arial.ttf"

fond = ColorClip(
    size=(800, 600),
    color=COLOR_BACKGROUND,
    duration=5
)

texte_court = creer_texte_adapte(
    texte="Texte court",
    font=FONT,
    largeur=700,
    hauteur=100,
    taille_police=55,
    taille_minimale=25,
    couleur=COLOR_WHITE
).with_position((50, 50))

texte_long = creer_texte_adapte(
    texte=(
        "Ceci est un texte volontairement très long "
        "pour vérifier que la taille de police est adaptée "
        "automatiquement à la zone disponible."
    ),
    font=FONT,
    largeur=700,
    hauteur=200,
    taille_police=55,
    taille_minimale=25,
    couleur=COLOR_WHITE
).with_position((50, 250))

video = CompositeVideoClip(
    [
        fond,
        texte_court,
        texte_long
    ],
    size=(800, 600)
).with_duration(5)

video.write_videofile(
    "output/test_text.mp4",
    fps=30,
    codec="libx264"
)