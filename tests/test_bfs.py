from pathplanning.bfs import bfs, reconstruire_chemin

def test_reconstruire_chemin_de_l_exercice():
    # Les prédécesseurs trouvés à la main dans l'exercice BFS.
    pred = {
        (0, 0): None,
        (0, 1): (0, 0),
        (0, 2): (0, 1),
        (1, 2): (0, 2),
        (1, 3): (1, 2),
        (2, 2): (1, 2),
        (2, 3): (1, 3),
        (2, 1): (2, 2),
    }
    assert reconstruire_chemin(pred, (2, 3)) == [
        (0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3)
    ]


GRILLE_EXERCICE = [
    [True,  True,  True,  False],
    [False, False, True,  True ],
    [True,  True,  True,  True ],
]

GRILLE_ARRIVEE_ISOLEE = [
    [True, True,  True ],
    [True, False, False],
    [True, False, True ],
]


def test_chemin_de_l_exercice():
    # Le chemin trouvé à la main, avec l'ordre haut, droite, bas, gauche.
    assert bfs(GRILLE_EXERCICE, (0, 0), (2, 3)) == [
        (0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3)
    ]


def test_depart_egal_arrivee():
    assert bfs(GRILLE_EXERCICE, (0, 0), (0, 0)) == [(0, 0)]


def test_arrivee_inaccessible():
    assert bfs(GRILLE_ARRIVEE_ISOLEE, (0, 0), (2, 2)) is None