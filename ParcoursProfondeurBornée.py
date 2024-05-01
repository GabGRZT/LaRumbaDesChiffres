import numpy as np
import copy
import fonctions


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

