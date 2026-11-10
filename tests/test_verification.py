from pathplanning.verification import chemin_valide

GRILLE_EXERCICE = [
    [True,  True,  True,  False],
    [False, False, True,  True ],
    [True,  True,  True,  True ],
]


def test_chemin_de_l_exercice_est_valide():
    chemin = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
    assert chemin_valide(GRILLE_EXERCICE, chemin, (0, 0), (2, 3))
    
def test_sortie_par_le_haut():
    # Sort par le haut puis revient : seul défaut, la case (-1, 0).
    chemin = [(0, 0), (-1, 0), (0, 0)]
    assert not chemin_valide(GRILLE_EXERCICE, chemin, (0, 0), (0, 0))


def test_sortie_par_le_bas():
    # Sort par le bas puis revient : seul défaut, la case (3, 3).
    chemin = [(2, 3), (3, 3), (2, 3)]
    assert not chemin_valide(GRILLE_EXERCICE, chemin, (2, 3), (2, 3))