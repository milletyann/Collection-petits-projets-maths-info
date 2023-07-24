import random

### Partie 1 : quelques fonctions utiles pour le réseau


def creerReseauVide(n):
    return [n, []]


def estUnLienEntre(paire, i, j):
    # paire est une liste à 2 élements
    return paire == [i, j] or paire == [j, i]


def sontAmis(reseau, i, j):
    for paire in reseau[1]:
        if estUnLienEntre(paire, i, j):
            return True
    return False


def declareAmis(reseau, i, j):
    if not sontAmis(reseau, i, j):
        reseau[1].append([i, j])


def listeDesAmisDe(reseau, i):
    amis = []
    for paire in reseau[1]:
        if paire[0] == i:
            amis.append(paire[1])
        elif paire[1] == i:
            amis.append(paire[0])
    return amis


### Partie 2 : Partitions


def creerPartitionsSingletons(n):
    return [i for i in range(n)]


# Objectifs des premières fonctions: déterminer si 2 nombres sont dans la même partition et
# fusionner 2 groupes pour n'en faire qu'un
def representant(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i


def fusion(parent, i, j):
    p = representant(parent, i)
    q = representatn(parent, j)
    parent[p] = q


# cette méthode n'est pas efficace, imaginons qu'on fusionne de manière itérative 0 avec tous
# les individus de 1 à n-1, on va obtenir une seule partition en serpent.

# Méthode de compression : pour résoudre le problème on va compresser une partition dès
# qu'on calcule un représentant d'un i, chaque ancêtre de i (y i compris) se retrouve avec
# la représentant de la partition comme parent.


# cette nouvelle optimisation est gratuite, on passe d'une complexité linéaire à
# une complexité linéaire
def representant_compression(parent, i):
    if parent[i] != i:
        j = representant_compression(parent, parent[i])
        parent[i] = j
    return parent[i]


def listeDesGroupes(parent):
    groupes = []  # groupes en cours de formation
    rep = []  # représentants des groupes déjà rencontrés
    l = len(parent)
    for i in range(l):
        r = representant(parent, i)
        k = 0
        while k < len(rep) and rep[k] != r:
            k += 1
        if k == len(rep):
            rep.append(r)
            groupes.append([])
        groupes[k].append(i)
    return groupes


def coupeMinimumRandomisee(reseau):
    n = reseau[0]
    parent = creerPartitionsSingletons(n)
    nbGroupes = n
    nbLiens = len(reseau[1])
    while nbGroupes > 2 and nbLiens > 0:
        nbLiens -= 1
        k = random.randint(0, nbLiens)
        [i, j] = reseau[1][k]
        ri = representant_compression(parent, i)
        rj = representant_compression(parent, j)
        if ri != rj:
            fusion(parent, ri, rj)
            nbGroupes -= 1
        reseau[1][k], reseau[1][nbLiens] = reseau[1][nbLiens], reseau[1, k]
    if nbGroupes > 2:
        r0 = representant_compression(parent, 0)
        i = 1
        while nbGroupes > 2:
            ri = representant_compression(parent, i)
            if r0 != ri:
                fusion(parent, r0, ri)
                nbGroupes -= 1
            i += 1
    return parent
