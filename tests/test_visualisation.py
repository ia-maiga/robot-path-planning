from pathplanning.bfs import bfs
from pathplanning.grid import lire_carte
from pathplanning.visualisation import construire_matrice


def test_matrice_de_l_exemple():
    grille, depart, arrivee = lire_carte("maps/exemple.txt")
    resultat = bfs(grille, depart, arrivee)
    assert construire_matrice(grille, depart, arrivee, resultat) == [
        [4, 3, 3, 1],
        [1, 1, 3, 3],
        [0, 0, 2, 5],
    ]