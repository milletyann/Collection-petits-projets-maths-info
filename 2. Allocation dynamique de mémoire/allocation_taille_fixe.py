from utils import *

### Partie 2 : Réservations de blocs de tailles fixes
# allouer cette fois des blocs de taille fixe TAILLE_BLOC,
# chaque première case de bloc vaut 1 si le bloc est occupé, 0 s'il est libre
# si une allocation est plus petite que TAILLE_BLOC, le reste des cases du bloc est perdue


def lire_prochain():
    return mem[0]


def ecrire_prochain(p):
    mem[0] = p


def est_reservee(p):
    return mem[p - 1] == 1


def est_libre(p):
    return mem[p - 1] == 0


def marque_reservee(p):
    mem[p - 1] = 1


def marque_libre(p):
    mem[p - 1] = 0


def reserver_taille_fixe(n, c):
    if n > TAILLE_BLOC - 1:
        return None

    for i in range(int((TAILLE_MEM - 1) / TAILLE_BLOC)):
        portion = i * TAILLE_BLOC + 2

        if est_libre(portion):
            marque_reservee(portion)
            for j in range(n):
                ecrire(portion, j, c)
            for j in range(n, TAILLE_BLOC - 1):
                ecrire(portion, j, 0)

            if not portion < mem[0]:
                mem[0] += TAILLE_BLOC

            return portion
    return None


def liberer_taille_fixe(p):
    marque_libre(p)
    if p == mem[0] - TAILLE_BLOC + 1:
        mem[0] -= TAILLE_BLOC


mem = demarrage_init()
print(mem)
reserver_taille_fixe(3, "p")  # vérifier que ça alloue correctement
print(mem)
reserver_taille_fixe(2, "z")  # pareil (à la suite et seulement 2 cases pas 3)
print(mem)
reserver_taille_fixe(3, "U")  # pareil
print(mem)
liberer_taille_fixe(6)  # libérer correctement les 2 'z'
print(mem)
reserver_taille_fixe(2, "a")  # vérifier que ça alloue bien à l'endroit le plus proche
print(mem)
liberer_taille_fixe(10)  # vérifier qu'on libère bien les 'U'
print(mem)
reserver_taille_fixe(
    2, "x"
)  # vérifier qu'on réécrit bien sur toute la portion (sinon on aurait 'x', 'x', 'U' et ça remttrait le 'U' dans la mémoire connue)
print(mem)
