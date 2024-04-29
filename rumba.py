import numpy as np
import copy

def etatinitial1():
    etatinitial = np.array([[1,4,7,0],[2,5,8,0],[3,6,9,0]])
    return etatinitial

def etatinitial2():
    etatinitial2 = np.array([[3,6,9,0],[2,5,8,0],[1,4,7,0]])
    return etatinitial2

def estEtatBut(etatActuel, etatBut):
    return (etatActuel == etatBut).all()


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
                print(list)
                for coordonne in list:
                    listFils.append(deplacement([ligne,colonne],coordonne, etat))
    return listFils

def pop(list):
    resultat=list[len(list)-1]
    list.remove(resultat)
    return resultat


listFilsEtat=filsEtat(etatinitial1())
for elem in listFilsEtat:
    print("Fils : \n",elem)

#etatinitial3=copy.copy(etatinitial1() == etatinitial2())
#for ligne in range(3):
 #   for colonne in range(4):
  #      print(etatinitial3[ligne][colonne])
print(estEtatBut(etatinitial1(),etatinitial2()))
#print(etatinitial1())
#print(place_libre(0, etatinitial1()))
#print(deplacement([0,0], [2,3], etatinitial1()))
#print(estSommet(etatinitial1(), 0,2))

list=[1,2,3]
print(pop(list))

print(list)
print(pop(list))
print(list)