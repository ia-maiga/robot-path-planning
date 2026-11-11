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

## 2026-11-03
- voisins : vérification des 4 bornes avant l'accès à la grille (court-circuit de and).
- voisins ne filtre pas les cases déjà vues : c'est le rôle de l'algorithme de recherche.

## 2026-11-04
- BFS : le dictionnaire pred sert aussi d'ensemble « déjà vue ».
- Test d'arrivée juste après popleft() : arrêt à l'extraction.
- Pas de chemin : BFS renvoie None, jamais un message texte.

## 2026-11-10
- BFS renvoie un ResultatRecherche (dataclass partagée par les trois algorithmes).
- Développés : comptés après le test d'arrivée, donc l'arrivée n'est pas comptée.
- Générés : len(pred), départ inclus.
- Coût : len(chemin) - 1. Sans chemin, chemin et coût valent None.
- Vérificateur chemin_valide : indépendant de voisins, pour ne pas partager ses bugs.
- Adjacence vérifiée par distance de Manhattan égale à 1.
- Ne vérifie pas l'optimalité : celle-ci sera contrôlée en comparant les coûts des 3 algorithmes.
- Vérificateur chemin_valide : indépendant de voisins, pour ne pas partager ses bugs.
- Adjacence vérifiée par distance de Manhattan égale à 1.
- Chaque test d'invalidité ne viole qu'une seule condition (vérifié par mutation).

Caractère	Signification
    .	     case libre
    #	     obstacle
    S      départ, case libre
    G      arrivée, case libre