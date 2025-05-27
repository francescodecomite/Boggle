# Construire un arbre à partir d'un lexique
# Lexique : un mot par ligne
from lexique import *

lexique=open('francaispurge.txt','r')

provi=lexique.readlines()
lesmots=[]
for u in provi:
    lesmots.append(u[:-1].upper())
    
arbre=Noeud('',"")
for parole in lesmots :
        arbre.ajouterMot(parole)
#print(arbre.suites['a'].suites.keys())




    
