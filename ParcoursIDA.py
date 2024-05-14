import numpy as np
import fonctions


def profondeurBornee(depart, but, s):
    en_attente = [(depart,0,0)]  # Liste des états non encore explorés, avec leur profondeur et g(e)
    vus = set()  # Liste des états déjà explorés
    nSeuil=1000
    global seuil
    global solution

    while en_attente:
        prochain = en_attente.pop(0)  # On récupère le prochain état à explorer (gestion de pile LIFO)
        vus.add(tuple(map(tuple,prochain[0])))  # On ajoute l'état à la liste des états explorés
        if fonctions.estEtatBut(prochain[0], but):
            solution=prochain[0]
            return True  # Retourne vrai
        else:
            listFils = fonctions.filsEtat(prochain[0])
            for etat in listFils:
                heuristique=(fonctions.fEtat(etat,but,prochain[2],1))
                if not (tuple(map(tuple,etat))in vus) and ((heuristique)<=s):
                    en_attente.insert(0,(etat, prochain[1] + 1,heuristique))  # Ajoute les nouveaux états à explorer
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
    solution=None
    seuil=fonctions.fEtat(depart,but,0,1)
    termine=False
    i=0
    while not termine:
        termine=profondeurBornee(depart, but, seuil)
        i+=1
        if i % 1000 == 0:
            print(i)
    return solution

depart = np.array([
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
print(ida(depart,but3))
