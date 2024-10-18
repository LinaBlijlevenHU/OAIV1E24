HEX_CHAR = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

# Hexwaarde (0x gevolgd door hexadecimale 'getallen')
hexwaarde = "0xABC"

def hex_to_decimal(hexgetal):
    # Remove the prefix indicating it's a hexadecimal
    toconvert = hexgetal.replace("0x", "").replace("#", "")

    # Variable to sum the result
    res = 0
    currentpower = 0

    # Loop over the characters backwards
    for c in toconvert[::-1]:
        # Find the corresponding digit or letter from the
        # array of hexadecimal characters
        i = HEX_CHAR.index(c)

        # Increase for this power of 16
        res += (16**currentpower) * i

        # Next character will be 16 times as valuable
        currentpower += 1

    return res

print(hex_to_decimal(hexwaarde))

assert int(hexwaarde, 16) == hex_to_decimal(hexwaarde)