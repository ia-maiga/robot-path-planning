from pathplanning.grid import voisins

GRILLE = [
    [True,  True,  True,  False],
    [False, False, True,  True ],
    [True,  True,  True,  True ],
]


def test_coin_haut_gauche():
    assert voisins(GRILLE, (0, 0)) == [(0, 1)]


def test_case_avec_trois_voisins():
    assert voisins(GRILLE, (1, 2)) == [(0, 2), (1, 3), (2, 2)]


def test_coin_bas_gauche():
    assert voisins(GRILLE, (2, 0)) == [(2, 1)]


def test_coin_bas_droite():
    assert voisins(GRILLE, (2, 3)) == [(1, 3), (2, 2)]
    
GRILLE2 = [
    [True,  False,  True,  False],
    [False, True, False,  True ],
    [True,  False,  True,  True ],
]

def test_entouree_obstacle():
    assert(voisins(GRILLE2, (1, 1)) == [ ])
    
GRILLE3 = [
    [True]
]

def test_une_case():
    assert(voisins(GRILLE3, (0,0)) == [ ])
    
GRILLE4 = [
    [True,  False,  True,  True],
]

def test_une_ligne():
    assert(voisins(GRILLE4, (0, 3)) == [(0, 2)])