import math

def explain_logarithm(target, base):
    exponent = math.log(target, base)
    print(f"{base}^x = {target}, "
          f"dan x = {base} log({target}) = {exponent:.1f}, "
          f"want {base}^{exponent:.1f} = {target}")

testgevallen = [
    (8, 2),
    (9, 3),
    (64, 2),
    (125, 5),
    (128, 2),
    (27, 3),
    (0.25, 2),
    (64, 4)
    #(0, 2),            # Kan niet
    #(-4, 2)            # Kan niet
]

for testgeval in testgevallen:
    target, base = testgeval
    explain_logarithm(target, base)