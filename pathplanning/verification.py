def chemin_valide(grille, chemin, depart, arrivee):
    """Renvoie True si `chemin` est un chemin valide de `depart`
    à `arrivee` dans `grille`, en 4-connexité. Ne vérifie pas
    l'optimalité."""
    n = len(grille)
    m = len(grille[0])
    if not chemin:
        return False
    if chemin[0] != depart:
        return False
    if chemin[-1] != arrivee:
        return False
    for i, j in chemin:
        if not (i >= 0 and i < n and j >= 0 and j < m):
            return False
        if not grille[i][j]:
            return False
    for (i1, j1), (i2, j2) in zip(chemin, chemin[1:]):
        if (abs(i1 - i2) + abs(j1 - j2)) != 1:
            return False
    return True
