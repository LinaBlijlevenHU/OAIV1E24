geheimwoord = "ezel"
geraden = "e"

placeholder = ['_'] * len(geheimwoord)

for i in range(len(geheimwoord)):
    karakter = geheimwoord[i]

    if karakter == geraden:
        placeholder[i] = geraden