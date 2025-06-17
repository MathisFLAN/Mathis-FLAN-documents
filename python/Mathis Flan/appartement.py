class Appartement:
    def __init__(self, region: str, ville: str, surface: int, etage: int):
        self.type = "appartement"
        self.region = region
        self.ville = ville
        self.surface = surface
        self.etage = etage
        self.prix = None

    def details(self):
        print("-Un appartement | region :", self.region, "| ville :", self.ville, "| surface :", self.surface, "| étage :", self.etage, "| prix :", self.prix)