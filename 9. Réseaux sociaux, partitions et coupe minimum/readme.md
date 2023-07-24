# Réseaux sociaux

## Objectifs
Le but est de regrouper des personnes par affinité dans un réseau social.
Pour cela, on cherche à répartir les personnes en deux groupes de sorte
à minimiser le nombre de liens d'amitié entre les 2 groupes. 
(En gros on cherche une coupe minimale du réseau).

## Structure de données
Les individus sont numérotés de 0 à n-1 (n individus au total). Un lien
d'amitié entre i et j est représenté dans une liste comme un doublet [i, j]
ou [j, i] (l'ordre est pas important).
Un réseau social est donc l'association de 2 éléments, regroupés dans ```reseau```:
- ```reseau[0] = n``` le nombre d'individus dans le réseau
- ```reseau[1]``` la liste non ordonnée des liens d'amitiés entre les individus


### Partie 1 : réseau social
Donne les fonctions d'initialisation basiques et des actions classiques sur 
l'architecture de réseau définie.

### Partie 2 : partitions
Un partition en ```k``` groupes d'un ensemble A consiste en k sous-ensembles disjoints
non-vides dont la réunion est A.
Cette partie implémente une structure efficace de calcul de partitions de n.
La structure en question est une sorte d'arbre (arité arbitraire) (un par partition du coup). La représentation n'est pas unique 
puisqu'elle dépend du choix de la racine/représentant.
On code cette structure dans un tableau ```parent```  où ```parent[i]``` contient 
le numéro du parent de i.
Initialement chaque individu est son propre représentant (```parent[i] = i```).

### Partie 3 : algorithme randomisé de coupe minimum
On met en oeuvre l'algorithme suivant:
1. Créer une partition P en ```n``` singletons de [|n|]
2. Initialement aucun lien d'amitié n'est marqué
3. Tant que la partition P contient au moins trois groupes et qu'un reste des liens d'amitiés non marqués dans le réseau:
    - Choisir le lien uniformément au hasard parmi les liens non-marqués du réseau, noté [i, j]
    - Si i et j n'appartiennent pas au même groupe dans P, on fusionne les 2 groupes correspondants
    - Marquer le lien [i, j]
4. Si P contient ```k>=3``` groupes, on fait ```k-1``` fusions pour obtenir deux groupes
5. Renvoyer la partition P