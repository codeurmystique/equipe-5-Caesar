"""
Tests pour le Mini-Projet A.
Equipe 5 Caesar
"""

import os

from main import (
    chiffrer,
    dechiffrer,
    enigma_chiffrer,
    lire_fichier,
    ecrire_fichier,
)

# =========================================================
#                 TESTS CHIFFREMENT CÉSAR
# =========================================================


# ---------------------------
# 1. Test des majuscules
# ---------------------------
def test_majuscules():
    def test_majuscules():
        assert chiffrer("BONJOUR", 3) == "ERQMRXU"
        assert chiffrer("Bonjour", 3) == "Erqmrxu"


# ---------------------------
# 2. Test accents + ponctuation
# ---------------------------
def test_accents_ponctuation():

    message = "éèê à, ça!"
    resultat = chiffrer(message, 2)

    # accents supprimés
    assert "é" not in resultat

    # ponctuation conservée
    assert "," in resultat
    assert "!" in resultat


# ---------------------------
# 3. Test grandes clés positives
# ---------------------------
def test_grande_cle_positive():

    assert chiffrer("abc", 52) == "abc"


# ---------------------------
# 4. Test grandes clés négatives
# ---------------------------
def test_grande_cle_negative():

    assert chiffrer("abc", -26) == "abc"


# ---------------------------
# 5. Test chiffrement / déchiffrement
# ---------------------------
def test_chiffrement_dechiffrement():

    message = "bonjour test"
    cle = 5

    chiffre = chiffrer(message, cle)
    dechiffre = dechiffrer(chiffre, cle)

    assert dechiffre == "bonjour test"


# ---------------------------
# 6. Test majuscules + accents mix
# ---------------------------
def test_mix_complexe():

    message = "École de technologie supérieur !"
    chiffre = chiffrer(message, 4)

    assert isinstance(chiffre, str)
    assert "!" in chiffre


# ---------------------------
# 7. Test caractères non alphabétiques
# ---------------------------
def test_caracteres_speciaux():

    message = "1234 @@### abc"
    chiffre = chiffrer(message, 3)

    assert "1234" in chiffre
    assert "@" in chiffre
    assert "#" in chiffre


# ---------------------------
# 8. Test identité (clé = 0)
# ---------------------------
def test_cle_zero():

    assert chiffrer("bonjour", 0) == "bonjour"


# ---------------------------
# 9. Test chaîne vide
# ---------------------------
def test_chaine_vide():

    assert chiffrer("", 5) == ""


# ---------------------------
# 10. Test espaces
# ---------------------------
def test_espaces():

    resultat = chiffrer("a b c", 1)

    assert " " in resultat


# =========================================================
#                    TESTS ENIGMA
# =========================================================


# ---------------------------
# 11. Test Enigma simple
# ---------------------------
def test_enigma_simple():

    resultat = enigma_chiffrer("abc", [1, 2, 3])

    assert resultat == "bdf"


# ---------------------------
# 12. Test Enigma avec ponctuation
# ---------------------------
def test_enigma_ponctuation():

    resultat = enigma_chiffrer("bonjour!", [1, 2, 3])

    assert "!" in resultat


# ---------------------------
# 13. Test Enigma conserve majuscules
# ---------------------------
def test_enigma_majuscules():

    resultat = enigma_chiffrer("BONJOUR", [1, 2, 3])

    assert resultat.isupper()


# ---------------------------
# 14. Test Enigma mauvaise clé
# ---------------------------
def test_enigma_mauvaise_cle():

    resultat = enigma_chiffrer("bonjour", [1, 2])

    assert resultat == "Tu dois utiliser exactement 3 clés"


# ---------------------------
# 15. Test Enigma clé négative
# ---------------------------
def test_enigma_cle_negative():

    resultat = enigma_chiffrer("abc", [-1, -2, -3])

    assert isinstance(resultat, str)


# =========================================================
#                    TESTS FICHIERS
# =========================================================


# ---------------------------
# 16. Test lire / écrire fichier
# ---------------------------
def test_lire_ecrire_fichier():

    nom_test = "test_temporaire.txt"
    contenu_attendu = "bonjour"

    # Écriture puis lecture
    ecrire_fichier(nom_test, contenu_attendu)
    contenu_recu = lire_fichier(nom_test)

    # Nettoyage
    if os.path.exists(nom_test):
        os.remove(nom_test)

    assert contenu_recu == contenu_attendu


# ---------------------------
# 17. Test lecture message officiel
# ---------------------------
def test_lecture_message_officiel():

    # Création du fichier
    ecrire_fichier("message.txt", "Veni, vidi, vici!")

    contenu = lire_fichier("message.txt")

    assert "Veni" in contenu

    chiffre = chiffrer(contenu, 3)

    # veni -> yhql
    assert "yhql" in chiffre


# =========================================================
#               TEST PERFORMANCE (TIMEIT)
# =========================================================


# ---------------------------
# 18. Test performance
# ---------------------------
def test_performance_timeit(capsys):

    from main import mesurer_performance

    mesurer_performance("chiffrer", "test", 3)

    # Capture console
    console_output = capsys.readouterr().out

    assert "Rapport de Performance" in console_output
    assert "Temps total" in console_output


# TODO : ajoutez vos propres tests ci-dessous
# - test brute-force César
# - test brute-force Enigma César
# - autres cas limites
