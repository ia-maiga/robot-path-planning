from dataclasses import dataclass


@dataclass
class ResultatRecherche:
    chemin: int | None
    cout: int | None
    developpes: int
    generes: int
    ordre: int
