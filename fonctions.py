import numpy as np
import copy

def etatinitial1():
    etatinitial = np.array([
                            [1,4,7,"|"],
                            [2,5,8,"|"],
                            [3,6,9,"|"]
                            ])
    return etatinitial

def etatinitial2():
    etatinitial2 = np.array([[3,6,9,"|"],
                             [2,5,8,"|"],
                             [1,4,7,"|"]
                             ])
    return etatinitial2

def estEtatBut(etatActuel, etatBut):
    return np.all(etatActuel == etatBut)

def estSommet(etat, ligne, colonne):
    if(ligne == 0 and etat[ligne][colonne]!=0):
        return True
    if (etat[ligne-1][colonne]==0 and etat[ligne][colonne]!=0):
        return True
    return False

def deplacement(pos_cube_init, pos_cube_final, etat):
    etatFils=copy.copy(etat)
    etatFils[pos_cube_final[0]][pos_cube_final[1]] = etatFils[pos_cube_init[0]][pos_cube_init[1]]
    etatFils[pos_cube_init[0]][pos_cube_init[1]] = 0
    return etatFils

def place_libre(colonne_cube, etat):
    list = []
    for ligne in range(3):
        for colonne in range(4):
            if(colonne != colonne_cube):
                # Tant qu'on est pas au point le plus bas du pique (=0)
                # et qu'on est pas à la fin de la matrice
                if (ligne==2 and etat[ligne][colonne] == 0):
                    list.append(([ligne,colonne]))
                else:
                    if (etat[ligne][colonne] == 0 and (etat[ligne+1][colonne] != 0)):
                        list.append([ligne, colonne])
    # Renvoie une liste de positions finales possibles
    return list

def filsEtat(etat):
    #etatFils = etat
    listFils = []
    # Boucle qui donne l'indice de la colonne
    for ligne in range(3):
        for colonne in range(4):
            if (estSommet(etat, ligne ,colonne)):
                #Boucle qui donne l'indice des sommets != n
                list = place_libre(colonne, etat)
                for coordonne in list:
                    moove = deplacement([ligne,colonne],coordonne, etat)
                    listFils.append(moove)
    return listFils

def nombreMalMis(etat,etatBut):
    nbMalMis=0;
    comparasionEtatBut=etat == etatBut
    for ligne in comparasionEtatBut:
        for booleen in ligne:
            if not booleen:
                nbMalMis+=1
    return nbMalMis
def fEtat(etat,etatBut,coutCheminParcouru,coutTransition):
    return (coutCheminParcouru+coutTransition)+(nombreMalMis(etat,etatBut))

#listFilsEtat=filsEtat(etatinitial1())
#for elem in listFilsEtat:
#    print("Fils : \n",elem)

#print(filsEtat( [0,4,7,0],
#                [2,5,8,0],
#               [3,6,9,1]))


#print(estEtatBut(etatinitial1(),etatinitial1()))
#print(etatinitial1())
#print(place_libre(0, etatinitial1()))
#print(deplacement([0,0], [2,3], etatinitial1()))
#print(estSommet(etatinitial1(), 0,2))