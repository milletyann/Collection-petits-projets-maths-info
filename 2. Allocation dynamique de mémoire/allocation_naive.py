from utils import *

### Partie 1 : Implémentation naïve
# Le premier élément de mem est l'indice de la prochaine case libre
# naïf car on ne peut pas implémenter de libération de mémoire


def reserver_naive(n, c):
    if TAILLE_MEM < n + mem[0]:
        return None
    initialiser(mem[0], n, c)
    mem[0] += n
    return mem[0]


mem = demarrage_init()
print(mem)
initialiser(mem[0], 2, "w")
mem[0] += 2
print(mem)
reserver_naive(2, "z")
print(mem)
