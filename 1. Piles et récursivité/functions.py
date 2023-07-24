# une pile est représentée par une liste dont on n'ajoute qu'en dernière place et ne retire que par la fin
# aucune fonction prédéfinie n'est autorisée à part .append(), .pop() et les petits trucs comme len()
# les boucles sont interdites également et il faut que toutes les fonctionnes soient récursives

def application(p, f):
    # applique f à chaque élément de p
    if len(p) == 1:
        return [f(p.pop())]
    elem = p.pop()
    l = application(p, f)
    l.append(f(elem))
    return l
    

def somme(p):
    # somme les éléments de p
    if len(p) == 1:
        return p.pop()        
    elem = p.pop()
    return somme(p)+elem

def maximum(p):
    # retourne le maximum de la pile
    if len(p) == 1:
        return p.pop()
    elem = p.pop()
    return max(elem, maximum(p))

def concatenation(p1, p2):
    # dépile les éléments de p2 pour les empiler au dessus de p1
    if len(p2) == 1:
        elem = p2.pop()
        p1.append(elem)
        return p1
    elem = p2.pop()
    concatenation(p1, p2).append(elem)
    return p1

def element(p, k):
    # renvoie le k-ième élément de p
    if k == 0:
        return p.pop()
    p.pop()
    return element(p, k-1)

def supprime(p, k):
    # supprime le k-ième élément de p
    if k == 0:
        p.pop()
        return p
    elem = p.pop()
    supprime(p, k-1).append(elem)
    return p

def insertion(p, y, k):
    # insère y en k-ième position de la liste
    if k == 0:
        p.append(y)
        return p
    elem = p.pop()
    l = insertion(p, y, k-1)
    l.append(elem)
    return l

def supprime_element(p, y):
    # supprime tous les y dans p
    if len(p) == 0:
        return []
    
    elem = p.pop()
    if elem == y:
        return supprime_element(p, y)
    l = supprime_element(p, y)
    l.append(elem)
    return l
    
def supprime_repetitions(p):
    # supprime les répétitions dans la pile en gardant celui le plus profond
    if len(p) == 1:
        return p
        
    elem = p.pop()
    l = supprime_repetitions(p)
    if elem in l:
        return l
    l.append(elem)
    return l


def f(x):
    return x*x

p = [3, 2, 12, 1, 3, 4, 12, 3]
p2 = [4, 3]

print(supprime_repetitions(p))