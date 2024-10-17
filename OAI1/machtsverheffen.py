"""
machtsverheffen.py

Je kunt ook machtsverheffen zonder * of **, met alleen de +. Dit is extreem langzaam, maar wel leuk
"""

def vermenigvuldig(a, b, verbose=False):
    """ Vermenigvuldig twee getallen met elkaar door herhaaldelijk op te tellen """
    # We beginnen met tellen vanaf nul: bij optellen starten we altijd vanaf 0
    res = 0

    # Doe b aantal keer
    for i in range(b):
        print(f"{i} * {a} = {res}")

        # Tel 1x a bij het resultaat op
        res += a

    # Return het totaal
    return res

def machtsverheffen(grondtal, exponent):
    """ Machtsverhef door herhaaldelijk te vermenigvuldigen """
    # Met 1 kunnen we veilig vermenigvuldigen
    res = 1

    # We gaan exponent aantal keer het getal met zichzelf vermenigvuldigen
    for i in range(exponent):
        print(f"{grondtal}^{i} = {res}")

        # Gebruik de vermenigvuldig functie (of gewoon res = res * grondtal)
        res = vermenigvuldig(res, grondtal)

    # Geef het resultaat terug
    return res

print(f"Vermenigvuldigen door herhaaldelijk op te tellen: ")
res1 = vermenigvuldig(3, 5)
print(f"Machtsverheffen door herhaaldelijk te vermenigvuldigen door herhaaldelijk op te tellen: ")
res2 = machtsverheffen(3, 4)

# Check tegen de originele Python-functie (testcode voor beginners)
assert res1 == 3*5
assert res2 == 3**4