TAILLE_MEM = 33
TAILLE_BLOC = 4
PROLOGUE = 2


def demarrage_init():
    # initialiser la mémoire
    global mem
    mem = [0] * TAILLE_MEM
    mem[0] = 1

    return mem


def demarrage_entete():
    # initialiser la mémoire
    global mem
    mem = [0] * TAILLE_MEM
    mem[0] = 4
    for i in range(4):
        mem[i + 1] = 1

    return mem


def lire(p, i):
    # renvoie le carac n°i de la portion p (= qui commence à la position p de mem)
    return mem[p + i]


def ecrire(p, i, c):
    # on écrit c à la position i de la portion p
    mem[p + i] = c
