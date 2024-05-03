import numpy as np
import copy
import fonctions
import ParcoursProfondeurBornée

def ida(depart, but, seuil):
    solution=None;
    seuil=fonctions.fEtat(depart)
    termine=false;
    while not termine:
        termine=ParcoursProfondeurBornée.profondeurDabordBornee(depart, but, seuil)
    if solution!=None:
        return solution
    else:
        return echec

