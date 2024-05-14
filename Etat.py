import copy


class Etat:
    def __init__(self, matrice):
        self.matrice = [["0","0","0","0"],
                        ["0","0","0","0"],
                        ["0","0","0","0"]
                        ]

    #def afficher(self):
    #    for row in self.matrice:
    #        print(" ".join(row))  # Join les éléments de chaque ligne avec un espace

    def est_etat_but(self, etat_but):
        return self.matrice == etat_but.matrice

    def est_sommet(self, ligne, colonne):
        if (ligne == 0 and self.matrice[ligne][colonne] != "|"):
            return True
        if (self.matrice[ligne - 1][colonne] == None and self.matrice[ligne][colonne] != "|"):
            return True
        return False

    def deplacement(self, pos_cube_init, pos_cube_final):
        etat_fils = copy.copy(self.matrice)
        etat_fils[pos_cube_final[0]][pos_cube_final[1]] = etat_fils[pos_cube_init[0]][pos_cube_init[1]]
        etat_fils[pos_cube_init[0]][pos_cube_init[1]] = "|"
        return etat_fils

    def place_libre(self, colonne_cube):
        liste = []
        for ligne in range(3):
            for colonne in range(4):
                if (colonne != colonne_cube):
                    if (ligne == 2 and self.matrice[ligne][colonne] == "|"):
                        liste.append((ligne, colonne))
                    else:
                        if (self.matrice[ligne][colonne] == "|" and self.matrice[ligne + 1][colonne] != None):
                            liste.append((ligne, colonne))
        return liste

    def fils_etat(self):
        liste_fils = []
        for ligne in range(3):
            for colonne in range(4):
                if self.est_sommet(ligne, colonne):
                    liste = self.place_libre(colonne)
                    for coordonnee in liste:
                        fils = self.deplacement((ligne, colonne), coordonnee)
                        liste_fils.append(fils)
        return liste_fils

    def nombre_mal_mis(self, etat_but):
        nb_mal_mis = 0
        for i in range(3):
            for j in range(4):
                if self.matrice[i][j] != etat_but.matrice[i][j]:
                    nb_mal_mis += 1
        return nb_mal_mis

    def f_etat(self, etat_but, cout_chemin_parcouru, cout_transition):
        f = cout_chemin_parcouru + cout_transition + self.nombre_mal_mis(etat_but)
        return f


# Création d'un état initial
#etat_initial = Etat([
#    ["1", "4", "7", "|"],
#    ["2", "5", "8", "|"],
#    ["3", "6", "9", "|"]
#])

# Création d'un état but
#etat_but = Etat([
#    ["1", "4", "7", "|"],
#    ["2", "5", "8", "|"],
#    ["3", "6", "9", "7"]
#])

# Affichage de l'état initial
#print("État initial :")
#etat_initial.afficher()

# Vérification si l'état initial est l'état but
#print("Est l'état but :", etat_initial.est_etat_but(etat_but))

# Vérification si (0, 1) est un sommet
#print("(0, 1) est un sommet :", etat_initial.est_sommet(0, 1))

# Recherche des fils de l'état initial
#print("Fils de l'état initial :")
#fils = etat_initial.fils_etat()

# Calcul du nombre de pièces mal placées
#print("Nombre de pièces mal placées dans l'état initial :", etat_initial.nombre_mal_mis(etat_but))

# Calcul de la fonction f pour l'état initial
#cout_chemin_parcouru = 5
#cout_transition = 3
#print("Fonction f pour l'état initial :", etat_initial.f_etat(etat_but, cout_chemin_parcouru, cout_transition))
