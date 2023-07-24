from utils import *

### Partie 3 : Portions avec en-tête et pied de page
# maintenant chaque portion à une en-tête et un pied de page d'une case chacun
# On met la même valeur dans les 2 : la taille de la portion + 1 si la portion est reservée
# (0 si elle est libre). Pour l'unicité, si la taille est impaire on rajoute une case. Ainsi
# la taille est toujours paire et si l'en-tête/pied de page est impaire on sait que c'est réservé

# On a une portion PROLOGUE et une portion EPILOGUE qui encadrent les portions mémoires, chacune
# de taille 2 (son en-tête et son pied de page), dont la position est posée par la position de
# son pied de page (ex :  2 pour le prologue, et mem[0] pour l'épilogue).


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


def precedent_est_libre(p):
    return mem[p - 2] % 2 == 0


def precedent_est_reserve(p):
    return mem[p - 2] % 2 == 1


def lire_position_epilogue():
    return mem[0]


def ecrire_position_epilogue(p):
    mem[0] = p


def reserver(n, c):
    p = 4

    # vérifie si on est à l'épilogue où si on est au début d'une portion
    while p != mem[0]:
        t = lire_taille(p)
        if est_libre(p) and (t >= n):
            # 2 cas: y'a la place ou pas pour faire une nouvelle section vide avec
            # ce qu'il reste dans la portion libre (au - 3 cases libres)
            if n <= t - 3:
                marque_reservee(p, n)
                for i in range(n):
                    ecrire(p, i, c)

                p += n + 2
                marque_libre(p, t - n - 2)
            else:
                marque_reservee(p, t)
                for i in range(n):
                    ecrire(p, i, c)

                for i in range(n, t):
                    ecrire(p, i, 0)

            return p

        p += t + 2

    # taille de la portion (sans entete ni pdp)
    t_portion = n + (n % 2)

    # vérifier qu'il reste de la place dans la mémoire
    if TAILLE_MEM - mem[0] - 1 < 2 + t_portion:
        return None

    # réserve la taille qu'il faut en fonction de la taille de ce qu'on veut stocker
    marque_reservee(p, t_portion)
    ecrire_position_epilogue(p + t_portion + 2)

    ecrire(lire_position_epilogue(), 0, 1)
    ecrire(lire_position_epilogue(), -1, 1)

    for i in range(n):
        ecrire(p, i, c)

    return p


def liberer(p):
    # vérifier que p est bien une portion
    p_tmp = 4
    while p_tmp < p:
        p_tmp += lire_taille(p) + 2
        if p_tmp > p:
            # on a dépassé p sans y passer donc p n'est pas un début de portion
            return

    # libérer la portion: modif entete et pdp
    t_p = lire_taille(p)
    marque_libre(p, t_p)
    # regarder si suivante libre: si oui on modifie la taille de la portion liberee en ajoutant la taille de la suivante +2
    p_suivante = p + t_p + 2
    if est_libre(p_suivante):
        t_suivante = lire_taille(p_suivante)
        marque_reservee(p, t_suivante + 2 + t_p)
        return "ok"
    # regarder si precedente libre: si oui on modifie sa taille en ajoutant la taille de la portion liberee (qui aura on pas été ajouté)
    if precedent_est_libre(p):
        t_precedente = lire_taille_precedent(p)
        marque_reservee(p - 2 - t_precedente, t_precedente + 2 + lire_taille(p))
        return "ok"

    return "ok"


mem = demarrage_entete()
print(mem)
reserver(6, "z")
print(mem)
reserver(3, "A")
print(mem)
reserver(2, "g")
print(mem)
# la mémoire est trop petite pour cette allocation donc ça n'alloue pas
reserver(14, "u")
print()
print(mem)
print(liberer(12))
print(mem)
