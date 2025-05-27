# Un programme pour les unir tous


from construireArbre import *
from generation import *
from sys import *

tousLesMots=set()
solutions=set()

t=[0]
k=[0]

# Construire tous les chemins partant d'une case
def construireChemins(plateau,i,j,chaine,casesVisitees):
    """
    plateau : le tableau 4x4 qui représente la partie
    i,j : coordonnées de la case de départ
    chaine :  la chaine deja lue le long de ce chemin
    casesVisitees : tableau 4x4 repérant les case devenues inacessibles
    """
   
    
    if estPresent(chaine,arbre) and len(chaine)>2:
        solutions.add(chaine)
    # Calculer les coordonnées de toutes les cases accessibles autour de i,j
    candidats=[]
   
    # Ligne 0
    if i==0 :
        candidats.append((i+1,j))
        if j==0:
            candidats.append((i,j+1))
            candidats.append((i+1,j+1))
        elif j==3:
            candidats.append((i,j-1))
            candidats.append((i+1,j-1))
        else :
            candidats.append((i,j+1))
            candidats.append((i+1,j+1))
            candidats.append((i,j-1))
            candidats.append((i+1,j-1))
    # Ligne 3
    if i==3:
        candidats.append((i-1,j))
        if j==0 :
            candidats.append((i-1,j+1))
            candidats.append((i,j+1))
        elif j==3:
            candidats.append((i-1,j-1))
            candidats.append((i,j-1))
        else :
            candidats.append((i-1,j-1))
            candidats.append((i-1,j+1))
            candidats.append((i,j-1))
            candidats.append((i,j+1))

    if i in [1,2]:
        if j==0 :
         candidats.append((i-1,j+1))
         candidats.append((i-1,j))
         candidats.append((i,j+1))
         candidats.append((i+1,j))
         candidats.append((i+1,j+1))

        elif j==3 :
         candidats.append((i-1,j-1))
         candidats.append((i-1,j))
         candidats.append((i,j-1))
         candidats.append((i+1,j-1))
         candidats.append((i+1,j))
       
        else :     
         candidats.append((i-1,j-1))
         candidats.append((i-1,j+1))
         candidats.append((i-1,j))
         candidats.append((i,j-1))
         candidats.append((i,j+1))
         candidats.append((i+1,j-1))
         candidats.append((i+1,j))
         candidats.append((i+1,j+1))
    # On a tous les candidats voisins de la case i,j
    # on supprime les cases déja visités
    newListe=[]
    for case in candidats :
        # print(case)
        if   not casesVisitees[case[0]][case[1]] :
            newListe.append(case)
    if newListe==[] :
        # On a fini
        #print(casesVisitees)
        #print(chaine)
        #tousLesMots.add(chaine)
        return chaine
    else : # le else est inutile mais c'est pour voir ce qu'on fait
        for c in newListe :
            visite=list(casesVisitees)
            visite[c[0]][c[1]]=True

            #print(c)
            #print(str(t[0])+"\t"+chaine+plateau[c[0]][c[1]]+"*")
            t[0]+=1
            
            construireChemins(plateau,c[0],c[1],chaine+plateau[c[0]][c[1]],visite)
            visite[c[0]][c[1]]=False
    return
        
            
        
            
            
        



if __name__=="__main__":
    # Ici, arbre, l'arbre lexical est connu
    # et aussi on peut construire une grille de Boogle
    
    plateau=genereBoggle()
    # plateau="BIPNOTIAANTIZLEL"
    imprime(plateau)
    plateau=transforme(plateau)
    for i in range(4):
        for j in range(4):
         print(i,j)   
         visitees=[[False for i in range(4)] for j in range(4)]
         visitees[i][j]=True
         construireChemins(plateau,i,j,plateau[i][j],visitees)
    print(len(solutions))
    s=list(solutions)
    s.sort()
    for mot in s:
        print(mot)

   
