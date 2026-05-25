# MGA802 — Mini-Projet A : Chiffrement de César

Projet réalisé dans le cadre du cours **MGA802 — Introduction à la programmation avec Python** à l'ÉTS.

---

# Description du programme

Ce programme Python permet de chiffrer et déchiffrer des messages en utilisant deux méthodes de chiffrement :
finalisation du README et correction des conflits
1. Le chiffrement de César classique
2. Le chiffrement Enigma César

Le programme permet :
- le chiffrement et le déchiffrement de messages dans la console ;
- l’utilisation de clés positives, négatives ou nulles ;
- l’utilisation d’un mode brute-force pour retrouver automatiquement les décalages possibles d’un message chiffré ;
- l’exécution du programme directement depuis le terminal avec `argparse` ;
- la validation automatique du code avec des tests unitaires `pytest`.

Les caractères non alphabétiques comme les espaces et la ponctuation sont conservés pendant le chiffrement et le déchiffrement.

---

# Fonctionnalités implémentées

## Chiffrement César classique

- Chiffrement d’un message
- Déchiffrement d’un message
- Gestion des clés positives
- Gestion des clés négatives
- Gestion de la clé nulle
- Conservation des espaces et de la ponctuation

## Brute-force César

- Test automatique des 26 décalages possibles
- Retour des résultats possibles sous forme de dictionnaire Python

## Enigma César

- Chiffrement d’un message avec trois clés différentes
- Rotation automatique des clés pendant le traitement des lettres
- Conservation des majuscules et minuscules
- Gestion des caractères non alphabétiques
- Validation du nombre de clés fournies
- Normalisation des accents avant le chiffrement

---

# Instructions d'installation et d'exécution

## Cloner le projet

```bash
git clone <url-du-github-du-projet>
```

---

## Exécution depuis le terminal

### Chiffrement César

```bash
python main.py chiffrer "Veni, vidi, vici!" --cle 42
```

### Déchiffrement César

```bash
python main.py dechiffrer "Ludy, lyty, lysy!" --cle 42
```

### Brute-force César

```bash
python main.py bruteforce "Ludy, lyty, lysy!" --cle 0
```

### Enigma César

```bash
python main.py enigma "MAISON" --cle 7-16-9
```

---

# Utilisation des tests unitaires

## Exécuter tous les tests

```bash
python -m pytest -v
```

## Exécuter uniquement les tests César classique

```bash
python -m pytest tests/test_caesar.py -v
```

Pour plus d’informations sur l’utilisation des tests, consulter le fichier :

```text
TESTS_GUIDE.md
```

---

## Lecture et écriture des fichiers texte

- Lecture du contenu d’un fichier texte avec `lire_fichier()`
- Écriture du contenu dans un fichier texte avec `ecrire_fichier()`
- Utilisation de `encoding="utf-8"` pour assurer la compatibilité avec les caractères accentués

Le programme utilise :

```python
with open(..., encoding="utf-8") as f:
```

afin de garantir une bonne gestion des caractères spéciaux et des accents.


# Utilisation de argparse

## Afficher l’aide du programme

```bash
python main.py -h
```

---

# Choix de conception

## Chiffrement César

Le chiffrement César a été implémenté avec un décalage circulaire utilisant l’opération modulo `% 26`.

Cette méthode permet :
- de gérer automatiquement les dépassements de l’alphabet ;
- d’accepter les clés négatives ;
- de conserver une logique simple et efficace.

Les lettres majuscules et minuscules sont conservées pendant le traitement.

Les espaces, chiffres et symboles de ponctuation ne sont pas modifiés.
Les caractères accentués sont normalisés avant le traitement afin d’assurer la compatibilité avec l’alphabet ASCII classique.

---

## Brute-force

Le mode brute-force teste automatiquement les 26 décalages possibles du chiffrement de César et retourne tous les résultats possibles sous forme de dictionnaire Python.

---

## Tests unitaires

Des tests unitaires ont été réalisés avec `pytest` afin de vérifier :
- les clés positives ;
- les clés négatives ;
- la clé nulle ;
- le chiffrement/déchiffrement complet ;
- le fonctionnement du brute-force.

---

## Utilisation de GitHub

Le développement a été réalisé avec des branches Git et des commits progressifs afin de faciliter :
- le suivi des fonctionnalités ;
- les corrections de bugs ;
- la collaboration entre les membres de l’équipe.

Exemple de branche utilisée :
```text
feat/cesar
```

---

# Structure du projet

```text
equipe-5-Caesar/
│
├── main.py
├── README.md
├── requirements.txt
├── TESTS_GUIDE.md
│
├── tests/
│   └── test_caesar.py
│
└── message.txt
```

---

# Distribution des tâches

Les membres de l’équipe ont collaboré sur les différentes parties du projet, notamment :

- l’implémentation du chiffrement César classique ;
- l’implémentation du déchiffrement César ;
- l’implémentation du chiffrement Enigma César ;
- le développement du mode brute-force ;
- la gestion des clés positives, négatives et nulles ;
- la gestion des fichiers texte ;
- l’intégration des arguments en ligne de commande avec `argparse` ;
- la création et l’exécution des tests unitaires `pytest` ;
- la validation et les essais du programme ;
- l’utilisation des branches Git et des commits progressifs ;
- la documentation du projet dans le `README.md` ;
- la préparation du rapport du projet.

Chaque membre a participé à la conception, au développement, aux tests et à la validation des différentes fonctionnalités du programme.

---

# Auteurs

- Ogechi Amajuoyi
- Asma Brik
- Nada Chaouachi

---


# Références

- Documentation officielle Python :
  https://docs.python.org/3/

- Documentation argparse :
  https://docs.python.org/3/library/argparse.html

- Documentation pytest :
  https://docs.pytest.org/

- Documentation string :
  https://docs.python.org/3/library/string.html
