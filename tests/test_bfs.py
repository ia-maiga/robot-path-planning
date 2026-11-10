from pathplanning.bfs import bfs, reconstruire_chemin
from pathplanning.verification import chemin_valide

# ---------------------------------------------------------------
# Grilles de test
# Convention : (ligne, colonne). True = libre, False = obstacle.
# ---------------------------------------------------------------

# La grille de l'exercice fait à la main.
GRILLE_EXERCICE = [
    [True, True, True, False],
    [False, False, True, True],
    [True, True, True, True],
]

# L'arrivée (2, 2) est entourée d'obstacles : aucun chemin possible.
GRILLE_ARRIVEE_ISOLEE = [
    [True, True, True],
    [True, False, False],
    [True, False, True],
]


# ---------------------------------------------------------------
# Reconstruction du chemin
# ---------------------------------------------------------------


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
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 2),
        (1, 3),
        (2, 3),
    ]


# ---------------------------------------------------------------
# BFS : le chemin trouvé
# ---------------------------------------------------------------


def test_chemin_de_l_exercice():
    # Le chemin trouvé à la main, avec l'ordre haut, droite, bas, gauche.
    resultat = bfs(GRILLE_EXERCICE, (0, 0), (2, 3))
    assert resultat.chemin == [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]


def test_depart_egal_arrivee():
    resultat = bfs(GRILLE_EXERCICE, (0, 0), (0, 0))
    assert resultat.chemin == [(0, 0)]
    assert resultat.cout == 0


def test_arrivee_inaccessible():
    resultat = bfs(GRILLE_ARRIVEE_ISOLEE, (0, 0), (2, 2))
    assert resultat.chemin is None
    assert resultat.cout is None
    assert resultat.developpes == 5
    assert resultat.generes == 5


# ---------------------------------------------------------------
# BFS : les métriques
# ---------------------------------------------------------------


def test_metriques_de_l_exercice():
    # Les valeurs comptées à la main dans l'exercice BFS.
    resultat = bfs(GRILLE_EXERCICE, (0, 0), (2, 3))
    assert resultat.cout == 5
    assert resultat.developpes == 6
    assert resultat.generes == 8
    assert resultat.ordre == [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 2)]


def test_chemin_bfs_est_valide():
    resultat = bfs(GRILLE_EXERCICE, (0, 0), (2, 3))
    assert chemin_valide(GRILLE_EXERCICE, resultat.chemin, (0, 0), (2, 3))
