"""Tests pour le Mini-Projet A.
equipe 5 caesar

"""

# ---------- Chaînes de test officielles — César (spec §7) ----------

from main import chiffrer, dechiffrer, enigma_chiffrer, lire_fichier, ecrire_fichier


# ---------------------------
# 1. Test des majuscules
# ---------------------------
def test_majuscules():

    assert chiffrer("Bonjour", 3) == chiffrer("BONJOUR", 3)


# ---------------------------
# 2. Test accents + ponctuation
# ---------------------------
def test_accents_ponctuation():

    message = "éèê à, ça!"
    resultat = chiffrer(message, 2)

    # doit supprimer les accents mais garder ponctuation
    assert "g" in resultat
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


# ---------------------------
# 8. Test identité (clé = 0)
# ---------------------------
def test_cle_zero():

    assert chiffrer("bonjour", 0) == "bonjour"


# ---------- Chaîne de test officielle — Enigma César ----------


# ---------------------------
# 9. Test Enigma César simple
# ---------------------------
def test_enigma_simple():

    resultat = enigma_chiffrer("abc", [1, 2, 3])

    assert resultat == "bdf"


# ---------------------------
# 10. Test Enigma avec ponctuation
# ---------------------------
def test_enigma_ponctuation():

    resultat = enigma_chiffrer("bonjour!", [1, 2, 3])

    assert "!" in resultat


# ---------------------------
# 11. Test Enigma conserve majuscules
# ---------------------------
def test_enigma_majuscules():

    resultat = enigma_chiffrer("BONJOUR", [1, 2, 3])

    assert resultat.isupper()


# ---------------------------
# 12. Test Enigma mauvaise clé
# ---------------------------
def test_enigma_mauvaise_cle():

    resultat = enigma_chiffrer("bonjour", [1, 2])

    assert resultat == "Tu dois utiliser exactement 3 clés"


# ---------------------------
# 13. Test Enigma clé négative
# ---------------------------
def test_enigma_cle_negative():

    resultat = enigma_chiffrer("abc", [-1, -2, -3])

    assert isinstance(resultat, str)


# ---------------------------
# 14. Test chaîne vide
# ---------------------------
def test_chaine_vide():

    assert chiffrer("", 5) == ""


# ---------------------------
# 15. Test espaces
# ---------------------------
def test_espaces():
    resultat = chiffrer("a b c", 1)
    assert " " in resultat


# ---------------------------
# 16. Test lire ecrire
# ---------------------------
def test_lire_ecrire_fichier():
    ecrire_fichier("test.txt", "bonjour")
    contenu = lire_fichier("test.txt")
    assert contenu == "bonjour"


# TODO : ajoutez vos propres tests ci-dessous
#  - test brute-force César
#  - test brute-force Enigma César
#  - autres cas limites

