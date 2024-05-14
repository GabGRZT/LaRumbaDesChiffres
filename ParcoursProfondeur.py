import numpy as np
import copy
from Etat import *

def profondeurDabord(depart, but):
    enAttente = [depart]  # Initialisation de la liste d'attente avec l'état de départ
    vus = set()  # Initialisation de l'ensemble des états visités
    trouve = False  # Initialisation du booléen trouvé à faux
    prochain = Etat([[0,0,0,0],[0,0,0,0],[0,0,0,0]])

    while enAttente and not trouve:
        prochain = enAttente.pop()  # Récupère et retire le prochain état à explorer de la liste enAttente

        if prochain in vus:  # Si l'état prochain a déjà été visité
            continue  # Passe à l'itération suivante

        vus.add(prochain)  # Ajoute l'état prochain à l'ensemble des états visités

        if prochain.est_etat_but(but):  # Vérifie si l'état prochain est l'état but recherché
            trouve = True  # Marque que l'état but a été trouvé
            return True, prochain  # Retourne vrai et l'état prochain

        # Ajoute les fils de l'état prochain qui n'ont pas encore été visités à la liste d'attente
        enAttente.extend(e for e in prchain.fils_etat() if e not in vus)

    if not trouve:  # Si aucun chemin n'est trouvé
        return False, depart  # Retourne faux et l'état de départ



# Création d'un etat initial
depart = Etat([[4,1,7,0],
               [2,5,8,0],
               [3,6,9,0]
                ])

# Création d'un etat final
but = Etat([[0,0,7,0],
            [2,5,8,1],
            [3,6,9,4]
            ])

trouve, etat_but = profondeurDabord(depart, but)
if trouve:
    print("La solution est trouvée : \n", etat_but)
else:
    print("Aucune solution trouvée: \n")