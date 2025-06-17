class Maison:
    def __init__(self, region: str, ville: str, surface: int, piscine: bool):
        self.type = "maison"
        self.region = region
        self.ville = ville
        self.surface = surface
        self.piscine = piscine
        self.prix = None

    def details(self):
        print("-Une maison | region :", self.region, "| ville :", self.ville, "| surface :", self.surface, "| piscine :", self.piscine, "| prix :", self.prix)


