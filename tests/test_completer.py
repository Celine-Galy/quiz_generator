import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent)
)

from generator.questions.completer import creer_question_completer
from generator.config import (
    WIDTH,
    HEIGHT,
    FONT,
    QUESTION_DURATION
)


def test_completer():
    question = {
        "type": "completer",
        "question": "Complète cette phrase :",
        "avant": "Le protocole",
        "apres": "permet d'attribuer automatiquement une adresse IP.",
        "reponse": "DHCP"
    }

    scene = creer_question_completer(
        question,
        "Quiz Réseau",
        1,
        WIDTH,
        HEIGHT,
        FONT
    )

    assert scene.duration == QUESTION_DURATION

def test_completer_reponse_manquante():

    question = {
        "type": "completer",
        "question": "Complète cette phrase :",
        "avant": "Le protocole",
        "apres": "permet d'attribuer automatiquement une adresse IP."
    }

    try:
        creer_question_completer(
            question,
            "Quiz Réseau",
            1,
            WIDTH,
            HEIGHT,
            FONT
        )
    except KeyError:
        return

    assert False, "Une erreur aurait dû être levée"