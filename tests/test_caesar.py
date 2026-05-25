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
import os


# ---------------------------
# 17. Test lire ecrire
# ---------------------------
def test_lire_ecrire_fichier():
    nom_test = "test_temporaire.txt"
    contenu_attendu = "bonjour"

    # Écriture puis lecture
    ecrire_fichier(nom_test, contenu_attendu)
    contenu_recu = lire_fichier(nom_test)

    # Nettoyage du fichier
    if os.path.exists(nom_test):
        os.remove(nom_test)

    assert contenu_recu == contenu_attendu

    # ---------------------------
    # 18. Test lecture du message
    # ---------------------------
    def test_lecture_message_officiel():
        # On crée le fichier requis pour le test
        ecrire_fichier("message.txt", "Veni, vidi, vici!")

        contenu = lire_fichier("message.txt")
        assert "Veni" in contenu
        chiffre = chiffrer(contenu, 3)
        assert "yhqk" in chiffre  # 'Veni' -> 'veni' décalé de 3 devient 'yhqk'

        # ---------------------------
        # 19. Test de la fonctionnalité Performance (timeit)
        # ---------------------------
        def test_performance_timeit(capsys):
            """Vérifie que l'option --timeit s'exécute correctement et affiche le rapport."""
            from main import main

            # On simule le passage d'arguments en ligne de commande à la fonction main
            arguments_simulation = ["chiffrer", "test de performance", "-c", "5", "--timeit"]

            # Exécution du main avec les arguments simulés
            main(arguments_simulation)

            # On capture ce qui a été affiché dans la console
            console_output = capsys.readouterr().out

            # Vérifications : le rapport doit contenir ces mots-clés
            assert "Rapport de Performance" in console_output
            assert "Action mesurée" in console_output
            assert "Temps total" in console_output


# TODO : ajoutez vos propres tests ci-dessous
#  - test brute-force César
#  - test brute-force Enigma César
#  - autres cas limites

