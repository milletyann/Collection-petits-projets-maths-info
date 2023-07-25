from utils import *


def lire_entree_chaine():
    return mem[1]


def ecrire_entree_chaine(p):
    mem[1] = p


def lire_predecesseur(p):
    return lire(p, 0)


def lire_successeur(p):
    return lire(p, 1)


def ecrire_predecesseur(p, predecesseur):
    ecrire(p, 0, predecesseur)


def ecrire_successeur(p, successeur):
    ecrire(p, 1, successeur)


def chaine_est_vide():
    return lire_entree_chaine() == 0


def ajoute_en_entree_de_chaine(p):
    e = lire_entree_chaine()
    ecrire_predecesseur(e, p)
    ecrire_successeur(p, e)
    ecrire_predecesseur(p, 0)
    ecrire_entree_chaine(p)


def supprime_dans_chaine(p):
    pred = lire_predecesseur(p)
    suiv = lire_successeur(p)
    ecrire_successeur(pred, suiv)
    ecrire_predecesseur(suiv, pred)


def reserver(n, c):
    return


def liberer(p):
    return


mem = demarrage_chaine()
print(mem)
