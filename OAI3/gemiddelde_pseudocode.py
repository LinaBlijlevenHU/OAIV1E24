"""
gemiddelde_pseudocode.py

Deze oefening vertaalt pseudocode naar Python

Pseudocode om te vertalen:

 Probleem: gegeven twee getallen, bereken het gemiddelde
 • Algoritme:
 1. ontvang getallen a en b
 2. bereken som = a + b
 3. bereken gemiddelde = som / 2
 4. geef gemiddelde terug
"""

#  1. ontvang getallen a en b
def gemiddelde(a, b):
    # 2. bereken som = a + b
    som = a + b

    # 3. bereken gemiddelde = som / 2
    gemiddelde = som / 2

    # 4. geef gemiddelde terug
    return gemiddelde

a, b = 50, 20
gemiddelde(a, b)