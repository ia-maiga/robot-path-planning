import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

LIBRE, OBSTACLE, DEVELOPPEE, CHEMIN, DEPART, ARRIVEE = range(6)

COULEURS = ListedColormap([
    "#ffffff",  # libre
    "#2b2b2b",  # obstacle
    "#a8d0f0",  # développée
    "#f4a300",  # chemin
    "#2e9e44",  # départ
    "#d63a3a",  # arrivée
])


def construire_matrice(grille, depart, arrivee, resultat):
    """Renvoie une liste de listes d'entiers (un code par case)."""

    # Couche 1 : LIBRE ou OBSTACLE pour chaque case.
    matrice = []
    for ligne in grille:
        rangee = []
        for libre in ligne:
            if libre:
                rangee.append(LIBRE)
            else:
                rangee.append(OBSTACLE)
        matrice.append(rangee)

    # Couche 2 : les cases développées.
    for i, j in resultat.ordre:
        matrice[i][j] = DEVELOPPEE

    # Couche 3 : le chemin, seulement s'il existe.
    if resultat.chemin is not None:
        for i, j in resultat.chemin:
            matrice[i][j] = CHEMIN

    # Couche 4 : le départ et l'arrivée.
    i, j = depart
    matrice[i][j] = DEPART
    i, j = arrivee
    matrice[i][j] = ARRIVEE

    return matrice


def afficher(grille, depart, arrivee, resultat, titre="", fichier=None):
    """Affiche la carte, les cases développées et le chemin.

    Si `fichier` est donné, enregistre l'image au lieu de l'afficher.
    """
    matrice = construire_matrice(grille, depart, arrivee, resultat)

    fig, ax = plt.subplots()
    ax.imshow(matrice, cmap=COULEURS, vmin=0, vmax=5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(
        f"{titre} — coût : {resultat.cout}, "
        f"développés : {resultat.developpes}"
    )

    if fichier:
        fig.savefig(fichier, dpi=150, bbox_inches="tight")
    else:
        plt.show()
    plt.close(fig)