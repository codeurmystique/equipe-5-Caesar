"""
MGA802 — Mini-Projet A : Chiffrement de César
Bienvennue au script d'automatisation du chiffrement/dechiffrement par décalage
"""

import argparse
import timeit
import string
import unicodedata


# variable global pour simplifier l'acces dans les fonctions
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

    # Retirer les accents sans perdre les majuscules
    mot = enlever_accents(mot)

    resultat = []

    for lettre in mot:

        # Sauvegarder la casse originale
        est_majuscule = lettre.isupper()

        lettre_min = lettre.lower()

        if lettre_min in ALPHABET:

            position = ALPHABET.find(lettre_min)

            nouvelle_position = (position + cles) % 26

            nouvelle_lettre = ALPHABET[nouvelle_position]

            # remettre la majuscule si nécessaire
            if est_majuscule:
                nouvelle_lettre = nouvelle_lettre.upper()

            resultat.append(nouvelle_lettre)

        else:
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


# Lire un fichier texte
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

    result = []

    message_normalise = enlever_accents(message)

    # Tester toutes les valeurs possibles pour la première clé
    for cle1 in range(26):

        # Tester toutes les valeurs possibles pour la deuxième clé
        for cle2 in range(26):

            # Tester toutes les valeurs possibles pour la troisième clé
            for cle3 in range(26):

                # Créer un tuple contenant les 3 clés
                cles = (cle1, cle2, cle3)

                texte = enigma_chiffrer(
                    message_normalise,
                    (-cle1, -cle2, -cle3)
                )

                result.append((cles, texte))

    return result


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

#Fonction de performance
def mesurer_performance(action, message, cle):
    """Mesure le temps d'exécution de l'action demandée en utilisant timeit."""
    if action == "chiffrer":
        code = lambda: chiffrer(message, cle)
    elif action == "dechiffrer":
        code = lambda: dechiffrer(message, cle)
    elif action == "enigma":
        code = lambda: enigma_chiffrer(message, cle)
    elif action == "bruteforce_cesar":
        code = lambda: brute_force_cesar(message)
    elif action == "bruteforce_enigma":
        code = lambda: brute_force_enigma(message)
    else:
        return

    # On réduit à 1 seule répétition pour la force brute Enigma (car 17 576 boucles c'est lourd)
    # Les autres actions s'exécutent 1 000 fois pour stabiliser la mesure
    repetitions = 1 if "bruteforce_enigma" in action else 1000

    temps_total = timeit.timeit(code, number=repetitions)
    temps_moyen = temps_total / repetitions

    print(f"\n--- Rapport de Performance (timeit) ---")
    print(f"Action mesurée     : {action}")
    print(f"Répétitions        : {repetitions}")
    print(f"Temps total        : {temps_total:.6f} secondes")
    print(f"Temps moyen / éval : {temps_moyen:.6f} secondes")

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

    parser.add_argument(
        "--timeit",
        action="store_true",
        help="Mesurer le temps d'exécution"
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
        resultat = dechiffrer(args.message,cle)

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

    import sys

    if len(sys.argv) == 1:

        print("Exemple d'utilisation :")
        print('python main.py chiffrer "bonjour" -c 3')
        print('python main.py enigma "MAISON" -c 7-16-9')
        print('python main.py bruteforce_cesar "erqmrxu" --timeit')

    else:
        main()
