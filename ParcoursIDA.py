import numpy as np
import fonctions


def profondeurBornee(depart, but, s):
    en_attente = [(depart,0,0)]  # Liste des états non encore explorés, avec leur profondeur et g(e)
    vus = []  # Liste des états déjà explorés
    nSeuil=1000
    global seuil
    global solution

    while en_attente:
        prochain = en_attente.pop()  # On récupère le prochain état à explorer (gestion de pile LIFO)
        vus.append(prochain[0])  # On ajoute l'état à la liste des états explorés
        if fonctions.estEtatBut(prochain[0], but):
            solution=prochain[0]
            return True  # Retourne vrai
        else:
            listFils = fonctions.filsEtat(prochain[0])
            for etat in listFils:
                heuristique=(fonctions.fEtat(etat,but,prochain[2],1))
                try:
                    vus.index(etat)
                    break;
                except ValueError:
                    if (heuristique)<=s:
                        en_attente.append((etat, prochain[1] + 1,heuristique))  # Ajoute les nouveaux états à explorer
                    else:
                        nSeuil=min(nSeuil,heuristique)
    if nSeuil==1000:
        return True
    else:
        seuil=nSeuil
        return False

def ida(depart, but):
    global solution
    global seuil
    solution=None;
    seuil=fonctions.fEtat(depart,but,0,1)
    termine=False;
    while not termine:
        termine=profondeurBornee(depart, but, seuil)
    return solution

#depart = np.array([
#                [1,4,7,0],
#                [2,5,8,0],
#                [3,6,9,0]
#                ])

#but = np.array([
#                [4,1,7,0],
#                [2,5,8,0],
#                [3,6,9,0]
#                ])

#seuil=0
#solution=None
#print(ida(depart,but))
