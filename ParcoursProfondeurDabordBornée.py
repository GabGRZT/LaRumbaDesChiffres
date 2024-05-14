import numpy as np
import fonctions

def dejaVu(etat,listeVu):
    for elem in listeVu:
        if (elem==etat).all():
            return True
def profondeurDabordBornee(depart, but, seuil):
    en_attente = [(depart,0)]  # Liste des états non encore explorés
    vus = set() # Liste des états déjà explorés
    trouve = False

    while en_attente and not trouve:
        prochain = en_attente.pop()  # On récupère le prochain état à explorer (gestion de pile LIFO)
        vus.add(tuple(map(tuple,prochain[0])))
        if fonctions.estEtatBut(prochain[0], but):
            trouve = True
            return trouve, prochain[0]  # Retourne vrai et l'état but s'il est trouvé
        else:
            listFils = fonctions.filsEtat(prochain[0])
            for etat in listFils:
                if not(tuple(map(tuple,etat)) in vus) and (prochain[1]+1)<=seuil:
                    en_attente.append((etat, prochain[1] + 1))  # Ajoute les nouveaux états à explorer
    return False, depart  # Retourne faux si l'état but n'est pas trouvé


depart = np.array([
                [1,4,7,0],
                [2,5,8,0],
                [3,6,9,0]
                ])

but1 = np.array([
                [0,0,7,0],
                [2,5,8,1],
                [3,6,9,4]
                ])

but2 = np.array([
                [0,4,7,0],
                [2,5,1,0],
                [3,6,9,8]
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

for seuil in range(11):
    print("seuil est à",seuil)
    trouve, etat_but = profondeurDabordBornee(depart,but1,seuil)
    if trouve:
        print("La solution est trouvée.")
    else:
        print("Aucune solution trouvée dans la profondeur maximale spécifiée.")
# list=[]
# list.append(depart)
# list.append(but1)
# for elem in list:
#     if (elem==but1).all():
#         print("Ben il l'a trouvé")
#print(list.count(depart))
#print(list.index(depart))
#try:
#    i=(list.count(but1))
#    print("Il est dans la liste",i)
#except ValueError:
#    print("Il n'est pas dans la liste!")

