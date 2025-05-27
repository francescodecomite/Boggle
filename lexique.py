# Construire un arbre à partir d'un lexique
"""
 Un noeud de l'arbre contient :
    - la lettre qui y amène : un caractère
    - mot : boolean vrai si la suite de lettre est mot du lexique
    - les liens vers les suites possibles : un dictionnaire de noeuds
        dont la clé est la lettre du noeud (evite les parcours de liste)
"""
class Noeud :
    def __init__(self,lettre="", mot=False):
        self.lettre=lettre
        self.mot=mot
        self.suites={}

    def __str__(self,indent=""):
        s=indent+"Lettre:\t"+self.lettre+"\n"+indent+"Mot:\t"+str(self.mot)+"\n"
        
        for j in self.suites.keys() :
            s=s+self.suites[j].__str__(indent+"\t")+"\n"
            
        return s
    
    # Ajouter un noeud en feuille d'un arbre
    def add(self,noeud):
        self.suites[noeud.lettre]=noeud
    
    # Ajouter un mot dans un arbre
    def ajouterMot(self,chaine):
        if chaine=="":
            self.mot=True
            return
        # Sinon, si le noeud suivant est déja là
        # descendre sur la branche, en ajoutant un mot amputé de sa
        #premiere lettre
        k=self.suites.get(chaine[0])
        if k!=None:
            # le noeud est dja là, on descend sur la branche
            self.suites[chaine[0]].ajouterMot(chaine[1:])
        else :
            # créer un nouveau noeud, et descendre
            newNoeud=Noeud(chaine[0],False)
            newNoeud.ajouterMot(chaine[1:])
            self.suites[chaine[0]]=newNoeud
        return
        
def estPresent(mot,arbre):
 """
    retourne True si le mot est présent dans l'arbre
 """
 pointeur=arbre.suites[mot[0]]
 mot=mot[1:]
 while mot!="":
        
        if not mot[0] in pointeur.suites.keys():
            return False
        pointeur=pointeur.suites[mot[0]]
        mot=mot[1:]
 return pointeur.mot
        
    
if __name__=="__main__":
    arbre=Noeud('',False)
    arbre.ajouterMot("maison")
    arbre.ajouterMot("maitre")
    arbre.ajouterMot("mai")
    print(estPresent("maisonnette",arbre))
    print(arbre)
    
    
    
