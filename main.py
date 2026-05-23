"""
MGA802 — Mini-Projet A : Chiffrement de César
Bienvennue au script d'automatisation du chiffrement/dechiffrement par décalage
"""

import argparse
import unicodedata
import string

# Variable global pour simplifier l'acces dans les fonctions
ALPHABET = string.ascii_lowercase


# Séparer les lettres de leurs accents
def enlever_accents(mot: str):

    mot = unicodedata.normalize('NFKD', mot)
    resultat = []

    # Filtrer pour ne garder que les vraies lettres
    for char in mot:
        if not unicodedata.combining(char):
            resultat.append(char)

    return ''.join(resultat)


# Introduire une fonction chiffrer
def chiffrer(mot: str, cles: int):

    # Chiffrer le mot en appliquant le decalage de césar
    mot = enlever_accents(mot.lower())

    resultat = []

    for lettre in mot:

        if lettre in ALPHABET:

            position = ALPHABET.find(lettre)

            # Introduire une nouvelle position et appliquer le decalage modulo 26
            nouvelle_position = (position + cles) % 26

            # Introduire une nouvelle lettre
            nouvelle_lettre = ALPHABET[nouvelle_position]

            resultat.append(nouvelle_lettre)

        else:
            # sinon resultat conserve la lettre
            resultat.append(lettre)

    return ''.join(resultat)


# Introduire une fonction de dechiffrement
def dechiffrer(mot: str, cles: int):

    return chiffrer(mot, -cles)


# Fonction Enigma César
def enigma_chiffrer(message: str, cles):

    if len(cles) != 3:
        return "Tu dois utiliser exactement 3 clés"

    message_normalise = enlever_accents(message)

    # Compteur indice
    index_cle = 0

    resultat = []

    # parcourir chaque lettre
    for lettre in message_normalise:

        lettre_min = lettre.lower()

        # Vérifier si une lettre alphabétique
        if lettre_min in ALPHABET:

            # choisir la clé
            cle_actuelle = cles[index_cle % 3]

            # position de la lettre
            position = ALPHABET.find(lettre_min)

            # Attribuer la nouvelle position
            nouvelle_position = (position + cle_actuelle) % 26

            # Recuperer la nouvelle lettre
            nouvelle_lettre = ALPHABET[nouvelle_position]

            # conserver les majuscules
            if lettre.isupper():
                nouvelle_lettre = nouvelle_lettre.upper()

            resultat.append(nouvelle_lettre)

            # Passer à une autre clé
            index_cle += 1

        else:
            resultat.append(lettre)

    return ''.join(resultat)


def enigma_dechiffrer(message: str, cles):
    cles_inversees = (-cles[0], -cles[1], -cles[2])
    return enigma_chiffrer(message, cles_inversees)

#Lire un fichier texte
def lire_fichier(nom_fichier: str):

    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        return fichier.read()

def ecrire_fichier(nom_fichier: str, contenu: str):

    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        fichier.write(contenu)


# Fonction qui essaye toutes les clés possibles du chiffrement César pour trouver le message original

def brute_force_cesar(message: str):
    resultat = []
    # Tester toutes les clés possibles de 0 à 25
    for cle in range(26):
        texte = dechiffrer(message, cle)
        resultat.append((cle, texte))
    return resultat


# Fonction qui essaye toutes les clés possibles du chiffrement Enigma pour trouver le message original

def brute_force_enigma(message: str):
    resultats = []
    message_normalise = enlever_accents(message)
    # Tester toutes les valeurs possibles pour la première clé
    for cle1 in range(26):
        # Tester toutes les valeurs possibles pour la deuxième clé
        for cle2 in range(26):
            # Tester toutes les valeurs possibles pour la troisième clé
            for cle3 in range(26):
                # Créer un tuple contenant les 3 clés
               cles = (cle1, cle2, cle3)

               texte = enigma_chiffrer(message_normalise,
                                       (-cle1, -cle2, -cle3)
               )

               resultats.append((cles,texte))
return "resultats"


