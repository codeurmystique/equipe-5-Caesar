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

- Chiffrer un message avec le chiffrement de César ;
- Déchiffrer un message en utilisant la techniqiue César ;
- Utiliser le mode Enigma César avec trois clés différentes ;
- Appliquer un brute force pour essayer toutes les clés possibles ;
- Lancer les opérations directement depuis le terminal grâce au module `argparse`.

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
| `chiffrer()` | 2.3 us|
| `dechiffrer()` | 2.5 us |
| `enigma_chiffrer()` | 3 us |
| `enigma_dechiffrer()` | 3.1 us |
| `brute_force_cesar()` | 60.1 us |
| `brute_force_enigma()` | 53.05 ms |

Le chiffrement César (2.3 us) est légerment plus rapide que le chiffrement Enigma (3 us)

De manière similaire, le déchiffrement César (2.5 us) est légerment plus rapide que le déchiffrement Enigma (3.1 us)

Les tests montrent que la brute force Enigma (53 ms) demande beaucoup plus de temps d'éxécution que la brute force César (60.1 us). 

En effet, la technique brute force Enigma nécéssite 883 (53/0.06) fois plus de temps d'éxécution que la technique brute force César.

La brute force César est très rapide puisqu’elle ne calcul que 26 possibilités.

La brute force Enigma est beaucoup plus coûteuse puisqu'elle doit calculer 17 576 combinaisons.

Les temps d’exécution ont été mesurés avec le module timeit:

```python
from timeit import timeit
from main import brute_force_cesar
timeit('brute_force_cesar(message_chiffre)', globals=globals(), number=1000)
```

NB: 
1) Afin de  mesurer les temps d'exécution des fonctions, nous avons utilisé la chaine de caractère "MAISON" avec les clés suivantes, pour couvrir les boucles de chiffrement-déchiffrement César et Enigma:
- César: clé = 42
- Enigma: clés = 42, 21, 7
2) les chiffres listés dans le tableau ci-dessus représentent la moyenne de temps d'éxécution sur 1000 itérations
3) Ordinateur utilisé: Dell Pro 14 Plus

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
