from pathplanning.bfs import bfs
from pathplanning.grid import lire_carte
from pathplanning.visualisation import afficher

grille, depart, arrivee = lire_carte("maps/labyrinthe.txt")
resultat = bfs(grille, depart, arrivee)
afficher(grille, depart, arrivee, resultat,
         titre="BFS", fichier="results/figures/bfs_labyrinthe.png")