from pathplanning.verification import chemin_valide

GRILLE_EXERCICE = [
    [True, True, True, False],
    [False, False, True, True],
    [True, True, True, True],
]

CHEMIN_VALIDE = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]


def test_chemin_de_l_exercice_est_valide():
    assert chemin_valide(GRILLE_EXERCICE, CHEMIN_VALIDE, (0, 0), (2, 3))


def test_sortie_par_le_haut():
    # Sort par le haut puis revient : seul défaut, la case (-1, 0).
    chemin = [(0, 0), (-1, 0), (0, 0)]
    assert not chemin_valide(GRILLE_EXERCICE, chemin, (0, 0), (0, 0))


def test_sortie_par_le_bas():
    # Sort par le bas puis revient : seul défaut, la case (3, 3).
    chemin = [(2, 3), (3, 3), (2, 3)]
    assert not chemin_valide(GRILLE_EXERCICE, chemin, (2, 3), (2, 3))


def test_chemin_vide():
    # Seul défaut : le chemin est vide.
    assert not chemin_valide(GRILLE_EXERCICE, [], (0, 0), (2, 3))


def test_mauvais_depart():
    # Seul défaut : le chemin commence en (0, 0), pas en (0, 1).
    assert not chemin_valide(GRILLE_EXERCICE, CHEMIN_VALIDE, (0, 1), (2, 3))


def test_mauvais_arrivee():
    # Seul défaut : le chemin finit en (2, 3), pas en (2, 2).
    assert not chemin_valide(GRILLE_EXERCICE, CHEMIN_VALIDE, (0, 0), (2, 2))


def test_obstacle():
    # Seul défaut : la case (1, 0) est un obstacle.
    chemin = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
    assert not chemin_valide(GRILLE_EXERCICE, chemin, (0, 0), (2, 3))


def test_saut():
    # Seul défaut : le pas de (0, 0) à (0, 2) a une distance de Manhattan de 2.
    chemin = [(0, 0), (0, 2), (1, 2), (1, 3), (2, 3)]
    assert not chemin_valide(GRILLE_EXERCICE, chemin, (0, 0), (2, 3))


def test_diagonale():
    # Seul défaut : déplacement en diagonale entre les cases (0, 1) et (1, 2).
    chemin = [(0, 0), (0, 1), (1, 2), (1, 3), (2, 3)]
    assert not chemin_valide(GRILLE_EXERCICE, chemin, (0, 0), (2, 3))
