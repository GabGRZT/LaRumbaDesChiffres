import numpy as np
import fonctions
from Etat import *

def profondeurDabord(depart, but):
#     enAttente = [depart]  # Initialisation de la liste d'attente avec l'état de départ
#     vus = set()  # Initialisation de l'ensemble des états visités
#     trouve = False  # Initialisation du booléen trouvé à faux
#     prochain = Etat([[0,0,0,0],[0,0,0,0],[0,0,0,0]])
#
#     while enAttente and not trouve:
#         prochain = enAttente.pop()  # Récupère et retire le prochain état à explorer de la liste enAttente
#
#         if prochain in vus:  # Si l'état prochain a déjà été visité
#             continue  # Passe à l'itération suivante
#
#         vus.add(prochain)  # Ajoute l'état prochain à l'ensemble des états visités
#
#         if prochain.est_etat_but(but):  # Vérifie si l'état prochain est l'état but recherché
#             trouve = True  # Marque que l'état but a été trouvé
#             return True, prochain  # Retourne vrai et l'état prochain
#
#         # Ajoute les fils de l'état prochain qui n'ont pas encore été visités à la liste d'attente
#         enAttente.extend(e for e in prchain.fils_etat() if e not in vus)
#
#     if not trouve:  # Si aucun chemin n'est trouvé
#         return False, depart  # Retourne faux et l'état de départ
# =======
    en_attente = [depart]  # Liste des états non encore explorés
    vus = set()  # Liste des états déjà explorés
    trouve = False

    while en_attente and not trouve:
        prochain = en_attente.pop()  # On récupère le prochain état à explorer (gestion de pile LIFO)
        vus.add(tuple(map(tuple,prochain)))  # On ajoute l'état à la liste des états explorés
#       if Etat.est_etat_but(prochain, but):
        if fonctions.estEtatBut(prochain, but):
            trouve = True
            return trouve, prochain  # Retourne vrai et l'état but s'il est trouvé
        else:
            listFils = fonctions.filsEtat(prochain)
            for etat in listFils:
                if not(tuple(map(tuple,etat))) in vus:  # Convertir etat en tuple
                    en_attente.append(etat)  # Ajoute les nouveaux états à explorer
    return trouve
#         iterations += 1
#         print("Iteration :", iterations )
#         afficheCouleur(etat)



# # Création d'un etat initial
# depart = Etat([[4,1,7,0],
#                [2,5,8,0],
#                [3,6,9,0]
#                 ])
#
# # Création d'un etat final
# but = Etat([[0,0,7,0],
#             [2,5,8,1],
#             [3,6,9,4]
#             ])

depart = np.array([
                [1,4,7,0],
                [2,5,8,0],
                [3,6,9,0]
                ])

but1 = np.array([
                [1,0,7,0],
                [2,5,8,0],
                [3,6,9,4]
                ])

trouve, etat_but = profondeurDabord(depart, but1)
if trouve:
    print("La solution est trouvée : \n", etat_but)
else:
    print("Aucune solution trouvée: \n")