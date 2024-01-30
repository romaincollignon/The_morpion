def afficher_grille(grille):
    # Affiche la grille de jeu actuelle
    for ligne in grille:
        print(" | ".join(ligne))
        # Question 2: print(???)

def verif_gagnant(grille, joueur):
    # Vérifie si le joueur a gagné
    for i in range(3):
        # Vérification des lignes et colonnes
        if grille[i][0] == grille[i][1] == grille[i][2] == joueur or grille[0][i] == grille[1][i] == grille[2][i] == joueur:
            return True
    # Vérification des diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] == joueur or grille[0][2] == grille[1][1] == grille[2][0] == joueur:
        return True
    return False

def jeu_morpion():
    # Initialise une grille de jeu vide
    grille = [[" " for _ in range(3)] for _ in range(3)]
    # Question 3: joueur_actuel = ???

    for _ in range(9):
        afficher_grille(grille)
        print(f"C'est au tour du joueur {joueur_actuel}.")

        ligne = int(input("Entrez le numéro de ligne (0-2): "))
        colonne = int(input("Entrez le numéro de colonne (0-2): "))

        if grille[ligne][colonne] == " ":
            grille[ligne][colonne] = joueur_actuel
        else:
            # Question 4
            continue

        if verif_gagnant(grille, joueur_actuel):
            afficher_grille(grille)
            # Question 5: print(f"??{joueur_actuel} ???")
            return

        joueur_actuel = "O" if joueur_actuel == "X" else "X"

    afficher_grille(grille)
    # QUESTION 1: print("????")

jeu_morpion()
