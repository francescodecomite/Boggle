# On génère une grille, on affiche la position des dés.
# Les numéros des dés sont leur index dans la liste *valeurs* dans le
# fichier 


from construireArbre import *
from generation import *
from sys import *
from random import random


solutions=set()

score=0
val=[0,0,0,1,1,2,3,5,11,11,11,11,11,11,11]
def valeur(chaine):
    """    retourne le nombre de points de cette chaine
    """
    p=len(chaine)
    return val[p]
    

# Construire tous les chemins partant d'une case
# desutilises memorise la position des dés qui composent le mot
def construireChemins(plateau,i,j,chaine,casesVisitees,desUtilises):
    global score,passage
    descourants=list(desUtilises)
    descourants.append((i,j))
   
    """
    plateau : le tableau 4x4 qui représente la partie
    i,j : coordonnées de la case de départ
    chaine :  la chaine deja lue le long de ce chemin
    casesVisitees : tableau 4x4 repérant les case devenues inacessibles
    """
   
    
    if estPresent(chaine,arbre) and len(chaine)>2:
        
       
        if not chaine in solutions :
         score+=valeur(chaine)   
         for des in descourants:
            nbVisites[des[0]][des[1]]+=1
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
           
            construireChemins(plateau,c[0],c[1],chaine+plateau[c[0]][c[1]],visite,descourants)
            visite[c[0]][c[1]]=False
    return
        
            
        
            
            
        



if __name__=="__main__":
    # Ici, arbre, l'arbre lexical est connu
    # et aussi on peut construire une grille de Boogle
    highScore=0
    nbSoluces=0
    meilleurPlateau=None
    
   
    k=genereBoggle()
    plateaugenere,positiondesDes=k
    smartImprime(k)
    print("Position des dés ",positiondesDes)
    
    
   
    while(True) :
     solutions=set()
     imprime(plateaugenere)
     plateau=transforme(plateaugenere)
     score=0
     nbVisites=[[0 for i in range(4)] for j in range(4)]
     for i in range(4):
      print(i)
      for j in range(4):
      
       visitees=[[False for i in range(4)] for j in range(4)]
       visitees[i][j]=True
       construireChemins(plateau,i,j,plateau[i][j],visitees,[])
     print("Nombre de solutions ",len(solutions))
     print("\t\tScore ",score)
     print(nbVisites)
     # verification : la somme des valeurs de nbVisites doit etre égale aux nombre de caractères
     # total des solutions
     print("Visites ", sum([sum(c) for c in nbVisites]))
     print("Taille des solutions ",sum([len(c) for c in solutions]))

     # Trouver la position sur le plateau qui a été la moins visitée
     mini=nbVisites[0][0]
     indices=(0,0)
     for i in range(4):
        for j in range(4):
            if nbVisites[i][j]<mini:
                mini=nbVisites[i][j]
                indices=(i,j)
     ind=4*indices[0]+indices[1]
     numeroDe=positiondesDes[ind]
     print("Minimum en case ("+str(indices[0])+","+str(indices[1])+"):"+str(mini))
     print("C'est le dé "+str(numeroDe)+" "+ valeurs[numeroDe])
     lettre=plateaugenere[ind]
     print(lettre)
     newLetter=choice(valeurs[numeroDe])
     # On tourne la face du dé le moins visité
     while newLetter==lettre:
         newLetter=choice(valeurs[numeroDe])
     plateaugenere=plateaugenere[:ind]+newLetter+plateaugenere[ind+1:]
     print("Nouveau plateau : "+plateaugenere)

     # De temps en temps, on secoue un dé au hasard
     if random()<0.2:
         print("Allotage de dé")
         # le numéro du dé à secouer sur le plateau
         indice=randint(0,16)
         print("Indice "+str(indice))
         numeroDe=positiondesDes[indice]
         print(numeroDe)
         lettre=plateaugenere[ind]
         print(lettre)
         newLetter=choice(valeurs[numeroDe])
         # On tourne la face du dé le moins visité
         while newLetter==lettre:
          newLetter=choice(valeurs[numeroDe])
         plateaugenere=plateaugenere[:ind]+newLetter+plateaugenere[ind+1:]
         print("Nouveau plateau : "+plateaugenere)
        
         
         
         
                                                
         
         
        






    

   
