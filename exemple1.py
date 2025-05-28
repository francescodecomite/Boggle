# Premier exemple : créer une grille, calculer
# et afficher les solutions et le score


from construireArbre import *
from generation import *


tousLesMots=set()
solutions=set()

t=[0]
k=[0]

# le score pour un mot de $i$ lettres. Pas de points en-dessous de trois lettres. 
val=[0,0,0,1,1,2,3,5,11,11,11,11,11,11,11]
# La fonction pour obtenir les points du mot en fonction de sa longueur.
def valeur(chaine):
    """    retourne le nombre de points de cette chaine
    """
    p=len(chaine)
    return val[p]
    

# Construire tous les chemins partant d'une case
# Je vous laisse explorer le code, décrire son fonctionnement est un peu long
def construireChemins(plateau,i,j,chaine,casesVisitees):
   
    """
    plateau : le tableau 4x4 qui représente la partie
    i,j : coordonnées de la case de départ
    chaine :  la chaine deja lue le long de ce chemin
    casesVisitees : tableau 4x4 repérant les cases devenues inacessibles
    """
    global score
    
    # On a trouvé un mot,on ajoute ses points au score, et on
    # ajoute le mot à l'ensemble des solutions
    if estPresent(chaine,arbre) and len(chaine)>2:
        score+=valeur(chaine)
        solutions.add(chaine)
    # et on continue..
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
    # dans la liste candidats
    # on supprime les cases déja visitées
    newListe=[]
    for case in candidats :
        # print(case)
        if   not casesVisitees[case[0]][case[1]] :
            newListe.append(case)
    if newListe==[] :
        # On a fini, car toutes les cases autour ont été visitées. 
        return 
    else : # le else est inutile mais c'est pour voir ce qu'on fait
        # On est quelque part dans l'arbre lexical, 
        for c in newListe :
            # On descend le long de la branche étiquetée par le caractère
            # de la case voisine
            visite=list(casesVisitees)
            visite[c[0]][c[1]]=True

            #print(c)
            #print(str(t[0])+"\t"+chaine+plateau[c[0]][c[1]]+"*")
            t[0]+=1
            
            construireChemins(plateau,c[0],c[1],chaine+plateau[c[0]][c[1]],visite)
            visite[c[0]][c[1]]=False
    return
        
            
        
            
            
        



if __name__=="__main__":
    # Ici, arbre, l'arbre lexical est connu,
    # parce qu'on a importé construireArbre.py  où le travail est fait
    # On peut construire une grille de Boogle, car generation.py est importé aussi.

    # Vous pouvez choisir d'entrer une grille, ou de la générer au hasard
    # Il suffit de décommenter une des deux lignes suivantes.
    #Dans le cas de la génération aléatoire, il faut prendre uniquement la
    #première composante du couple engendrer par genereBoggle() (dans generation)
    #plateaugenere="DRLAEEALSRPNTIAC"   
    plateaugenere=genereBoggle()[0]
    # L'ensemble qui contiendra toutes les solutions
    solutions=set()
    imprime(plateaugenere)
    # On transforme la description du plateau (chaine de 16 caractères)
    # en un tableau 4x4, plus facile à manipuler à mon avis. 
    plateau=transforme(plateaugenere)
    score=0
    
    for i in range(4):
        # Pour ne pas s'ennuyer pendant que le programme calcule 
        print(i)
        for j in range(4): 
         visitees=[[False for i in range(4)] for j in range(4)]
         visitees[i][j]=True
         construireChemins(plateau,i,j,plateau[i][j],visitees)
    # Afficher les solutions     
    print("Nombre de solutions ",len(solutions))
    print("Score ",score)
    s=list(solutions)
    s.sort()
    for mot in s :
        print(mot)
   
