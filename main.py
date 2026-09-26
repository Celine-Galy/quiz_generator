import json
import os

from generator.questions.qcm import creer_question_qcm
from generator.questions.vrai_faux import creer_question_vrai_faux
from generator.questions.image import creer_question_image
from generator.questions.rebus import creer_question_rebus
from generator.questions.intrus import creer_question_intrus
from generator.questions.classement import creer_question_classement
from generator.questions.texte_cache import creer_question_texte_cache
from generator.questions.logo import creer_question_logo
from generator.questions.association import creer_question_association

from generator.video import assembler_scenes
from generator.config import (
    WIDTH,
    HEIGHT,
    FPS,
    FONT,
    OUTPUT_FILE
)

# Association entre le type de question
# et la fonction qui permet de créer la scène
GENERATEURS = {
    "qcm": creer_question_qcm,
    "vrai_faux": creer_question_vrai_faux,
    "image": creer_question_image,
    "rebus": creer_question_rebus,
    "intrus": creer_question_intrus,
    "classement": creer_question_classement,
    "texte_cache": creer_question_texte_cache,
    "logo": creer_question_logo,
    "association": creer_question_association
}


# Chargement du quiz
with open("quiz.json", "r", encoding="utf-8") as fichier:
    quiz = json.load(fichier)


scenes = []


# Création des scènes
for numero, question in enumerate(
    quiz["questions"],
    start=1
):

    print(f"Création de la question {numero}...")

    type_question = question["type"]

    if type_question not in GENERATEURS:
        print(
            f"Type de question non pris en charge : "
            f"{type_question}"
        )
        continue

    generateur = GENERATEURS[type_question]

    scene = generateur(
        question,
        quiz["titre"],
        numero,
        WIDTH,
        HEIGHT,
        FONT
    )

    scenes.append(scene)


print(f"{len(scenes)} scène(s) créée(s).")


# Assemblage des scènes
video = assembler_scenes(scenes)


# Création du dossier de sortie
os.makedirs("output", exist_ok=True)


# Génération de la vidéo
video.write_videofile(
    OUTPUT_FILE,
    fps=FPS,
    codec="libx264",
    audio=False
)


print(f"Vidéo créée : {OUTPUT_FILE}")