from utils import *

### Partie 1 : Implémentation naïve
# Le premier élément de mem est l'indice de la prochaine case libre
# naïf car on ne peut pas implémenter de libération de mémoire


def initialiser_naive(p, n, c):
    # initialise la portion p de taille n avec des caractères c
    for i in range(n):
        ecrire(p, i, c)
    mem[0] += n


def reserver_naive(n, c):
    if TAILLE_MEM < n + mem[0]:
        return None
    initialiser_naive(mem[0], n, c)
    return mem[0]


mem = demarrage_init()
print(mem)
initialiser_naive(mem[0], 2, "w")
print(mem)
reserver_naive(2, "z")
print(mem)
