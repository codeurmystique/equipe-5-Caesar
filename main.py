"""
MGA802 — Mini-Projet A : Chiffrement de César
Bienvenue au script d'automatisation du chiffrement/dechiffrement par décalage
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

# Fonction de chiffrement Enigma César utilisant 3 clés différentes
def enigma_chiffrer(message: str, cles):

    if len(cles) != 3:
        return "Tu dois utiliser exactement 3 clés"

    message_normalise = enlever_accents(message)
    resultat = []
    index_cle = 0

    for lettre in message_normalise:
        lettre_min = lettre.lower()

        if lettre_min in ALPHABET:
            cle_actuelle = cles[index_cle % 3]

            position = ALPHABET.find(lettre_min)
            nouvelle_position = (position + cle_actuelle) % 26
            nouvelle_lettre = ALPHABET[nouvelle_position]

            if lettre.isupper():
                nouvelle_lettre = nouvelle_lettre.upper()

            resultat.append(nouvelle_lettre)
            index_cle += 1

        else:
            resultat.append(lettre)

    return "".join(resultat)


# Fonction de déchiffrement Enigma César utilisant les clés inversées
def enigma_dechiffrer(message: str, cles):

    cles_inversees = (-cles[0], -cles[1], -cles[2])
    return enigma_chiffrer(message, cles_inversees)


# Fonction qui essaie toutes les clés possibles du chiffrement César
def brute_force_cesar(message: str):

    resultats = []

    for cle in range(26):
        texte = dechiffrer(message, cle)
        resultats.append((cle, texte))

    return resultats


# Fonction qui essaie toutes les combinaisons possibles des 3 clés Enigma César
def brute_force_enigma(message: str):

    resultats = []

    for cle1 in range(26):
        for cle2 in range(26):
            for cle3 in range(26):
                cles = (cle1, cle2, cle3)
                texte = enigma_dechiffrer(message, cles)
                resultats.append((cles, texte))

    return resultats



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
    if "-" in texte.lstrip("-"):

        # Si oui, c'est une clé Enigma César
        return tuple(int(x) for x in texte.split("-"))

    # Sinon, c'est une clé César simple
    return int(texte)


def main(argv=None):
    """Point d'entrée principal du programme en ligne de commande."""

    # === ÉTAPE 1 : Créer et configurer le parseur d'arguments ===
    parser = argparse.ArgumentParser(
        description="Mini-Projet A : chiffrement de César / Enigma César."
    )

    # === ÉTAPE 2 : Définir les arguments attendus ===

    parser.add_argument(
        "action",
        choices=[
            "chiffrer",
            "dechiffrer",
            "enigma",
            "bruteforce_cesar",
            "bruteforce_enigma"
        ],
        help="Opération à effectuer."
    )

    parser.add_argument(
        "message",
        help="Texte à traiter (mettez-le entre guillemets)."
    )

    parser.add_argument(
        "-c",
        "--cle",
        required=False,
        help="Clé : un entier (ex. '42') ou 'a-b-c' (ex. '7-16-9') pour Enigma."
    )

    # === ÉTAPE 3 : Analyser les arguments ===
    args = parser.parse_args(argv)

    # === ÉTAPE 4 : Convertir la clé ===
    cle = None

    if args.cle:
        cle = _parse_cle(args.cle)

    # === ÉTAPE 5 : Choisir et exécuter l'opération ===

    if args.action == "chiffrer":

        # Appeler la fonction chiffrer
        resultat = chiffrer(args.message, cle)

        print(resultat)

    elif args.action == "dechiffrer":

        # Appeler la fonction dechiffrer
        resultat = dechiffrer(args.message, cle)

        print(resultat)

    elif args.action == "enigma":

        # Appeler la fonction enigma
        resultat = enigma_chiffrer(args.message, cle)

        print(resultat)

    elif args.action == "bruteforce_cesar":

        resultat = brute_force_cesar(args.message)

        for cle, texte in resultat:
            print(f"Clé {cle} : {texte}")

    elif args.action == "bruteforce_enigma":

        resultat = brute_force_enigma(args.message)

        for cles, texte in resultat:
            print(f"Clés {cles} : {texte}")


# TODO : Une fois les fonctions de base implémentées, vous pourrez :
# - Ajouter des options pour lire/écrire depuis des fichiers
# - Implémenter le mode brute-force
# - Ajouter d'autres fonctionnalités


if __name__ == "__main__":
    main()