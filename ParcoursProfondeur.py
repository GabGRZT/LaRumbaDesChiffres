import numpy as np
import copy
import fonctions
from Etat import Etat
from affichage_console import afficheCouleur

def profondeurDabord(depart, but):
    en_attente = [depart]  # Liste des états non encore explorés
    vus = set()  # Liste des états déjà explorés
    trouve = False
    iterations = 1

    while iterations != 4:
        prochain = en_attente.pop(0)  # On récupère le prochain état à explorer (gestion de pile LIFO)
        vus.add(tuple(map(tuple,prochain)))  # On ajoute l'état à la liste des états explorés
# <<<<<<< Updated upstream
#         if Etat.est_etat_but(prochain, but):
# =======
        if fonctions.estEtatBut(prochain, but):
            trouve = True
            return trouve, prochain  # Retourne vrai et l'état but s'il est trouvé
        else:
            listFils = Etat.fils_etat(prochain)
            for etat in listFils:
# <<<<<<< Updated upstream
#                 if etat not in vus:  # Convertir etat en tuple
#                     #print("etat\n",etat)
#                     #print("vus\n",vus)
#                     en_attente.insert(0,etat)  # Ajoute les nouveaux états à explorer
#         iterations += 1
#         print("Iteration :", iterations )
#         afficheCouleur(etat)
# =======
                if (tuple(map(tuple,etat)) in vus):
                    en_attente.insert(0,etat)  # Ajoute les nouveaux états à explorer
    return False, depart  # Retourne faux si l'état but n'est pas trouvé


# Création d'un état initial
departEtat = Etat([
    ["1", "4", "7", "|"],
    ["2", "5", "8", "|"],
    ["3", "6", "9", "|"]
])

# Création d'un état but
butEtat = Etat([
    ["|", "4", "7", "3"],
    ["|", "5", "8", "2"],
    ["|", "6", "9", "1"]
])

depart = np.array([
                [4,1,7,0],
                [2,5,8,0],
                [3,6,9,0]
                ])

but = np.array([
                [0,0,7,0],
                [2,5,8,1],
                [3,6,9,4]
                ])
trouve, etat_but = profondeurDabord(depart, but)
if trouve:
    print("La solution est trouvée : \n", etat_but)
else:
    print("Aucune solution trouvée: \n",etat_but)