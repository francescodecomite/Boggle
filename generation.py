# Code générant un plateau de Boggle
from random import randint,choice

# Composition des dés


#Valeurs des dés
valeurs=["ETUKNO","EVGTIN","DECAMP","IELRUW","EHIFSE","RECALS","ENTDOS","OFXRIA"
         ,"NEVEDZ","EIOATA","GLENYU","BMAQJO","TLIBRA","SPULTE","AIMSOR","ENHRIS"]


#Secoue le plateau, fournit l'ordre des dés
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
        # On retourne le plateau des lettres, et aussi la position de chaque dé
        # ça permettra de demander de tourner un dé sur une autre face
        # pour optimiser le score
    return (plateau,liste)

# Formate le plateau sous forme d'un tableau 4x4
def transforme(chaine):
    liste=[[chaine[4*j+i] for i in range(4)] for j in range(4)]
    return liste
    
                    
# Afficher le plateau comme une grille de boogle
def imprime(chaine):
    for i in range(4):
        print(chaine[4*i]+" "+chaine[4*i+1]+" "+chaine[4*i+2]+" "+chaine[4*i+3]+" ")
        #print(chaine[4*i:4*i+4])

# Affiche le plateau et la position des dés
def smartImprime(genere) :
    chaine=genere[0]
    des=genere[1]
    for i in range(4):
        s=chaine[4*i]+" "+chaine[4*i+1]+" "+chaine[4*i+2]+" "+chaine[4*i+3]+"\t\t"
        s+=str(des[4*i])+"\t"+str(des[4*i+1])+"\t"+str(des[4*i+2])+"\t"+str(des[4*i+3])
        print(s)

if __name__=="__main__":
    (k,l)=(genereBoggle())
    smartImprime((k,l))
    print(k)
    imprime(k)
    print(transforme(k))
    print(l)
    
