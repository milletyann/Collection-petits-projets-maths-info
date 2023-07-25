# Allocation dynamique de mémoire

## Objectifs
On s'intéresse à un environnement de développement à mémoire limitée, et on veut limiter la création de nouvelles structures dans la mémoire.
Le principe est d'allouer au fur-et-à-mesure des portions de mémoire, et d'en libérer.
On ne peut écrire que des caractères dans les cases (pour faire plus simple).
On implémente 4 solutions, chacune aura des petites fonctions propres à la structure utilisée, et ses propres fonctions ```reserver(n, c)```
qui ajoute les caractères ```c``` sur une taille de ``n`` dans la mémoire, et ```liberer(p)``` (disponible pour les parties 2, 3 et 4) qui libère 
la portion de mémoire qui commence à ```p``` .

## Structure de données
La mémoire est une liste de taille TAILLE_MEM.
Quand une portion possède une en-tête pour contenir une information, on identifie la portion comme ```p``` l'index dans la mémoire où commencent les données, donc l'en-tête en question est située à l'index ```p-1```.

### Partie 1 : Implémentation naïve
On ne peut pas libérer de portion parce qu'on ne sait pas où est stocké quoi. L'index 0 contient la première position libre dans la mémoire.
On implémente donc une fonction ```reserver(n, c)```.

### Partie 2 : Réservations de blocs de tailles fixes
On ne réserve que des blocs de taille fixe TAILLE_BLOC, dans ce bloc de taille fixe il y a l'en-tête qui vaut 0 si la portion est libre et 1 si elle est réservée.
On implémente une nouvelle fonction ```reserver(n, c)``` et une fonction ```liberer(p)``` qui marque comme libre le bloc qui commence à ```p-1``` (l'en-tête donc).

### Partie 3 : Portions avec en-tête et pied de page
Pour améliorer un peu le nombre de portions libres et pouvoir stocker des données plus grandes sans perdre trop de place, on ajoute une notion de prologue et d'épilogue.
De plus chaque portion contient une en-tête et un pied de page, contenant la même information pour une portion, à savoir la taille de la portion (taille utile, hors en-tête et pdp). Chaque portion est de taille paire, si on veut stocker une taille impaire on rajoute un 0 à la fin.
Ainsi dans l'en-tête et le pied de page on stocke la taille de la portion, +1 si elle est réservée, +0 si elle est libre. Pas de problème d'unicité puisque les tailles sont toujours paires.
Épilogue et prologue sont des portions vides réservées (et ne prennent que 2 cases qui valent toutes 1).
```mem[0]``` contient la position de l'épilogue (seconde place de l'épilogue sur les 2).
La mémoire est initialisée en [4, 1, 1, 1, 1, 0, 0, ..., O].
On implémente à nouveau ```reserver(n, c)```, et ```liberer(p)``` qui cette fois doit vérifier si les portions adjacentes sont libres pour pouvoir fusionner les portions libres afin d'en faire une seule plus grande. De plus si la dernière portion de la zone déjà réservée est libre, on redéplace le prologue pour limiter la zone de réservation

NB : la zone de réservation est la zone où il existe des portions réservées, il peut y avoir de la place plus loin que le prologue.

### Partie 4 : Chaînage explicite des portions libres
Maintenant on veut améliorer la recherche de portions libres.
Donc on maintient une chaîne de portions libres, organisée ainsi:
- Si une portion ```p``` est libre dans la mémoire (donc elle doit être localisée dans la chaîne de portions libres), ```mem[p]``` contient la position de la portion libre prédécesseur, et ```mem[p+1]``` contient la position de la portion libre suivante.
- La position de l'entrée de la chaîne est stockée dans ```mem[1]```, elle ne peut valoir ```0``` que si la chaîne est vide.
- Si la chaîne n'est pas vide, elle contient une portion finale, dont la portion suivante est ```0```.

On implémente les fonctions suivantes (en plus de fonctions basiques)=
- ```ajoute_en_entree_de_chaine(p)``` : ajoute une portion libre ```p``` en tête de la chaîne (qui en fait son entrée).
- ```supprime_dans_chaine(p)``` : qui supprime la portion ```p``` de la chaîne.
- ```demarrage_chaine()``` : la nouvelle fonction d'initialisation de la mémoire selon cette nouvelle implémentation.
- ```reserver(n, c)```
- ```liberer(p)```