from collections import deque

from pathplanning.grid import voisins
from pathplanning.resultat import ResultatRecherche


def reconstruire_chemin(pred, arrivee):
    """Remonte les prédécesseurs depuis `arrivee` jusqu'au départ,
    et renvoie le chemin dans l'ordre départ → arrivée."""
    chemin = []
    case = arrivee
    while case is not None:
        chemin.append(case)
        case = pred[case]
    chemin.reverse()
    return chemin


def bfs(grille, depart, arrivee):
    """Cherche un plus court chemin de `depart` à `arrivee` avec BFS.

    Renvoie un ResultatRecherche. Si aucun chemin n'existe,
    ses champs `chemin` et `cout` valent None.
    """
    pred = {depart: None}
    file = deque([depart])
    developpes = 0
    ordre = []

    while file:
        u = file.popleft()

        if u == arrivee:
            chemin = reconstruire_chemin(pred, arrivee)
            return ResultatRecherche(
                chemin=chemin,
                cout=len(chemin) - 1,
                developpes=developpes,
                generes=len(pred),
                ordre=ordre,
            )

        developpes += 1
        ordre.append(u)

        for v in voisins(grille, u):
            if v not in pred:
                pred[v] = u
                file.append(v)

    return ResultatRecherche(
        chemin=None,
        cout=None,
        developpes=developpes,
        generes=len(pred),
        ordre=ordre,
    )
