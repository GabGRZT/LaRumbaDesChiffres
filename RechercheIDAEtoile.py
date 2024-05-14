import numpy as np
import fonctions
from affichage_console import afficheCouleur

def dejaVu(etat,liste):
    for elem in liste:
        if (etat==elem).all():
            return True
    return False
def profondeurBornee(depart, but, s):
    en_attente = [(depart,0,fonctions.fEtat(depart,but,0,1))]  # Liste des états non encore explorés, avec leur profondeur et g(e)
    vus = set()  # Liste des états déjà explorés
    nSeuil=1000
    global seuil
    global solution
    nbEtatCree=0
    nbEtatDeveloppes=0

    while en_attente:
        prochain = en_attente.pop()  # On récupère le prochain état à explorer (gestion de pile LIFO)
        vus.add(tuple(map(tuple,prochain[0])))  # On ajoute l'état à la liste des états explorés
        nbEtatDeveloppes+=1
        if fonctions.estEtatBut(prochain[0], but):
            solution=prochain[0]
            return True,nbEtatCree,nbEtatDeveloppes  # Retourne vrai+nbEtatCree+nbEtatDeveloppes
        else:
            listFils = fonctions.filsEtat(prochain[0])
            nbEtatCree+=listFils.__len__()
            for etat in listFils:
                heuristique=(fonctions.fEtat(etat,but,prochain[2],1))
                if (not(tuple(map(tuple,etat)) in vus)) and (heuristique<=s):
                    en_attente.append((etat, prochain[1] + 1, heuristique))  # Ajoute les nouveaux états à explorer
                else:
                    nSeuil=min(nSeuil,heuristique)
    if nSeuil==1000:
        return True,nbEtatCree,nbEtatDeveloppes
    else:
        seuil=nSeuil
        return False,nbEtatCree,nbEtatDeveloppes

def ida(depart, but):
    global solution
    global seuil
    nbIteration=0
    tableauNombredeNoeud=[]
    tableauNombreEtatDeveloppe=[]
    solution=None
    seuil=fonctions.fEtat(depart,but,0,1)
    resultat=False,None,None
    while not resultat[0]:
        resultat=profondeurBornee(depart, but, seuil)
        tableauNombredeNoeud.append(resultat[1])
        tableauNombreEtatDeveloppe.append(resultat[2])
        nbIteration+=1
        if nbIteration%1000==0:
            print(nbIteration)
    return solution,nbIteration,tableauNombredeNoeud,tableauNombreEtatDeveloppe

#1,2,3: 1J,2J,3J
#4,5,6: 1B,2B,3B
#7,8,9: 1R,2R,3R

situationInitiale1 = np.array([
                [0,0,4,7],
                [2,0,5,8],
                [3,1,6,9]
                ])

but1 = np.array([
                [1,0,4,7],
                [2,0,5,8],
                [3,0,6,9]
                ])

but2 = np.array([
                [1,9,4,0],
                [2,8,5,0],
                [3,7,6,0]
                ])

situationInitiale2 = np.array([
                [1,4,7,0],
                [2,5,8,0],
                [3,6,9,0]
                ])

but3 = np.array([
                [7,8,1,0],
                [2,4,5,0],
                [3,6,9,0]
                ])

but4 = np.array([
                [2,5,8,0],
                [1,4,7,0],
                [3,6,9,0]
                ])

but5 = np.array([
                [8,0,5,0],
                [2,4,7,0],
                [3,6,9,1]
                ])

but6 = np.array([
                [1,2,3,0],
                [7,8,9,0],
                [4,5,6,0]
                ])

seuil=0
solution=None

# probleme1=ida(situationInitiale1,but1)
# # afficheCouleur("situation initiale 1",situationInitiale1)
# # afficheCouleur("Solution problème 1",probleme1[0])
# print("Nombre d'iteration : ",probleme1[1],"\n")
#
# probleme2=ida(situationInitiale1,but2)
# # afficheCouleur("situation initiale 1",situationInitiale2)
# # afficheCouleur("Solution problème 2",probleme2[0])
# print("Nombre d'iteration : ",probleme2[1],"\n" )
#
# probleme3=ida(situationInitiale2,but3)
# # afficheCouleur("situation initiale 2",situationInitiale2)
# # afficheCouleur("Solution problème 3",probleme3[0])
# print("\nNombre d'iteration : ",probleme3[1],"\n")
#
# #probleme4=ida(situationInitiale2,but4)
# #print("Solution problème 4\n",probleme4[0],"\nNombre d'iteration",probleme4[1])
#
# probleme5=ida(situationInitiale2,but5)
# afficheCouleur("situation initiale 2",situationInitiale2)
# afficheCouleur("Solution problème 5",probleme5[0])
# print("\nNombre d'iteration : ",probleme5[1],"\n")
#
# #probleme6=ida(situationInitiale2,but6)
# #print("Solution problème 6\n",afficheCouleur(probleme6[0]),"\nNombre d'iteration : ",probleme6[1])

probleme1=ida(situationInitiale1,but1)
print("Solution problème 1\n",probleme1[0],"\nNombre d'iteration",probleme1[1],"\nNombre Etat créer",probleme1[2],"\nNombre Etat developpés",probleme1[3])

probleme2=ida(situationInitiale1,but2)
print("Solution problème 2\n",probleme2[0],"\nNombre d'iteration",probleme2[1],"\nNombre Etat créer",probleme2[2],"\nNombre Etat developpés",probleme2[3])

probleme3=ida(situationInitiale2,but3)
print("Solution problème 3\n",probleme3[0],"\nNombre d'iteration",probleme3[1],"\nNombre Etat créer",probleme3[2],"\nNombre Etat developpés",probleme3[3])

probleme4=ida(situationInitiale2,but4)
print("Solution problème 4\n",probleme4[0],"\nNombre d'iteration",probleme4[1],"\nNombre Etat créer",probleme4[2],"\nNombre Etat developpés",probleme4[3])

probleme5=ida(situationInitiale2,but5)
print("Solution problème 5\n",probleme5[0],"\nNombre d'iteration",probleme5[1],"\nNombre Etat créer",probleme5[2],"\nNombre Etat developpés",probleme5[3])

probleme6=ida(situationInitiale2,but6)
print("Solution problème 6\n",probleme6[0],"\nNombre d'iteration",probleme6[1],"\nNombre Etat créer",probleme6[2],"\nNombre Etat developpés",probleme6[3])

# bon=[]
# bon.append(but1)
# bon.append(but2)
#
# print(dejaVu(but2,bon))

