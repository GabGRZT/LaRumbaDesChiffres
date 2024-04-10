import numpy as np

def etatinitial1():
    etatinitial = np.array([[1,4,7,0],[2,5,8,0],[3,6,9,0]])
    return etatinitial

#def etatinitial2():
    #matrice = np.array([[1,4,7,0],[2,5,8,0],[3,6,9,0]])
    #print(matrice)

def estSommet(etat, index):
    return etat[0][index] != 0
        

def filsEtat(etat):
    etatsFils = etat
    list = []
    #Boucle qui donne l'indice de la colonne
    for colonneInitiale in range(4):
        if (estSommet(etat, colonneInitiale)):
            #Boucle qui donne l'indice des sommets != n
            for colonneAutre in range(4):
                if(colonneAutre != colonneInitiale and (not(estSommet(etat, colonneAutre)))):
                    ligneRecherchée = 0 
                    #Tant qu'on est pas au point le plus bas du pique (=0) 
                    #et qu'on est pas à la fin de la matrice
                    while (etat[ligneRecherchée][colonneAutre]==0 and ligneRecherchée != 2):
                        ligneRecherchée+=1
                    etatsFils[ligneRecherchée][colonneAutre] = etat[0][colonneInitiale]
    print("-----------")
    print(etatsFils)

filsEtat(etatinitial1())

