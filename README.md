# Générateur de quiz vidéo

Générateur de vidéos de quiz au format **16:9 – 1920×1080**, développé en Python avec **MoviePy** et **Pillow**.

Le contenu des quiz est défini dans `quiz.json`.

Le programme génère automatiquement une vidéo MP4 dans le dossier `output`.

---

## 1. Prérequis

* Python 3
* Environnement virtuel Python (`.venv`)
* MoviePy
* Pillow
* pytest (pour les tests)
* FFmpeg (utilisé par MoviePy pour générer la vidéo)

Les dépendances du projet sont disponibles dans :

```text
requirements.txt
```

---

## 2. Structure du projet

```text
quizz/
│
├── main.py
├── quiz.json
├── requirements.txt
├── README.md
│
├── assets/
│   ├── fonts/
│   │   └── arial.ttf
│   │
│   ├── images/
│   │
│   └── rebus/
│
├── generator/
│   ├── __init__.py
│   ├── config.py
│   ├── elements.py
│   ├── text.py
│   ├── video.py
│   ├── audio.py
│   │
│   └── questions/
│       ├── __init__.py
│       ├── qcm.py
│       ├── vrai_faux.py
│       ├── image.py
│       ├── rebus.py
│       ├── intrus.py
│       ├── classement.py
│       ├── texte_cache.py
│       ├── logo.py
│       ├── association.py
│       ├── calcul.py
│       └── completer.py
│
├── tests/
│   ├── test_completer.py
│   ├── test_generateurs.py
│   ├── test_quiz_json.py
│   └── test_text.py
│
└── output/
    └── quiz.mp4
```

### Rôle des principaux fichiers

* `main.py` : point d'entrée du programme et orchestration de la génération.
* `quiz.json` : contenu du quiz.
* `generator/config.py` : paramètres généraux de la vidéo et paramètres graphiques.
* `generator/elements.py` : éléments graphiques communs aux différentes questions.
* `generator/text.py` : gestion de l'affichage automatique des textes longs.
* `generator/video.py` : assemblage des scènes vidéo.
* `generator/questions/` : générateurs spécifiques à chaque type de question.
* `tests/` : tests automatisés du projet.
* `assets/` : polices et images utilisées par les quiz.
* `output/` : vidéos générées.

---

## 3. Lancer le projet

Ouvrir un terminal dans le dossier du projet :

```text
C:\Projets\quizz
```

### Activer l'environnement virtuel

Sous Windows :

```bash
.venv\Scripts\activate
```

Une fois activé, le terminal doit afficher quelque chose comme :

```text
(.venv) C:\Projets\quizz>
```

### Lancer le programme

```bash
python main.py
```

Le programme affiche la progression :

```text
Création de la question 1...
Création de la question 2...
Création de la question 3...
...
Vidéo créée : output/quiz.mp4
```

La vidéo générée se trouve dans :

```text
output/quiz.mp4
```

---

## 4. Installer les dépendances

Si l'environnement virtuel n'existe pas encore :

```bash
python -m venv .venv
```

Puis l'activer :

