import numpy as np
import copy
import fonctions

def dejaVu(etat,listeVu):
    for elem in listeVu:
        if (elem==etat).all():
            return True
def profondeurDabordBornee(depart, but, seuil):
    en_attente = [(depart,0)]  # Liste des états non encore explorés
    vus = [] # Liste des états déjà explorés
    trouve = False

    while en_attente and not trouve:
        prochain = en_attente.pop()  # On récupère le prochain état à explorer (gestion de pile LIFO)
        vus.append(prochain[0])
        #print("prochain[0]",prochain[0])
        #vus=np.array([vus,prochain[0]])
        #vus.put(0,prochain[0]) # On ajoute l'état à la liste des états explorés
        if fonctions.estEtatBut(prochain[0], but):
            trouve = True
            print("La taille de la liste en attente est",vus.__len__())
            return trouve, prochain[0]  # Retourne vrai et l'état but s'il est trouvé
        else:
            listFils = fonctions.filsEtat(prochain[0])
            for etat in listFils:
                # etatdejaVu = dejaVu(etat, vus)
                # if not(etatdejaVu) and ((prochain[1]+1)<=seuil):
                #     en_attente.append((etat, prochain[1]+1))  # Ajoute les nouveaux états à explorer
                # #print(vus)
                try:
                    #print("mec tu rentre un jour ici?")
                    i=vus.index(etat)
                    #print(i)
                    #print("\nL'état est dans la liste\n")
                    break;
                except ValueError:
                    #print("Etat n'est pas dans la liste")
                    if (prochain[1]+1)<=seuil:
                        en_attente.append((etat, prochain[1] + 1))  # Ajoute les nouveaux états à explorer
                else:
                    print("Vend moi du rêve")
    print("La taille de la liste en attente est", vus.__len__())
    return False, depart  # Retourne faux si l'état but n'est pas trouvé

#depart = np.array([
#                [4,1,7,0],
#                [2,5,8,0],
#                [3,6,9,0]
#                ])

#but1 = np.array([
#                [0,0,7,0],
#                [2,5,8,1],
#                [3,6,9,4]
#                ])
#but2 = np.array([
#                [1,4,7,0],
#                [2,5,8,0],
#                [3,6,9,0]
#                ])

#for seuil in range(10):
#     print("seuil est à",seuil)
#     trouve, etat_but = profondeurDabordBornee(depart,but2,seuil)
#     if trouve:
#         print("La solution est trouvée.")
#     else:
#         print("Aucune solution trouvée dans la profondeur maximale spécifiée.")
#list=[]
#list.append(depart)
#list.append(but1)
#for elem in list:
#     if (elem==but1).all():
#         print("Ben il l'a trouvé")
#print(list.count(depart))
#print(list.index(depart))
#try:
#    i=(list.count(but1))
#    print("Il est dans la liste",i)
#except ValueError:
#    print("Il n'est pas dans la liste!")

