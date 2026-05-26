# MGA802 — Mini-Projet A — Équipe 5

# Chiffrement César et Enigma César

---

# 1. Description du programme

Ce projet consiste à développer un programme Python capable de :

- Chiffrer un message avec le chiffrement de César
- Déchiffrer un message
- Utiliser une version améliorée appelée **Enigma César**
- Réaliser une attaque brute-force
- Mesurer les performances du programme

Le programme utilise les arguments de ligne de commande (`argparse`) afin de permettre une utilisation simple et flexible.

---

# 2. Fonctionnalités du programme

## Chiffrement César

Le chiffrement de César consiste à décaler chaque lettre de l’alphabet selon une clé donnée.

### Exemple

```bash
python main.py chiffrer "bonjour" -c 3
```

### Résultat

```text
erqmrxu
```

---

## Déchiffrement César

Permet de retrouver le message original.

### Exemple

```bash
python main.py dechiffrer "erqmrxu" -c 3
```

### Résultat

```text
bonjour
```

---

## Enigma César

Version améliorée utilisant 3 clés différentes qui changent à chaque lettre.

### Exemple

```bash
python main.py enigma "Bonjour" -c 7-16-9
```

---

## Brute-force César

Teste automatiquement toutes les clés possibles.

### Exemple

```bash
python main.py bruteforce_cesar "erqmrxu"
```

---

## Brute-force Enigma

Teste toutes les combinaisons possibles des 3 clés.

### Exemple

```bash
python main.py bruteforce_enigma "message"
```

---

# 3. Installation

## Prérequis

- Python 3 installé sur votre ordinateur

### Vérification

```bash
python --version
```

---

# 4. Exécution du programme

Ouvrir un terminal dans le dossier du projet puis exécuter :

```bash
python main.py
```

---

# 5. Exemples d’utilisation

## Chiffrer un message

```bash
python main.py chiffrer "Bonjour à tous" -c 5
```

---

## Déchiffrer un message

```bash
python main.py dechiffrer "Gtsotzw f ytzx" -c 5
```

---

## Utiliser Enigma César

```bash
python main.py enigma "Maison" -c 7-16-9
```

---

## Mesurer le temps d’exécution

```bash
python main.py bruteforce_cesar "erqmrxu" --timeit
```

---

# 6. Structure du projet

```text
equipe-5-Caesar/
│
├── main.py
├── README.md
├── TESTS_GUIDE.md
├── requirements.txt
├── message.txt
│
├── tests/
│   └── test_caesar.py
│
└── .gitignore
```

---

# 7. Choix de conception

## Gestion des accents

Les accents sont supprimés grâce au module `unicodedata`.

### Exemple

```text
é → e
à → a
ç → c
```

Cela permet d’éviter les erreurs lors du chiffrement.

---

## Gestion des majuscules

Le programme conserve les majuscules originales.

### Exemple

```text
Bonjour → Erqmrxu
```

---

## Conservation de la ponctuation

Les espaces, chiffres et symboles ne sont pas modifiés.

### Exemple

```text
Bonjour ! → Erqmrxu !
```

---

## Utilisation de fonctions

Le programme est structuré avec plusieurs fonctions afin de :

- rendre le code plus lisible
- faciliter les tests
- améliorer la maintenance du projet

---

# 8. Technologies utilisées

- Python 3
- argparse
- unicodedata
- string
- timeit

---

# 9. Tests

Les tests automatiques sont disponibles dans :

```text
tests/test_caesar.py
```

Pour lancer les tests :

```bash
pytest
```

---

# 10. Auteurs

Projet réalisé par :

- 
- Asma Brik
- Ajouter les autres membres de l’équipe

---

# 11. Conclusion

Ce projet nous a permis de :

- comprendre le fonctionnement du chiffrement de César
- manipuler des chaînes de caractères en Python
- utiliser les arguments de ligne de commande
- développer un système de chiffrement polyalphabétique
- réaliser des tests et mesurer les performances du programme
