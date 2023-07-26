from utils import *


def est_reservee(p):
    return mem[p - 1] % 2 == 1


def est_libre(p):
    return mem[p - 1] % 2 == 0


def marque_reservee(p, taille):
    # taille est forcément un nombre pair
    # (=> si n est impair il faut lui avoir rajouté 1 avant)
    mot = taille + 1
    mem[p - 1] = mot
    mem[p + taille] = mot


def marque_libre(p, taille):
    mot = taille
    mem[p - 1] = mot
    mem[p + taille] = mot


def lire_taille(p):
    return 2 * (mem[p - 1] // 2)


def lire_taille_precedent(p):
    return 2 * (mem[p - 2] // 2)


def lire_position_epilogue():
    return mem[0]


def ecrire_position_epilogue(p):
    mem[0] = p


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


def precedent_est_libre(p):
    return mem[p - 2] % 2 == 0


def precedent_est_reserve(p):
    return mem[p - 2] % 2 == 1


def chaine_est_vide():
    return lire_entree_chaine() == 0


def ajoute_en_entree_de_chaine(p):
    e = lire_entree_chaine()
    if e == 0:
        # on est au début, et la valeur du prédécesseur n'indique
        # pas sa position (contrairement à tous les autres maillons
        # de la chaîne)
        mem[1] = p
    else:
        ecrire_predecesseur(e, p)

    ecrire_successeur(p, e)
    ecrire_predecesseur(p, 0)
    ecrire_entree_chaine(p)


def supprime_dans_chaine(p):
    pred = lire_predecesseur(p)
    suiv = lire_successeur(p)
    ecrire_successeur(pred, suiv)

    if suiv != 0:
        ecrire_predecesseur(suiv, pred)


def reserver(n, c):
    p_libre = mem[1]
    t = lire_taille(p_libre)

    while p_libre != 0:
        t = lire_taille(p_libre)

        if t >= n:
            t_portion = n + (n % 2)
            if t_portion <= t - 3:
                marque_reservee(p_libre, t_portion)
                initialiser(p_libre, t_portion, c)

                supprime_dans_chaine(p_libre)
                marque_libre(p_libre + t_portion + 2, t - t_portion - 2)
                ajoute_en_entree_de_chaine(p_libre + t_portion + 2)
                return p_libre
            else:
                marque_reservee(p_libre, t)
                supprime_dans_chaine(p_libre)
                initialiser(p_libre, n, c)
                initialiser(p_libre + n, t - n, 0)
                return p_libre

            # la fonction lire_successeur fonctionne pas sûrement
            # pour des raisons de localité j'ai pas le temps de voir
            p_libre = mem[p_libre + 1]

    # si on est ici c'est qu'on a finito la chaine et qu'on n'a pas pu trouver de place
    e = mem[0]
    t_portion = n + (n % 2)
    if TAILLE_MEM - e - 1 < t_portion + 2:
        return None
    marque_reservee(e, t_portion)
    ecrire_position_epilogue(e + t_portion + 2)
    initialiser(e, n, c)
    initialiser(e + n, t_portion - n, 0)
    initialiser(lire_position_epilogue() - 1, 2, 1)
    return e


def liberer(p):
    p_tmp = 5
    while p_tmp < p:
        p_tmp += lire_taille(p_tmp) + 2
        if p_tmp > p:
            return None

    t_p = lire_taille(p)
    ajoute_en_entree_de_chaine(p)
    marque_libre(p, t_p)
    # regarder si suivante libre: si oui on modifie la taille de la portion liberee en ajoutant la taille de la suivante +2
    p_suivante = p + t_p + 2
    if est_libre(p_suivante):
        t_suivante = lire_taille(p_suivante)

        supprime_dans_chaine(p_suivante)
        supprime_dans_chaine(p)
        marque_reservee(p, t_suivante + 2 + t_p)
        initialiser(p, t_suivante + 2 + t_p, 0)  # opt: pour visualiser
        marque_libre(p, t_suivante + 2 + t_p)
        ajoute_en_entree_de_chaine(p)

    # regarder si precedente libre: si oui on modifie sa taille en ajoutant la taille de la portion liberee (qui aura on pas été ajouté)
    if precedent_est_libre(p):
        t_precedente = lire_taille_precedent(p)
        t_p = lire_taille(p)
        p -= 2 + t_precedente
        supprime_dans_chaine(p)
        supprime_dans_chaine(p + t_precedente + 2)
        marque_reservee(p, t_precedente + 2 + t_p)
        initialiser(p, t_precedente + 2 + t_p, 0)  # opt: pour visualiser
        marque_libre(p, t_precedente + 2 + t_p)
        ajoute_en_entree_de_chaine(p)

    # si la portion suivante est l'épilogue, on le rapproche
    if lire_position_epilogue() == p + lire_taille(p) + 2:
        ecrire_position_epilogue(p)
        supprime_dans_chaine(p)
        initialiser(p - 1, 2, 1)
        initialiser(p + 1, TAILLE_MEM - p - 1, 0)

    return


mem = demarrage_chaine()
print(mem)
p1 = reserver(2, "A")
p2 = reserver(2, "B")
p3 = reserver(2, "C")
p4 = reserver(2, "D")
p5 = reserver(1, "E")
p6 = reserver(1, "F")
# pas la place de réserver p7
p7 = reserver(1, "Z")
print(mem)
liberer(p5)
liberer(p3)
# liberer(p4)
liberer(p1)
# liberer(p6)
print(mem)
p7 = reserver(2, "U")
print(mem)
