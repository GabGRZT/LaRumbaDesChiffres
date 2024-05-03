import numpy as np
import copy
import fonctions


def profondeurDabordBornee(depart, but, seuil):
    en_attente = [(depart,0)]  # Liste des états non encore explorés
    vus = []  # Liste des états déjà explorés
    trouve = False

    while en_attente and not trouve:
        prochain = en_attente.pop()  # On récupère le prochain état à explorer (gestion de pile LIFO)
        vus.append(prochain[0].tolist())  # On ajoute l'état à la liste des états explorés
        if fonctions.estEtatBut(prochain[0], but):
            trouve = True
            return trouve, prochain  # Retourne vrai et l'état but s'il est trouvé
        else:
            listFils = fonctions.filsEtat(depart)
            for etat in listFils:
                if (not(etat.tolist() in vus) and (prochain[1]+1)<=seuil):  # Convertir etat en tuple
                    en_attente.append((etat,prochain[1]+1))  # Ajoute les nouveaux états à explorer
    return False, depart  # Retourne faux si l'état but n'est pas trouvé

depart = np.array([
                [0,4,7,0],
                [2,5,8,0],
                [3,6,9,1]
                ])

but = np.array([
                [0,4,7,0],
                [0,5,8,2],
                [3,6,9,1]
                ])

for seuil in range(20):
    print("nSeuil est à",seuil)
    trouve, etat_but = profondeurDabordBornee(depart, but,seuil)
    if trouve:
        print("La solution est trouvée.")
    else:
        print("Aucune solution trouvée dans la profondeur maximale spécifiée.")

