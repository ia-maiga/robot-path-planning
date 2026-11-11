# Convention : (ligne, colonne) partout

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # haut, droite, bas, gauche


def voisins(grille, case):
    """Renvoie la liste des cases voisines libres de `case`,
    dans l'ordre haut, droite, bas, gauche."""
    n = len(grille)  # nombre de lignes
    m = len(grille[0])  # nombre de colonnes
    i, j = case
    voisin = []
    for di, dj in DIRECTIONS:
        ni = i + di
        nj = j + dj
        if (ni >= 0 and ni < n and nj >= 0 and nj < m) and grille[ni][nj]:
            voisin.append((ni, nj))
    return voisin
            
            
def lire_carte(nom_fichier):
    """Lit une carte texte et renvoie (grille, depart, arrivee).
    
    '.' = libre, '#' = obstacle, 'S' = départ, 'G' = arrivée.
    """
    with open(nom_fichier) as f:
        lignes = [l for l in f.read().splitlines() if l]   # ignore les lignes vides

    grille = []
    depart = None
    arrivee = None

    for i, ligne in enumerate(lignes):
        rangee = []
        for j, c in enumerate(ligne):
            rangee.append(c != '#')
            if c == 'S':
                depart = (i, j)
            if c == 'G': 
                arrivee = (i, j)
        grille.append(rangee)

    if depart is None or arrivee is None:
        raise ValueError("Pas de départ ou d'arrivée")
    return grille, depart, arrivee