"""
Doe dit eens voor de tweede observatie: (36, 4,3)

num_iterations = 10000
learning_rate = 0,0001
a = 0,00041, b = 0,01189
Itereer num_iterations keer: tweede iteratie = 1
	Voor elke observatie (x_k, y_k): tweede observatie = (36, 4,3)
		error="(" 𝑎+𝑏∙x_k ")"−y_𝑘 ": ???"
		𝑎=𝑎−error∙learning_rate: ???
		𝑏=𝑏−x_k ∙error∙learning_rate: ???

Na 2 keer doorlopen krijgen we dus a = ??? en b= ???
"""

# (% aanwezigheid, eindcijfer)
observatie = (36, 4.3)

# Learning rate/stapgrootte/alpha
learning_rate = 0.0001

# Huidige nulpunt en helling (intercept, coefficient)
a, b = 0.00041, 0.01189

# Voorspelling met huidige a en b
y_pred = a + b * observatie[0]

# Bereken de error
error = y_pred - observatie[1]

# Stel a en b bij
a = a - error * learning_rate
b = b - observatie[0] * error * learning_rate

print(f"Nieuwe functie y_pred = {a} + {b}x")


