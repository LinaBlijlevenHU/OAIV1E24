"""
klinkers_pseudocode.py

Deze oefening vertaalt pseudocode naar Python

 Probleem: verwijder alle klinkers uit een stuk tekst
 • Algoritme:
 1. ontvang tekst t
 2. herhaal stap 3. voor elke letter l in t
 3. als l geen klinker is, voeg deze toe aan de nieuwe tekst n
 4. geef n terug
"""

KLINKERS = ["a", "e", "i", "o", "u"]

# Maak alvast de nieuwe string aan (voor stap 3)
n = ""

#  1. ontvang tekst t (hier kunnen we ook een functie inzetten)
t = input("Typ hier je tekst en ontvang deze terug zonder klinkers!\n")

#  2. herhaal stap 3. voor elke letter l in t
for l in t:
    #  3. als l geen klinker is, voeg deze toe aan de nieuwe tekst n
    if l.lower() not in KLINKERS:
        n += l

#  4. geef n terug (als we binnen een functie werken, is dit het punt waar we returnen)
print(f"De tekst zonder klinkers is: \n{n}")

"""
Alternatieven met functies
"""

#  1. ontvang tekst t
def verwijder_klinkers(t):
    n = ""

    #  2. herhaal stap 3. voor elke letter l in t
    for l in t:
        #  3. als l geen klinker is,
        if l.lower() in KLINKERS:
            # voeg deze toe aan de nieuwe tekst n
            n += l

    #  4. geef n terug (als we binnen een functie werken, is dit het punt waar we returnen)
    return n

def verwijder_klinkers_oneliner(t):
    return [l for l in t if l.lower() not in KLINKERS]

# Implementatie met functie
#print(verwijder_klinkers(t))
#print(verwijder_klinkers_oneliner(t))