from random import randint

vents =("NE", "N", "NO", "O", "SO", "S", "SE", "E")
direction = vents[randint(0, 7)]
vitesse = randint(0, 300)

print("direction du vent :", direction)
print("vitesse du vent :", vitesse)