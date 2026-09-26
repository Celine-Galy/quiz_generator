# Générateur de quiz vidéo

Générateur de vidéos de quiz au format **16:9 – 1920×1080**, développé en Python avec **MoviePy**.

Le contenu des quiz est défini dans `quiz.json`.
Le programme génère automatiquement une vidéo MP4 dans le dossier `output`.

---

## 1. Prérequis

* Python installé
* Environnement virtuel Python (`.venv`)
* MoviePy
* Pillow
* FFmpeg (utilisé par MoviePy pour générer la vidéo)

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
│   ├── elements.py
│   ├── video.py
│   │
│   └── questions/
│       ├── __init__.py
│       ├── qcm.py
│       ├── vrai_faux.py
│       ├── image.py
│       └── rebus.py
│
└── output/
    └── quiz.mp4
```

---

## 3. Lancer le projet

Ouvrir un terminal dans le dossier du projet :

```text
C:\Projets\quizz
```

### Activer l'environnement virtuel

Sous Windows :

```bash
python -m venv .venv  
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

Cela permet de conserver la liste des versions utilisées par le projet.

---

# 6. Modifier le contenu du quiz

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

Actuellement, le programme gère :

### QCM

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

### Vrai / Faux

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

### Image

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

### Rébus

```json
{
    "type": "rebus",
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

# 8. Ajouter une image

Pour une question de type `image`, placer l'image dans :

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

Les paramètres principaux sont actuellement définis dans `main.py` :

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

Ces paramètres sont actuellement centralisés dans :

```text
generator/elements.py
```

avec :

```python
QUESTION_DURATION = 8
COUNTDOWN_DURATION = 5
```

---

# 12. Police

La police utilisée est actuellement :

```text
assets/fonts/arial.ttf
```

Elle est définie dans `main.py` :

```python
FONT = os.path.join(
    "assets",
    "fonts",
    "arial.ttf"
)
```

Si la police est introuvable, vérifier que le fichier existe bien :

```text
assets/fonts/arial.ttf
```

---

# 13. En cas d'erreur

### Erreur : fichier image introuvable

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

### Erreur concernant la police

Vérifier que :

```text
assets/fonts/arial.ttf
```

existe.

---

### Le programme ne trouve pas MoviePy

Vérifier que l'environnement virtuel est activé :

```bash
.venv\Scripts\activate
```

Puis :

```bash
pip install -r requirements.txt
```

---

# 14. Workflow habituel

Pour créer une nouvelle vidéo :

```text
1. Modifier quiz.json
        ↓
2. Ajouter les éventuelles images
        ↓
3. Activer .venv
        ↓
4. Lancer python main.py
        ↓
5. Vérifier output/quiz.mp4
```

Commande complète :

```bash
.venv\Scripts\activate
python main.py
```

---

# 15. Évolution prévue du projet

Types de questions envisagés :

* [x] QCM
* [x] Vrai / Faux
* [x] Image à deviner
* [x] Rébus
* [ ] Intrus
* [ ] Classement
* [ ] Texte caché / compléter
* [ ] Logo
* [ ] Son
* [ ] Calcul
* [ ] Association

Évolutions techniques envisagées :

* [ ] Améliorer l'architecture du générateur
* [ ] Centraliser davantage les paramètres graphiques
* [ ] Ajouter des transitions
* [ ] Ajouter de l'audio
* [ ] Ajouter des effets sonores
* [ ] Ajouter une musique de fond
* [ ] Améliorer la gestion des images
* [ ] Ajouter éventuellement une interface de génération
* [ ] Automatiser davantage la création des vidéos

---

## 16. Commande à retenir

Si je dois simplement me rappeler comment lancer le projet :

```bash
cd C:\Projets\quizz
.venv\Scripts\activate
python main.py
```

La vidéo finale est ensuite dans :

```text
output/quiz.mp4
```