```bash
.venv\Scripts\activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## 5. Mettre à jour les dépendances

Après l'installation ou la modification d'une bibliothèque :

```bash
pip freeze > requirements.txt
```

Cela permet de conserver les versions utilisées par le projet.

---

## 6. Modifier le contenu du quiz

Les questions sont définies dans :

```text
quiz.json
```

Exemple :

```json
{
    "titre": "Quiz informatique",
    "questions": [
        {
            "type": "qcm",
            "question": "Quel protocole attribue automatiquement une adresse IP ?",
            "reponses": [
                "DNS",
                "DHCP",
                "ARP",
                "FTP"
            ],
            "bonne_reponse": 1
        }
    ]
}
```

La valeur de `bonne_reponse` correspond à l'index de la réponse :

```text
0 → première réponse
1 → deuxième réponse
2 → troisième réponse
3 → quatrième réponse
```

---

# 7. Types de questions disponibles

Le projet prend actuellement en charge les types suivants :

* QCM
* Vrai / Faux
* Image
* Rébus
* Intrus
* Classement
* Texte caché
* Logo
* Association
* Calcul
* Compléter

---

## QCM

```json
{
    "type": "qcm",
    "question": "Quel protocole attribue automatiquement une adresse IP ?",
    "reponses": [
        "DNS",
        "DHCP",
        "ARP",
        "FTP"
    ],
    "bonne_reponse": 1
}
```

Les questions longues sont automatiquement découpées sur plusieurs lignes et la taille de la police peut être réduite pour rester dans la zone prévue.

---

## Vrai / Faux

```json
{
    "type": "vrai_faux",
    "question": "Le protocole DNS permet de résoudre les noms de domaine.",
    "bonne_reponse": true
}
```

La réponse peut être :

```text
true  → VRAI
false → FAUX
```

---

## Image

```json
{
    "type": "image",
    "image": "assets/images/python.jpg",
    "bonne_reponse": "Python"
}
```

L'image doit être placée dans :

```text
assets/images/
```

---

## Rébus

```json
{
    "type": "rebus",
    "question": "Quel mot se cache derrière ce rébus ?",
    "images": [
        "assets/rebus/chat.jpg",
        "assets/rebus/peau.jpg"
    ],
    "bonne_reponse": "Chapeau"
}
```

Les images du rébus doivent être placées dans :

```text
assets/rebus/
```

---

## Intrus

Le type `intrus` permet de proposer plusieurs éléments et de demander lequel ne correspond pas aux autres.

Exemple de structure :

```json
{
    "type": "intrus",
    "question": "Quel élément est l'intrus ?",
    "reponses": [
        "HTTP",
        "HTTPS",
        "FTP",
        "HTML"
    ],
    "bonne_reponse": 3
}
```

---

## Classement

Le type `classement` permet de présenter plusieurs éléments qui doivent être classés dans un ordre déterminé.

La structure exacte dépend du scénario de classement utilisé par le générateur.

---

## Texte caché

Le type `texte_cache` permet d'afficher progressivement ou de révéler un texte.

Exemple :

```json
{
    "type": "texte_cache",
    "question": "Quel mot se cache dans cette phrase ?",
    "texte": "..."
}
```

---

## Logo

Le type `logo` permet de faire deviner une entreprise, une marque ou une organisation à partir de son logo.

Les images sont stockées dans :

```text
assets/images/
```

---

## Association

Le type `association` permet d'associer des éléments d'une colonne avec les éléments correspondants d'une autre colonne.

Exemple :

```json
{
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
```

Les associations utilisent les indices des éléments de la colonne de droite.

---

## Calcul

Le type `calcul` permet de proposer une question nécessitant une réponse numérique.

Exemple :

```json
{
    "type": "calcul",
    "question": "Combien font 15 × 8 ?",
    "bonne_reponse": "120"
}
```

---

## Compléter

Le type `completer` permet de demander à l'utilisateur de compléter une phrase.

Exemple :

```json
{
    "type": "completer",
    "question": "Complète cette phrase :",
    "avant": "Le protocole",
    "apres": "permet d’attribuer automatiquement une adresse IP.",
    "reponse": "DHCP"
}
```

La réponse est affichée lors de la révélation.

---

# 8. Ajouter une image

Pour les questions utilisant une image, placer le fichier dans :

```text
assets/images/
```

Par exemple :

```text
assets/images/python.jpg
```

Puis indiquer le chemin dans `quiz.json` :

```json
"image": "assets/images/python.jpg"
```

---

# 9. Ajouter une image de rébus

Placer les images dans :

```text
assets/rebus/
```

Exemple :

```text
assets/
└── rebus/
    ├── chat.jpg
    └── peau.jpg
```

Puis dans `quiz.json` :

```json
"images": [
    "assets/rebus/chat.jpg",
    "assets/rebus/peau.jpg"
]
```

---

# 10. Paramètres vidéo

Les paramètres généraux sont centralisés dans :

```text
generator/config.py
```

Paramètres actuels :

```python
WIDTH = 1920
HEIGHT = 1080
FPS = 30
```

Cela correspond à :

* Résolution : **1920 × 1080**
* Format : **16:9**
* Fréquence : **30 images/seconde**
* Format de sortie : **MP4**
* Codec vidéo : **H.264**
* Audio : actuellement désactivé

---

# 11. Durée d'une question

La durée actuelle d'une question est de :

```text
8 secondes
```

Le compte à rebours dure :

```text
5 secondes
```

La réponse correcte apparaît ensuite pendant les :

```text
3 dernières secondes
```

Ces paramètres sont centralisés dans :

```text
generator/config.py
```

avec :

```python
QUESTION_DURATION = 8
COUNTDOWN_DURATION = 5
```

---

# 12. Paramètres graphiques

Les principaux paramètres graphiques sont également centralisés dans :

```text
generator/config.py
```

Ils comprennent notamment :

* couleurs ;
* tailles de police ;
* police utilisée ;
* dimensions générales de la vidéo ;
* durée des scènes.

Exemple :

```python
FONT_SIZE_QUESTION = 55
FONT_SIZE_OPTION = 40
FONT_SIZE_REVEAL = 45
FONT_SIZE_COUNTDOWN = 70
```

Cela permet de modifier l'apparence générale du quiz sans devoir modifier chaque générateur individuellement.

Certaines tailles peuvent toutefois rester spécifiques à certains types de questions lorsque leur mise en page nécessite un traitement particulier.

---

# 13. Gestion automatique des textes longs

Le fichier :

```text
generator/text.py
```

contient les fonctions permettant de gérer les textes longs.

Le système utilise **Pillow** pour :

* mesurer le texte ;
* déterminer une taille de police adaptée ;
* découper automatiquement le texte sur plusieurs lignes ;
* centrer verticalement et horizontalement le texte ;
* générer une image contenant le texte ;
* intégrer cette image dans la vidéo avec MoviePy.

La fonction principale utilisée pour cela est :

```python
creer_texte_adapte()
```

Elle permet notamment d'éviter qu'une question longue soit coupée ou dépasse de sa zone d'affichage.

Le système est actuellement intégré au générateur **QCM**.

---

# 14. Tests automatisés

Le projet utilise **pytest** pour vérifier le fonctionnement des différents composants.

Les tests sont regroupés dans :

```text
tests/
```

Pour lancer l'ensemble des tests :

```bash
pytest
```

Le projet dispose actuellement de tests pour :

* les générateurs de questions ;
* la structure du fichier `quiz.json` ;
* le générateur `completer` ;
* les fonctions de gestion du texte.

Une suite de tests verte doit afficher un résultat similaire à :

```text
26 passed
```

Les tests doivent être exécutés après une modification importante du code.

---

# 15. Police

La police utilisée actuellement est :

```text
assets/fonts/arial.ttf
```

Elle est définie dans :

```text
generator/config.py
```

avec :

```python
FONT = "assets/fonts/arial.ttf"
```

Si la police est introuvable, vérifier que le fichier existe bien :

```text
assets/fonts/arial.ttf
```

---

# 16. En cas d'erreur

## Erreur : fichier image introuvable

Exemple :

```text
FileNotFoundError: Image introuvable
```

Vérifier le chemin indiqué dans `quiz.json`.

Par exemple :

```json
"image": "assets/images/python.jpg"
```

Le fichier doit réellement se trouver ici :

```text
quizz/
└── assets/
    └── images/
        └── python.jpg
```

---

## Erreur concernant la police

Vérifier que :

```text
assets/fonts/arial.ttf
```

existe.

---

## Le programme ne trouve pas MoviePy

Vérifier que l'environnement virtuel est activé :

```bash
.venv\Scripts\activate
```

Puis installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## Un test échoue après une modification

Lancer :

```bash
pytest
```

Lire le nom du test qui échoue et corriger le problème avant de poursuivre les modifications.

Il est recommandé de procéder progressivement :

```text
Modifier le code
      ↓
Lancer pytest
      ↓
Vérifier les tests
      ↓
Générer une vidéo
      ↓
Vérifier le rendu visuel
```

---

# 17. Workflow habituel

Pour créer une nouvelle vidéo :

```text
1. Modifier quiz.json
        ↓
2. Ajouter les éventuelles images
        ↓
3. Activer .venv
        ↓
4. Lancer les tests
        ↓
5. Lancer python main.py
        ↓
6. Vérifier output/quiz.mp4
        ↓
7. Vérifier visuellement le rendu
```

Commandes :

```bash
cd C:\Projets\quizz

.venv\Scripts\activate

pytest

python main.py
```

La vidéo finale est ensuite disponible dans :

```text
output/quiz.mp4
```

---

# 18. État actuel du projet

Types de questions :

* [x] QCM
* [x] Vrai / Faux
* [x] Image à deviner
* [x] Rébus
* [x] Intrus
* [x] Classement
* [x] Texte caché
* [x] Logo
* [x] Calcul
* [x] Association
* [x] Compléter

Évolutions techniques :

* [x] Architecture séparant les générateurs de questions
* [x] Centralisation des paramètres graphiques
* [x] Gestion automatique des textes longs
* [x] Tests automatisés avec pytest
* [x] Génération de scènes vidéo indépendantes
* [ ] Ajouter des transitions
* [ ] Ajouter de l'audio
* [ ] Ajouter des effets sonores
* [ ] Ajouter une musique de fond
* [ ] Améliorer la gestion des images
* [ ] Ajouter éventuellement une interface de génération
* [ ] Automatiser davantage la création des vidéos

---

# 19. Commande à retenir

```bash
cd C:\Projets\quizz

.venv\Scripts\activate

pytest

python main.py
```

La vidéo finale est ensuite dans :

```text
output/quiz.mp4
```
