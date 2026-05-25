"""
MGA802 — Mini-Projet A : Chiffrement de César
Bienvenue au script d'automatisation du chiffrement/dechiffrement par décalage
"""

import argparse
import unicodedata

# On importe le module string parce qu'il contient des chaînes utiles,
# comme l'alphabet en minuscules et l'alphabet en majuscules.
import string

# Constante contenant toutes les lettres minuscules de l'alphabet anglais.
# On l'utilise pour trouver la position d'une lettre minuscule.
ALPHABET_MIN = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"

# Constante contenant toutes les lettres majuscules de l'alphabet anglais.
# On l'utilise pour préserver les majuscules pendant le chiffrement.
ALPHABET_MAJ = string.ascii_uppercase  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Séparer les lettres de leurs accents
def enlever_accents(mot: str):

    mot = unicodedata.normalize('NFKD', mot)
    resultat = []

    # Filtrer pour ne garder que les vraies lettres
    for char in mot:
        if not unicodedata.combining(char):
            resultat.append(char)

    return ''.join(resultat)


def chiffrer(message: str, cle: int) -> str:
    """
    Chiffre un message avec le chiffrement de César.

    Paramètres :
        message : le texte à chiffrer
        cle : le décalage à appliquer aux lettres

    Retour :
        Le message chiffré
    """

    # On crée une chaîne vide qui recevra progressivement le message chiffré.
    resultat = ""
    message = enlever_accents(message)

    # On parcourt chaque caractère du message original, un par un.
    for caractere in message:

        # Si le caractère est une lettre minuscule, on applique le décalage
        # dans l'alphabet minuscule.
        if caractere in ALPHABET_MIN:

            # On cherche la position de la lettre dans l'alphabet.
            # Exemple : "a" est à la position 0, "b" à 1, "c" à 2.
            position = ALPHABET_MIN.find(caractere)

            # On calcule la nouvelle position après le décalage.
            # Le modulo 26 permet de revenir au début de l'alphabet
            # si on dépasse la lettre "z".
            nouvelle_position = (position + cle) % 26

            # On récupère la nouvelle lettre à cette position
            # et on l'ajoute au résultat.
            resultat += ALPHABET_MIN[nouvelle_position]

        # Si le caractère est une lettre majuscule, on applique la même logique
        # mais avec l'alphabet majuscule pour préserver la casse.
        elif caractere in ALPHABET_MAJ:

            # On cherche la position de la lettre majuscule.
            position = ALPHABET_MAJ.find(caractere)

            # On calcule la nouvelle position avec le même principe.
            nouvelle_position = (position + cle) % 26

            # On ajoute la nouvelle lettre majuscule au résultat.
            resultat += ALPHABET_MAJ[nouvelle_position]

        # Si le caractère n'est pas une lettre de l'alphabet,
        # par exemple une virgule, un espace, un accent ou un point,
        # on le garde tel quel.
        else:
            resultat += caractere

    # Quand tous les caractères ont été traités,
    # on retourne le message chiffré complet.
    return resultat


def dechiffrer(message: str, cle: int) -> str:
    """
    Déchiffre un message chiffré avec le chiffrement de César.

    Le déchiffrement applique le décalage inverse.
    Si le chiffrement utilise +cle, le déchiffrement utilise -cle.
    """

    return chiffrer(message, -cle)

def brute_force_cesar(message: str) -> dict:
    """
    Teste toutes les clés possibles du chiffrement de César.

    Paramètre :
        message : le message chiffré

    Retour :
        Un dictionnaire contenant chaque clé testée et le message déchiffré correspondant.
    """

    resultats = {}

    for cle in range(26):
        message_dechiffre = dechiffrer(message, cle)
        resultats[cle] = message_dechiffre

    return resultats


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
        if lettre_min in ALPHABET_MIN:

            # choisir la clé
            cle_actuelle = cles[index_cle % 3]

            # position de la lettre
            position = ALPHABET_MIN.find(lettre_min)

            # Attribuer la nouvelle position
            nouvelle_position = (position + cle_actuelle) % 26

            # Recuperer la nouvelle lettre
            nouvelle_lettre = ALPHABET_MIN[nouvelle_position]

            # conserver les majuscules
            if lettre.isupper():
                nouvelle_lettre = nouvelle_lettre.upper()

            resultat.append(nouvelle_lettre)

            # Passer à une autre clé
            index_cle += 1

        else:
            resultat.append(lettre)

    return ''.join(resultat)


# Fonction pour déchiffre un message Enigma César en utilisant les clés inversées.

def enigma_dechiffrer(message: str, cles):
    cles_inversees = (-cles[0], -cles[1], -cles[2])
    return enigma_chiffrer(message, cles_inversees)



# Fonction qui essaye toutes les clés possibles du chiffrement Enigma pour trouver le message original
def brute_force_enigma(message: str):
    resultats = []

    # Tester toutes les valeurs possibles pour la première clé
    for cle1 in range(26):

        # Tester toutes les valeurs possibles pour la deuxième clé
        for cle2 in range(26):

            # Tester toutes les valeurs possibles pour la troisième clé
            for cle3 in range(26):

                # Créer un tuple contenant les 3 clés
                cles = (cle1, cle2, cle3)

                # Déchiffrer le message
                # On utilise les clés négatives pour inverser le chiffrement
                texte = enigma_chiffrer(
                    message,
                    (-cle1, -cle2, -cle3)
                )

                resultats.append((cles, texte))

    return resultats


# Lire un fichier texte
def lire_fichier(nom_fichier: str):

    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        return fichier.read()


def ecrire_fichier(nom_fichier: str, contenu: str):

    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        fichier.write(contenu)
        

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
		choices=["chiffrer", "dechiffrer", "bruteforce", "enigma"],
		help="Opération à effectuer (chiffrer, dechiffrer, bruteforce ou enigma).")

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

	if args.action == "chiffrer":
		# L'utilisateur veut chiffrer : on appelle chiffrer()
		resultat = chiffrer(args.message, cle)
	elif args.action == "dechiffrer":
		# L'utilisateur veut déchiffrer : on appelle dechiffrer()
		resultat = dechiffrer(args.message, cle)
	elif args.action == "bruteforce":
		# L'utilisateur veut utiliser la force brute César : on appelle brute_force_cesar()
		resultat = brute_force_cesar(args.message)
	else:  # args.action == "enigma"
		# L'utilisateur veut utiliser Enigma César : on appelle enigma_chiffrer()
		resultat = enigma_chiffrer(args.message, cle)

	# === ÉTAPE 6 : Afficher le résultat ===
	# print() affiche le résultat à l'écran pour que l'utilisateur le voie.
	print(resultat)


if __name__ == "__main__":
    main()
