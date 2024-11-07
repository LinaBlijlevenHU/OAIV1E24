"""
gemiddelde_lijst.py

Bereken het gemiddelde van een lijst

Pseudocode:
# Ontvang meerdere getallen in een lijst
# Pak de som van de lijst
# Deel door de lengte van de lijst
# Geef gemiddelde terug
"""

import random

def gemiddelde(lijst):
    som = sum(lijst)
    lengte = len(lijst)
    gemiddelde = som / lengte
    return gemiddelde

def gemiddelde_oneliner(lijst):
    return sum(lijst) / len(lijst)

# Pak 7 getallen tussen 1 en 50
lijst = random.sample(range(1, 51), 7)
print(lijst)