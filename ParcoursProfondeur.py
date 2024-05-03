import numpy as np
import copy
import fonctions

def profondeurDabord(depart, but):
    en_attente = [depart]  # Liste des états non encore explorés
    vus = []  # Liste des états déjà explorés
    trouve = False

    while en_attente and not trouve:
        prochain = en_attente.pop()  # On récupère le prochain état à explorer (gestion de pile LIFO)
        vus.append(prochain.tolist())  # On ajoute l'état à la liste des états explorés

        if fonctions.estEtatBut(prochain, but):
            trouve = True
            return trouve, prochain  # Retourne vrai et l'état but s'il est trouvé
        else:
            listFils = fonctions.filsEtat(depart)
            for etat in listFils:
                if not(etat.tolist() in vus):  # Convertir etat en tuple
                    en_attente.append(etat)  # Ajoute les nouveaux états à explorer

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

trouve, etat_but = profondeurDabord(depart, but)
if trouve:
    print("La solution est trouvée : \n", etat_but)
else:
    print("Aucune solution trouvée.")

