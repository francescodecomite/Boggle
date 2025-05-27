def uniformise(u):
    resu=""
    for c in u:
        if ((c>='a') and (c<='z')):
           resu=resu+c
        else:
            if not c in conversion.keys():
             print(c,"la valeur ",ord(c))
            else:
             resu=resu+conversion[c]
    return resu

conversion={'ö':'o','ö':'o','ä':'a',' ':'','ô':'o','é':'e','.':'','3':'',')':'','ç':'c','9':'','5':'','è':'e','2':'','1':'','î':'i','4':'','(':'','ê':'e','8':'','-':'','â':'a','.':'',"'":'',"â":'a','ã':'a','à':'a','û':'u','ï':'i','ë':'e','ü':'u','ù':'u'}

bizarre=set()
fichier=open("motfrancais.txt",'r',encoding='utf-8')
sortie=open('fancaispurge.txt','w')

listemots=fichier.readlines()
resu=list()
"""
for u in listestations:
    print("\t"+u.lower(),end="")
"""

i=0

for u in listemots:
    lu=u.lower()
    lu=lu[:-1]
    #lu=uniformise(lu)
   
    resu.append(uniformise(lu))
    i+=1

setresu=set(resu)
resu=list(setresu)
resu.sort()
for m in resu:
    sortie.write(m+"\n")
sortie.close()
