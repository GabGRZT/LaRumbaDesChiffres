import copy

class Etat:
    def __init__(self, etat):
        self.etat = etat

    def afficheCouleur(self,nom):
        print(nom, ":")
        for tige in self.etat:
            for cube in tige:
                if cube == 0:
                    print(" |", end="")  # Pour les emplacements vides
                elif cube in [1, 2, 3]:
                    print("\033[93m {}\033[00m".format(str(cube)), end="")
                elif cube in [4, 5, 6]:
                    print("\033[34m {}\033[00m".format(str(cube)), end="")
                elif cube in [7, 8, 9]:
                    print("\033[91m {}\033[00m".format(str(cube)), end="")
            print()  # Permet de faire un retour à la ligne

    def est_etat_but(self, etat_but):
        return self.etat == etat_but.etat

    def est_sommet(self, ligne, colonne):
        if (ligne == 0 and self.etat[ligne][colonne] != 0):
            return True
        if (self.etat[ligne - 1][colonne] == 0 and self.etat[ligne][colonne] != 0):
            return True
        return False

    def deplacement(self, pos_cube_init, pos_cube_final):
        etat_fils = copy.copy(self.etat)
        etat_fils[pos_cube_final[0]][pos_cube_final[1]] = etat_fils[pos_cube_init[0]][pos_cube_init[1]]
        etat_fils[pos_cube_init[0]][pos_cube_init[1]] = 0
        return etat_fils

    def place_libre(self):
        liste = []
        for ligne in range(3):
            for colonne in range(4):
                if(self.etat[ligne][colonne] == 0 and self.est_sommet(ligne, colonne)):
                    liste.append((ligne,colonne))
                if (ligne == 2 and self.etat[ligne][colonne] == 0):
                    liste.append((ligne, colonne))
                else:
                    if (self.etat[ligne][colonne] == 0 and self.etat[ligne + 1][colonne] != 0):
                        liste.append((ligne, colonne))
        return liste

    def fils_etat(self):
        liste_fils = []
        fils = Etat([[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        i = 0
        for ligne in range(3):
            for colonne in range(4):
                if self.est_sommet(ligne, colonne):
                    liste = self.place_libre()
                    #print("Places libres :", liste)
                    for coordonnee in liste:
                        #print("Coordonnée :",coordonnee)
                        self.etat = self.deplacement((ligne, colonne), coordonnee)
                        liste_fils.append(self)
                        #self.afficheCouleur("Fils "+str(i))
                        i += 1
                        self.etat = self.deplacement(coordonnee,(ligne, colonne))
        return liste_fils

    def heuristique(self, etat_but):
        nb_mal_mis = 0
        for i in range(3):
            for j in range(4):
                if self.etat[i][j] != etat_but.etat[i][j]:
                    nb_mal_mis += 1
        return nb_mal_mis

    def f_etat(self, etat_but, cout_chemin_parcouru, cout_transition):
        f = cout_chemin_parcouru + cout_transition + self.nombre_mal_mis(etat_but)
        return f


# Création d'un état initial
etat_initial = Etat([
    [1, 0, 7, 0],
    [2, 5, 8, 0],
    [3, 6, 9, 4]
])

# Création d'un état but
etat_but = Etat([
    [1, 4, 0, 0],
    [2, 5, 8, 0],
    [3, 6, 9, 7]
])

# Affichage de l'état initial
#etat_initial.afficheCouleur("État initial")

# Vérification si l'état initial est l'état but
#print("Est l'état but :", etat_initial.est_etat_but(etat_but))

# Vérification si (0, 1) est un sommet
#print("(0, 0) est un sommet :", etat_initial.est_sommet(0, 0))
#print("(0, 3) est un sommet :", etat_initial.est_sommet(0, 3))

#Verification des places libres



# Recherche des fils de l'état initial
#liste_fils = etat_initial.fils_etat()

# Calcul du nombre de pièces mal placées
#print("Nombre de pièces mal placées par rapport à l'état but :", etat_initial.heuristique(etat_but))

# Calcul de la fonction f pour l'état initial
#cout_chemin_parcouru = 5
#cout_transition = 1
#print("Fonction f pour l'état initial :", etat_initial.f_etat(etat_but, cout_chemin_parcouru, cout_transition))
