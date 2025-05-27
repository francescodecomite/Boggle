# Code générant un plateau de Boggle
from random import randint,choice

# Composition des dés


#Valeurs des dés
valeurs=["ETUKNO","EVGTIN","DECAMP","IELRUW","EHIFSE","RECALS","ENTDOS","OFXRIA"
         ,"NEVEDZ","EIOATA","GLENYU","BMAQJO","TLIBRA","SPULTE","AIMSOR","ENHRIS"]


#Secoue le plateau, fournit l'ordre des des
def genereBoggle():
    liste=[i for i in range(16)]
    for i in range(16):
        # échanger liste[i] avec un plus lointain
        j=randint(i,15)
        temp=liste[i]
        liste[i]=liste[j]
        liste[j]=temp
    # choisir une lettre parmi 6 sur chaque dé
    plateau=""
    for i in range(16):
        plateau+=choice(valeurs[liste[i]])
    return plateau

# Formate le plateu sous forme d'un tableau 4x4
def transforme(chaine):
    liste=[[chaine[4*j+i] for i in range(4)] for j in range(4)]
    return liste
    
                    
# Afficher comme une grille de boogle
def imprime(chaine):
    for i in range(4):
        print(chaine[4*i]+" "+chaine[4*i+1]+" "+chaine[4*i+2]+" "+chaine[4*i+3]+" ")
        #print(chaine[4*i:4*i+4])

if __name__=="__main__":
    k=genereBoggle()
    print(k)
    imprime(k)
    print(transforme(k))
    
