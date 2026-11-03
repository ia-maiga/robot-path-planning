# Convention : (ligne, colonne) partout

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # haut, droite, bas, gauche


def voisins(grille, case):
    """Renvoie la liste des cases voisines libres de `case`,
    dans l'ordre haut, droite, bas, gauche."""
    n = len(grille)       # nombre de lignes
    m = len(grille[0])    # nombre de colonnes
    i, j = case
    voisin = []
    for di, dj in DIRECTIONS:
        ni = i+di
        nj = j+dj
        if (ni>=0 and ni < n and nj>=0 and nj < m) and grille[ni][nj]:
            voisin.append((ni, nj))
    return voisin
        
        
        
