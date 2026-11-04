from collections import deque

from pathplanning.grid import voisins


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
    """Renvoie un plus court chemin de `depart` à `arrivee`
    (liste de cases), ou None s'il n'en existe pas."""
    pred = {depart:None}
    file = deque([depart])
    while file:
        u = file.popleft()
        if u == arrivee:
            return reconstruire_chemin(pred, arrivee)
        for v in voisins(grille, u):
            if v not in pred:
                pred[v] = u
                file.append(v)
    return None