def _parse_cle(texte: str):
    """Convertit l'argument --cle en clé utilisable.

    Cette fonction analyse la clé fournie par l'utilisateur en ligne de commande
    et la transforme en type Python approprié :
    - César           : un entier, ex. "42" ou "-42"
    - Enigma César    : trois entiers séparés par des tirets, ex. "7-16-9"

    Paramètre :
        texte (str) : la chaîne saisie par l'utilisateur après --cle.

    Retour :
        int : une clé entière pour César
        tuple : un tuple de 3 entiers pour Enigma César

    Exemple :
        _parse_cle("42") → 42 (int)
        _parse_cle("7-16-9") → (7, 16, 9) (tuple)
    """
    # Vérifier s'il y a un tiret dans la clé (sauf si c'est juste un signe négatif).
    # lstrip("-") enlève tous les tirets au début, pour distinguer :
    #   "-42" (entier négatif, pas de tiret après le signe)
    #   "7-16-9" (trois nombres séparés par des tirets)
    if "-" in texte.lstrip("-"):
        # Si oui, c'est une clé Enigma César : on coupe au niveau du "-" et on convertit en entiers.
        return tuple(int(x) for x in texte.split("-"))
    # Sinon, c'est une clé César simple : on convertit en entier.
    return int(texte)


# choisir l'action nécessaire

if args.action == "chiffrer" :

    # Appeler la fonction chiffrer
    resultat = chiffrer(args.message, cle)
    print(resultat)

elif args.action== "dechiffrer" :
    # Appeler la fonction dechiffrer
    resultat = dechiffrer(args.message, cle)
    print(resultat)

else:
# Appeler la fonction enigma
   resultat = enigma_chiffrer(args.message, cle)
   print(resultat)


def main(argv=None):
    """Point d'entrée principal du programme en ligne de commande.

    Cette fonction :
    1. Parse les arguments saisis par l'utilisateur (action, message, clé)
    2. Convertit la clé en type approprié (int ou tuple)
    3. Appelle la fonction correspondante (chiffrer, dechiffrer ou enigma_chiffrer)
    4. Affiche le résultat

    Paramètre :
        argv (list ou None) : si None, utilise sys.argv (arguments de la console).
                              si list, utilise les arguments fournis (utile pour les tests).

    Exemples d'utilisation en terminal :
        python main.py chiffrer "Veni, vidi, vici!" --cle 42
        python main.py dechiffrer "Ludy, lyty, lysy!" --cle 42
        python main.py enigma "MAISON" --cle 7-16-9
    """
    # === ÉTAPE 1 : Créer et configurer le parseur d'arguments ===
    # argparse est un module qui aide à gérer les arguments en ligne de commande.
    # ArgumentParser crée un analyseur personnalisé pour notre programme.
    parser = argparse.ArgumentParser(
        description="Mini-Projet A : chiffrement de César / Enigma César.")

    # === ÉTAPE 2 : Définir les arguments attendus ===

    # Argument positionnel "action" : l'opération à effectuer.
    # - Obligatoire (pas de -- devant)
    # - Doit être l'une des valeurs listées dans "choices"
    parser.add_argument(
        "action",
        choices=["chiffrer", "dechiffrer", "enigma"],
        help="Opération à effectuer (chiffrer, dechiffrer ou enigma).")

    # Argument positionnel "message" : le texte à traiter.
    # - Obligatoire
    # - C'est la chaîne que nous allons chiffrer ou déchiffrer
    parser.add_argument(
        "message",
        help="Texte à traiter (mettez-le entre guillemets).")

    # Argument optionnel "--cle" (abréviation "-c") : la clé de chiffrement.
    # - Obligatoire via required=True
    # - Peut être un entier (César) ou trois entiers séparés par des tirets (Enigma César)
    parser.add_argument(
        "-c", "--cle", required=True,
        help="Clé : un entier (ex. '42') ou 'a-b-c' (ex. '7-16-9') pour Enigma.")

    # === ÉTAPE 3 : Analyser les arguments ===
    # parse_args() transforme les arguments en un objet "Namespace" avec des attributs.
    # Si argv=None, il lit automatiquement depuis la ligne de commande.
    # Sinon, il utilise la liste fournie.
    args = parser.parse_args(argv)

    # Maintenant, on peut accéder aux arguments via :
    # - args.action (ex. "chiffrer")
    # - args.message (ex. "Veni, vidi, vici!")
    # - args.cle (ex. "42" ou "7-16-9", toujours en chaîne de caractères)

    # === ÉTAPE 4 : Convertir la clé (texte) en type approprié ===
    # _parse_cle() transforme la clé en int (César) ou tuple (Enigma).
    cle = _parse_cle(args.cle)

    # === ÉTAPE 5 : Choisir et exécuter l'opération ===
    # Selon l'action, on appelle la fonction appropriée.
    # (Une fois que chiffrer / dechiffrer / enigma_chiffrer seront implémentées,
    #  ces appels retourneront le résultat du chiffrement/déchiffrement.)





# TODO : Une fois les fonctions de base implémentées, vous pourrez :
# - Ajouter des options pour lire/écrire depuis des fichiers
# - Implémenter le mode brute-force
# - Ajouter d'autres fonctionnalités


if __name__ == "__main__":
    main()