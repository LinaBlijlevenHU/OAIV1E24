"""
3 * 2 * 1 = 6 = 3!

Mogelijke volgordes (zonder herhaling)
a b c
a c b
b a c
b c a
c a b
c b a

Stel: a, b, c, d
4 * 3 * 2 * 1 = 4!
Hoe berekenen we dit?
"""

# Bereken de faculteit van een getal
def faculteit(getal):
    # Initiële waarde om mee te vermenigvuldigen
    res = 1

    # Loop achteruit van het hoogste getal naar de laagste
    for i in range(getal, 0, -1):
        # Vermenigvuldig het huidige resultaat
        res *= i

    return res

print(faculteit(4))