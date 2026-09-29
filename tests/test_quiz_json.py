import json
from pathlib import Path


def charger_quiz():
    chemin = Path(__file__).resolve().parent.parent / "quiz.json"

    with open(chemin, "r", encoding="utf-8") as fichier:
        return json.load(fichier)


def test_quiz_json_valide():
    quiz = charger_quiz()

    assert "titre" in quiz
    assert "questions" in quiz
    assert isinstance(quiz["questions"], list)
    assert len(quiz["questions"]) > 0


def test_questions_ont_un_type():
    quiz = charger_quiz()

    for question in quiz["questions"]:
        assert "type" in question
        assert isinstance(question["type"], str)
        assert question["type"] != ""


def test_types_questions_connus():
    quiz = charger_quiz()

    types_connus = {
        "qcm",
        "vrai_faux",
        "image",
        "rebus",
        "intrus",
        "classement",
        "texte_cache",
        "logo",
        "association",
        "calcul",
        "completer"
    }

    for question in quiz["questions"]:
        assert question["type"] in types_connus

def test_champs_obligatoires_par_type():
    quiz = charger_quiz()

    champs_obligatoires = {
        "qcm": ["question", "reponses", "bonne_reponse"],
        "vrai_faux": ["question", "bonne_reponse"],
        "image": ["image", "bonne_reponse"],
        "rebus": ["question", "images", "bonne_reponse"],
        "intrus": ["question", "elements", "intrus"],
        "classement": ["question", "elements", "ordre_correct"],
        "texte_cache": ["question", "texte", "bonne_reponse"],
        "logo": ["image", "bonne_reponse"],
        "association": ["question", "gauche", "droite", "associations"],
        "calcul": ["question", "bonne_reponse"],
        "completer": ["question", "avant", "apres", "reponse"]
    }

    for question in quiz["questions"]:
        type_question = question["type"]

        for champ in champs_obligatoires[type_question]:
            assert champ in question, (
                f"Le champ '{champ}' manque "
                f"dans une question de type '{type_question}'"
            )