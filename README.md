# Boggle

Pas de copyright, de licence ou quoi que ce soit, faaites ce que vous voulez de ces fichiers. 

## Introduction
Une série de petits programmes pour créer et résoudre des grilles de Boggle. J'ajoute aussi un ou des algos pour rechercher des *bonnes* grilles, voir la grille ultime. 

## La liste des fichiers
- **apurelexique.py** : Un programme auxiliaire pour formatter un ficher de lexique (une liste de mots français). Normalement, vous n'en aurez 
pas besoin, sauf si vous récupérez un dictionnaire plus complet que le mien. Si vous en trouvez un, faîtes-moi signe !
- **construireArbre.py** : Partant d'un lexique, construit l'arbre contenant tous les mots dans un arbre, dont les branches sont étiquetées par des lettres. Quand j'aurai 5 minutes, je 
ferai un petit schéma. Normalement, vous n'avez pas à vous soucier de ce programme, il est appelé par un autre programme (voir petit exemple : )
- **francaispurge.txt** : la liste de mots la plus complète que j'aie à ce jour (300000 mots). Ce fichier sert dans le programme, mais vous n'avez normalement pas à y entrer. Sauf pour ajouter des mots qui n'y seraient pas. Je l'ai déjà fait, ils sont au début du fichier. 
- **generation.py** : Le code qui génère un plateau de Boggle avec les dés français. La fonction **genereBoggle()** construit un couple, dont le premier élément est une chaîne de 16 caractères représentant le plateau, ligne par ligne. Le second élément est la place de chacun des dés utilisés, je pense l'utiliser pour optimiser les scores : pouvoir retourner un dé sans toucher aux 
autres dés. 
- **lexique.txt** : Une liste de 130000 mots français, avec des caractères spéciaux. Plus très utile, puisque j'ai un lexique plus complet. 
- **lexiquepurge.txt** : Le même lexique, sans les caractères spéciaux. 
- **motfrancais.txt** : Le dictionnaire de 300000 mots, qui donne **francaispurge.txt** une fois nettoyé des caractères spéciaux. 
- **README.md** : ce fichier
- **union.py** : Le programme principal, un peu brouillon. J'ajouterai des fichiers d'exemples d'utilisation plus simples au fur et à mesure. 
- **exemple1.py** : Un programme basique qui crée ou utilise une grille, et calcule les solutions. Vous pouvez comparer ses résultats avec les grilles générées [ici](https://www.boggle.fr/index.php) : 
décommentez la ligne 143 et recopiez le plateau généré sur le site. Boggle.fr trouve environ 10% de mots en plus, vous pouvez les rajouter à **francaispurge.txt**

## Utilisation
### Créer une grille, chercher tous les mots, afficher le score et les solutions
Testez le programme **exemple1.py**
