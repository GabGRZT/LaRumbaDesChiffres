import numpy as np
import copy
import fonctions

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
    #print("Etat :",etat)
    #print("Etat fils:",etatFils)
    return etatFils

def place_libre(colonne_cube, etat):
    list = []
    for ligne in range(3):
        for colonne in range(4):
            if(colonne != colonne_cube):
                # Tant qu'on est pas au point le plus bas du pique (=0)
                # et qu'on est pas à la fin de la matrice
                if ligne==2 and etat[ligne][colonne] == 0:
                    list.append(([ligne,colonne]))
                else:
                    if etat[ligne][colonne] == 0 and (etat[ligne+1][colonne] != 0 ):
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
                #print(list)
                for coordonne in list:
                    listFils.append(deplacement([ligne,colonne],coordonne, etat))
    return listFils

def profondeurDabord(depart, but, estEtatBut, filsEtat):
    en_attente = [depart]  # Liste des états non encore explorés
    vus = []  # Ensemble des états déjà explorés
    trouve = False

    while en_attente and not trouve:
        prochain = en_attente.pop()  # On récupère le prochain état à explorer (gestion de pile LIFO)
        vus.append(prochain)  # On ajoute l'état à la liste des états explorés
        print("Prochain : ",prochain)
        print("Vus : ",vus,"\n")

        if estEtatBut(prochain, but):
            trouve = True
            return trouve, prochain  # Retourne vrai et l'état but s'il est trouvé
        else:
            for etat in filsEtat(prochain):
                print(etat,"\n")
                if etat in vus:
                    pass
                else:
                    en_attente.append(etat)  # Ajoute les nouveaux états à explorer

    return False, depart  # Retourne faux si l'état but n'est pas trouvé


depart = [
    [1,4,7,0],
    [2,5,8,0],
    [3,6,9,0],
]

but = [
    [0,0,0,7],
    [2,5,8,4],
    [3,6,9,1],
]
trouve, etat_but = profondeurDabord(depart, but, estEtatBut, filsEtat)
if trouve:
    print("La solution est trouvée :", etat_but)
else:
    print("Aucune solution trouvée.")

