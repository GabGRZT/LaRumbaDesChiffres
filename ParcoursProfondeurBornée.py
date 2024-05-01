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

def profondeurDabordBornee(depart, but, estEtatBut, filsEtat, nSeuil):
    en_attente = [depart]  # Liste des états non encore explorés
    vus = []  # Liste des états déjà explorés
    trouve = False

    while en_attente and not trouve:
        prochain = en_attente.pop()  # On récupère le prochain état à explorer (gestion de pile LIFO)
        vus.append(prochain)  # On ajoute l'état à la liste des états explorés
        print("Prochain : ", prochain)
        print("Vus : ", vus)

        if estEtatBut(prochain, but):
            solution = prochain
            return True
        else:
            for e in filsEtat(prochain):
                if(filsEtat(e) <= solution and e not in vus):
                    en_attente.insert(0, e)
                else:
                    nSueil = min(nSeuil, filsEtat(e))
    if nSeuil == 10:
        return True
    else:
        seuil = nSeuil
        return False

depart = [
    [1,4,7,0],
    [2,5,8,0],
    [3,6,9,0],
]

but = [
    [0,4,7,0],
    [2,5,8,0],
    [3,6,9,1],
]

nSeuil = 1
trouve = profondeurDabordBornee(depart, but, estEtatBut, filsEtat,nSeuil)
if trouve:
    print("La solution est trouvée.")
else:
    print("Aucune solution trouvée dans la profondeur maximale spécifiée.")

