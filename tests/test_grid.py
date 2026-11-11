import pytest

from pathplanning.grid import voisins
from pathplanning.grid import lire_carte, voisins

# ---------------------------------------------------------------
# Grilles de test
# Convention : (ligne, colonne). True = libre, False = obstacle.
# ---------------------------------------------------------------

# La grille de l'exercice fait à la main.
GRILLE_EXERCICE = [
    [True,  True,  True,  False],
    [False, False, True,  True ],
    [True,  True,  True,  True ],
]

# La case (1, 1) est libre, ses 4 voisins orthogonaux sont des obstacles,
# mais ses 4 diagonales sont libres.
GRILLE_CASE_ENTOUREE = [
    [True,  False, True,  False],
    [False, True,  False, True ],
    [True,  False, True,  True ],
]

GRILLE_UNE_CASE = [
    [True],
]

GRILLE_UNE_LIGNE = [
    [True, False, True, True],
]


# ---------------------------------------------------------------
# Tests sur la grille de l'exercice
# ---------------------------------------------------------------

def test_coin_haut_gauche():
    assert voisins(GRILLE_EXERCICE, (0, 0)) == [(0, 1)]


def test_case_avec_trois_voisins():
    assert voisins(GRILLE_EXERCICE, (1, 2)) == [(0, 2), (1, 3), (2, 2)]


def test_coin_bas_gauche():
    assert voisins(GRILLE_EXERCICE, (2, 0)) == [(2, 1)]


def test_coin_bas_droite():
    assert voisins(GRILLE_EXERCICE, (2, 3)) == [(1, 3), (2, 2)]


# ---------------------------------------------------------------
# Cas particuliers
# ---------------------------------------------------------------

def test_case_entouree_d_obstacles():
    # Vérifie aussi que les diagonales ne sont pas des voisins.
    assert voisins(GRILLE_CASE_ENTOUREE, (1, 1)) == []


def test_grille_d_une_seule_case():
    assert voisins(GRILLE_UNE_CASE, (0, 0)) == []


def test_bord_droit_d_une_grille_d_une_ligne():
    assert voisins(GRILLE_UNE_LIGNE, (0, 3)) == [(0, 2)]
    


def test_lire_carte_exemple():
    grille, depart, arrivee = lire_carte("maps/exemple.txt")
    assert grille == GRILLE_EXERCICE
    assert depart == (0, 0)
    assert arrivee == (2, 3)


def test_lire_carte_sans_arrivee(tmp_path):
    fichier = tmp_path / "carte.txt"
    fichier.write_text("S..\n...\n")
    with pytest.raises(ValueError):
        lire_carte(fichier)