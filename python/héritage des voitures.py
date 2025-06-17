class Voiture:
    def __init__(self, marque: str, couleur: str, reservoir: int) -> None:
        self.marque = marque
        self.couleur = couleur
        self.reservoir = reservoir

    def __str__(self) -> str:
        return f"[marque: {self.marque} couleur: {self.couleur} reservoir:{self.reservoir}]"
    
    def run (self) -> int:
        distance = 0
        while self.reservoir > 0 :
            distance += self.reservoir/5*100
        return distance
    
class Sport(Voiture):
    def __init__(self, marque: str, couleur: str, reservoir: int, power: str):
        super().__init__(marque, couleur, reservoir)
        self._power = power
    
V1 = Voiture("Tesla", "verte", 40)
V2 = Voiture("Ford Fiesta", "Blanche", 42)

V3 = Sport("mercedes", "noire", 80, 200)

print(V1.run())
print(V2.run())

print(V1)