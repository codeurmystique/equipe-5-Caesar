# MG802 — Mini-Projet A - Equipe 5

## Chiffrement César et Enigma César


---

# 1. Introduction

Ce rapport présente la documentation relative à un programme Python permettant de réaliser différentes opérations de chiffrement et de déchiffrement basées sur le chiffrement de César ainsi que sur une version simplifiée d’Enigma César.

nous allons détailler :

- la structure du programme ;
- les stratégies algorithmiques retenues, en particulier pour le brute force ;
- l’évaluation de l’efficacité du programme (temps d’exécution, etc.) ;
- la distribution des tâches au sein de l’équipe

---

# 2. Structure du programme

Le programme permet à l’utilisateur de :

- chiffrer un message avec le chiffrement de César ;
- déchiffrer un message ;
- utiliser le mode Enigma César avec trois clés différentes ;
- appliquer un brute force pour essayer toutes les clés possibles ;
- lancer les opérations directement depuis le terminal grâce au module `argparse`.

Le projet est principalement organisé dans un fichier `main.py` contenant les différentes fonctions du programme.

Les fonctions principales développées sont :

| Fonction | Rôle |
|---|---|
| `chiffrer()` | Chiffre un message avec le décalage de César |
| `dechiffrer()` | Déchiffre un message |
| `enigma_chiffrer()` | Applique le chiffrement Enigma César |
| `enigma_dechiffrer()` | Déchiffre un message Enigma |
| `brute_force_cesar()` | Applique l'approche brute force pour trouver la clé de chiffrement César |
| `brute_force_enigma()` | Applique l'approche brute force pour trouver la clé de chiffrement Enigma |
| `_parse_cle()` | Convertit l'argument --cle en clé utilisable |
| `main()` | La fonction point d'entrée du programme de chiffrement |

Le programme utilise également :

- le module `string` pour accéder facilement à l’alphabet ;
- le module `unicodedata` pour retirer les accents ;
- le module `argparse` pour lancer les commandes depuis le terminal.

## Exemple d’utilisation

```bash
python main.py chiffrer "Bonjour" --cle 3
```

Résultat :

```text
Erqmrxu
```

Le mode Enigma César utilise trois clés différentes appliquées successivement sur les lettres du message.

Exemple :

```text
(7,16,9)
```

Les décalages se répètent selon le modèle :

```text
7 → 16 → 9 → 7 → 16 → 9 ...
```

---

# 3. Stratégies algorithmiques utilisées

## 3.1 Chiffrement de César

Le chiffrement de César consiste à déplacer chaque lettre d’un certain nombre de positions dans l’alphabet.

Exemple:
```text
Clé : (3)
```

```text
A → D
B → E
C → F
D → G
...
```

Le programme calcule la nouvelle position grâce à l’opération modulo 26 :

""" python
nouvelle_position = (position + cle) % 26
""""

L’utilisation du modulo permet de revenir au début de l’alphabet lorsque la fin est atteinte.

Les accents sont retirés afin de simplifier le traitement des caractères.

---

## 3.2 Enigma César

Le mode Enigma César est une version simplifiée inspirée de la machine Enigma historique.

Enigma César utilise trois clés différentes,Contrairement au chiffrement de César classique qui utilise une seule clé.

Exemple :

```text
Clés : (7,16,9)
```

Chaque lettre du message utilise la clé suivante de manière cyclique.

| Position | Clé utilisée |
|---|---|
| 1 | 7 |
| 2 | 16 |
| 3 | 9 |
| 4 | 7 |
| 5 | 16 |

Cette approche augmente la complexité du chiffrement et rend le décryptage plus difficile qu’avec un simple décalage fixe.

---

## 3.3 Brute force

Le brute force consiste à essayer automatiquement toutes les clés possibles afin de retrouver le message original.

### César

Le chiffrement César possède seulement 26 clés possibles :

```text
0 à 25
```

Le programme teste donc chaque clé puis affiche le résultat correspondant.

### Enigma César

Pour Enigma César, chaque clé peut prendre 26 valeurs possibles :

```text
26 × 26 × 26 = 17 576 combinaisons
```

Le programme utilise trois boucles imbriquées pour tester toutes les combinaisons possibles.

---

# 4. Évaluation des performances


| Fonction | temps d’exécution |
|---|------|
| `chiffrer()` | 0,04s|
| `dechiffrer()` | 0.04s |
| `enigma_chiffrer()` | 0.025s |
| `enigma_dechiffrer()` | 0.02s |
| `brute_force_cesar()` | 0.03s |
| `brute_force_enigma()` | 0.15s |


Le brute force César est très rapide puisqu’il ne teste que 26 possibilités.

Le brute force Enigma est plus coûteux puisque le programme doit analyser 17 576 combinaisons.

Les temps d’exécution ont été mesurés avec :

```python
from time import perf_counter
```

Les tests montrent que le brute force Enigma demande beaucoup plus de calculs que le chiffrement César simple.

---

# 5. Travail d’équipe et conclusion

Le projet a été réalisé de manière collaborative à l’aide de GitHub.

Chaque membre de l’équipe a contribué :

- Au développement ;
- Aux tests ;
- A l’amélioration du code ;
- A la rédaction du README ;
- A l’ajout des commentaires.

Les principales tâches réalisées étaient :

- développement des fonctions de chiffrement ;
- implémentation du brute force ;
- création des tests unitaires ;
- validation des fonctionnalités avec `pytest`.

Ce projet nous a permis de développer plusieurs compétences importantes, essentiellement:

- création de fonctions Python ;
- Manipulation de GitHub ;
- débogage et tests unitaires.

# Auteurs 

- Nada Chaouachi
- Asma Brik
- Amajuoyi Ogechi


# Références

- Documentation officielle Python :
  https://docs.python.org/3/

- Documentation argparse :
  https://docs.python.org/3/library/argparse.html

- Documentation pytest :
  https://docs.pytest.org/

- Documentation string :
  https://docs.python.org/3/library/string.html
