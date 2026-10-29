# Journal de décisions

## 2026-10-29 — Cadrage du projet

### Périmètre V1
- Grille 2D finie, obstacles fixes et connus à l'avance.
- Déplacements déterministes, robot assimilé à un point.
- Coût de 1 par déplacement. Les coûts variables (terrain) sont une extension prévue.

### Règles de déplacement
- Convention (ligne, colonne) partout.
- 4-connexité, ordre des voisins fixé : haut, droite, bas, gauche.

### Métriques
- Métrique principale : nombre de nœuds développés (retirés de la frontière).
- Métriques secondaires : nœuds générés, coût du chemin, temps de calcul.
- Le temps mesure l'implémentation Python, pas seulement l'algorithme.
- Taux de solvabilité des cartes, à distinguer de la réussite des algorithmes.

### Protocole
- Test d'arrivée à l'extraction de la frontière, pour les trois algorithmes.
- Mêmes cartes, mêmes départs et arrivées pour tous les algorithmes.
- Règle de départage des égalités d'A* à fixer et documenter.

### Environnement
- WSL (Ubuntu), projet dans le disque Linux.
- Environnement Conda dédié : `robot`, Python 3.12.
- Paquet `pathplanning/` plutôt que `src/`, pour simplifier les imports avec pytest.