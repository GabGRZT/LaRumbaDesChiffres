def afficheCouleur(nom,etat):
    print(nom,":")
    for tige in etat:
        for cube in tige:
            if cube == 0:
                print(" |" ,end="")  # Pour les emplacements vides
            elif cube in [1, 2, 3]:
                print("\033[93m {}\033[00m".format(str(cube)), end="")
            elif cube in [4, 5, 6]:
                print("\033[34m {}\033[00m".format(str(cube)), end="")
            elif cube in [7, 8, 9]:
                print("\033[91m {}\033[00m".format(str(cube)), end="")
        print()  # Permet de faire un retour à la ligne

# Exemple d'utilisation :
etat_initial1 = [["|", "|", "4", "7"],
                 ["2", "|", "5", "8"],
                 ["3", "1", "6", "9"]]

etat_but1 = [["1", "|", "4", "7"],
             ["2", "|", "5", "8"],
             ["3", "|", "6", "9"]]

etat_but2 = [["1", "9", "4", "|"],
             ["2", "8", "5", "|"],
             ["3", "7", "6", "|"]]

etat_initial2 = [["1", "4", "7", "|"],
                 ["2", "5", "8", "|"],
                 ["3", "6", "9", "|"]]

etat_but3 = [["7", "8", "1", "|"],
             ["2", "4", "5", "|"],
             ["3", "6", "9", "|"]]

etat_but4 = [["2", "5", "8", "|"],
             ["1", "4", "7", "|"],
             ["3", "6", "9", "|"]]

etat_but5 = [["8", "|", "5", "|"],
             ["2", "4", "7", "|"],
             ["3", "6", "9", "1"]]

etat_but6 = [["1", "2", "3", "|"],
             ["4", "5", "6", "|"],
             ["7", "8", "9", "|"]]

#afficheCouleur(etat_initial1, "Etat initial 1")
#print("\n")
#afficheCouleur(etat_but1,"Etat but 1")
#print("\n")
#afficheCouleur(etat_but2,"Etat but 2")
#print("\n")
#afficheCouleur(etat_initial2, "Etat initial 2")
#print("\n")
#afficheCouleur(etat_but3,"Etat but 3")
#print("\n")
#afficheCouleur(etat_but4,"Etat but 4")
#print("\n")
#afficheCouleur(etat_but5,"Etat but 5")
#print("\n")
#afficheCouleur(etat_but6,"Etat but 6")