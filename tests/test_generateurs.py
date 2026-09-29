import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent)
)

from generator.config import (
    WIDTH,
    HEIGHT,
    FONT,
    QUESTION_DURATION
)

from generator.questions.qcm import creer_question_qcm
from generator.questions.vrai_faux import creer_question_vrai_faux
from generator.questions.calcul import creer_question_calcul
from generator.questions.completer import creer_question_completer
from generator.questions.intrus import creer_question_intrus
from generator.questions.classement import creer_question_classement
from generator.questions.texte_cache import creer_question_texte_cache
from generator.questions.association import creer_question_association
from generator.questions.logo import creer_question_logo
from generator.questions.image import creer_question_image
from generator.questions.rebus import creer_question_rebus

def test_generateur_qcm():
    question = {
        "type": "qcm",
        "question": "Combien font 2 + 2 ?",
        "reponses": ["3", "4", "5", "6"],
        "bonne_reponse": 1
    }

    scene = creer_question_qcm(
        question, "Test", 1,
        WIDTH, HEIGHT, FONT
    )

    assert scene.duration == QUESTION_DURATION


def test_generateur_vrai_faux():
    question = {
        "type": "vrai_faux",
        "question": "La Terre est ronde.",
        "bonne_reponse": True
    }

    scene = creer_question_vrai_faux(
        question, "Test", 1,
        WIDTH, HEIGHT, FONT
    )

    assert scene.duration == QUESTION_DURATION


def test_generateur_calcul():
    question = {
        "type": "calcul",
        "question": "Combien font 15 × 8 ?",
        "bonne_reponse": "120"
    }

    scene = creer_question_calcul(
        question, "Test", 1,
        WIDTH, HEIGHT, FONT
    )

    assert scene.duration == QUESTION_DURATION


def test_generateur_completer():
    question = {
        "type": "completer",
        "question": "Complète cette phrase :",
        "avant": "Le protocole",
        "apres": "permet d'attribuer automatiquement une adresse IP.",
        "reponse": "DHCP"
    }

    scene = creer_question_completer(
        question, "Test", 1,
        WIDTH, HEIGHT, FONT
    )

    assert scene.duration == QUESTION_DURATION

def test_generateur_intrus():
    question = {
        "type": "intrus",
        "question": "Quel élément est différent ?",
        "elements": [
            "TCP",
            "UDP",
            "HTTP",
            "Pizza"
        ],
        "intrus": 3
    }

    scene = creer_question_intrus(
        question, "Test", 1,
        WIDTH, HEIGHT, FONT
    )

    assert scene.duration == QUESTION_DURATION

def test_generateur_classement():
    question = {
        "type": "classement",
        "question": "Classe ces éléments dans le bon ordre :",
        "elements": [
            "Étape 1",
            "Étape 2",
            "Étape 3",
            "Étape 4"
        ],
        "ordre_correct": [
            0,
            1,
            2,
            3
        ]
    }

    scene = creer_question_classement(
        question, "Test", 1,
        WIDTH, HEIGHT, FONT
    )

    assert scene.duration == QUESTION_DURATION

def test_generateur_texte_cache():
    question = {
        "type": "texte_cache",
        "question": "Complète le nom du langage :",
        "texte": "P _ T H O N",
        "bonne_reponse": "Y"
    }

    scene = creer_question_texte_cache(
        question, "Test", 1,
        WIDTH, HEIGHT, FONT
    )

    assert scene.duration == QUESTION_DURATION

def test_generateur_association():
    question = {
        "type": "association",
        "question": "Associe chaque protocole à son utilisation :",
        "gauche": [
            "HTTP",
            "DNS",
            "DHCP"
        ],
        "droite": [
            "Attribution automatique d'une IP",
            "Résolution de noms",
            "Communication Web"
        ],
       "associations": {
            "A": 3,
            "B": 2,
            "C": 1
        }
    }

    scene = creer_question_association(
        question, "Test", 1,
        WIDTH, HEIGHT, FONT
    )

    assert scene.duration == QUESTION_DURATION

def test_association_mapping():
    question = {
        "type": "association",
        "question": "Associe chaque langage à son domaine.",
        "gauche": [
            "HTML",
            "Python",
            "SQL",
            "CSS"
        ],
        "droite": [
            "Base de données",
            "Mise en forme",
            "Structure d'une page web",
            "Programmation"
        ],
        "associations": {
            "A": 3,
            "B": 4,
            "C": 1,
            "D": 2
        }
    }

    associations = question["associations"]

    assert associations["A"] == 3
    assert associations["B"] == 4
    assert associations["C"] == 1
    assert associations["D"] == 2

def test_association_index_mapping():
    associations = {
        "A": 3,
        "B": 4,
        "C": 1,
        "D": 2
    }

    assert associations["A"] - 1 == 2
    assert associations["B"] - 1 == 3
    assert associations["C"] - 1 == 0
    assert associations["D"] - 1 == 1

def test_generateur_logo():
    question = {
        "type": "logo",
        "image": "assets/images/microsoft.jpg",
        "bonne_reponse": "Nom du logo"
    }

    scene = creer_question_logo(
        question, "Test", 1,
        WIDTH, HEIGHT, FONT
    )

    assert scene.duration == QUESTION_DURATION

def test_generateur_image():
    question = {
        "type": "image",
        "question": "Quelle est cette image ?",
        "image": "assets/images/microsoft.jpg",
        "bonne_reponse": "Test"
    }

    scene = creer_question_image(
        question, "Test", 1,
        WIDTH, HEIGHT, FONT
    )

    assert scene.duration == QUESTION_DURATION

def test_generateur_rebus():
    question = {
        "type": "rebus",
        "question": "Quel mot se cache derrière ce rébus ?",
        "images": [
            "assets/rebus/chat.jpg",
            "assets/rebus/pot.jpg"
        ],
        "bonne_reponse": "Test"
    }

    scene = creer_question_rebus(
        question, "Test", 1,
        WIDTH, HEIGHT, FONT
    )

    assert scene.duration == QUESTION_DURATION