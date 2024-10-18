def dollarNaarEuro(dollar_bedrag, wisselkoers):
    return dollar_bedrag * wisselkoers

def faculteit(getal):
    res = 1

    for i in range(getal):
        res *= i

    return res

# Wachtwoord
def valid_wachtwoord(huidig, nieuw):
    return not (huidig == nieuw or len(nieuw) < 8 or " " in nieuw)

huidig = "******"
nieuw = input("Voer een nieuw wachtwoord in")

while not valid_wachtwoord(huidig, nieuw):
    nieuw = input("Da's niet geldig probeer opnieuw: ")