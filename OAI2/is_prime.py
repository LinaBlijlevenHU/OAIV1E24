def is_prime(no) -> bool:
    """
    Check if a number is prime

    :param      int:    The number
    :return     bool:   Is it prime?
    """
    # Check of er delers zijn die niet 1 of het getal zelf zijn
    for i in range(2, no-1):
        # Als we kunnen delen door dit getal zonder rest,
        # heeft het getal meerdere delers en is het dus niet priem.
        if no % i == 0:
            return False

    # Als we geen tegenvoorbeeld kunnen vinden, is het getal alleen deelbaar door zichzelf
    # en 1 en dus priem.
    return True

def test_is_prime():
    # Definieer wat getallen die wel of niet priem zijn
    testgevallen = [
        (8, False),
        (7, True),
        (19, True),
        (48, False),
        (256, False),
        (11, True),
        (37, True),
        (73, True)
    ]

    # Zorg dat de functie het juiste resultaat geeft.
    for testgeval in testgevallen:
        assert is_prime(testgeval[0]) == testgeval[1]

if __name__ == "__main__":
    # Test even of alles goed is gegaan hiho
    test_is_prime()