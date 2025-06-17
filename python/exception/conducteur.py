class Conducteur:
    def __init__(self, nom: str, vitesse: int, points: int):
        self.nom = nom
        self.vitesse = vitesse
        self.route = None
        self.points = points
        self.amende = 0

    def rouler(self, route_obj):
        if self.vitesse > route_obj.vitesse_limit:
            self.amende += 30
            self.points -= 1
            raise Exception("Vous roulez à", self.vitesse,"au lieu de", route_obj.vitesse_limit,", vous avez une amende de 30€ et 1 points de retrait")
        if self.vitesse > route_obj.vitesse_limit + 30:
            self.amende += 90
            self.points -= 3
            raise Exception("Vous roulez à", self.vitesse,"au lieu de", route_obj.vitesse_limit,", vous avez une amende de 90€ et 3 points de retrait")
        self.route = route_obj
        print("Tout est bon pour ce conducteur")