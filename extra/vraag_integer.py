def vraag_integer():
    getal = input("Typ een heel getal: ")

    try:
        return int(getal)
    except ValueError:
        print("Dat is niet geldig")


def vraag_integer2():
    getal = input("TYp een heel getal:")

    while not getal.isnumeric():
        getal = input("Probeer opnieuw")

    return int(getal)


vraag_integer()