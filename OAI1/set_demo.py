# Alle studenten die CSC volgen
csc_studenten = {"Ticho", "Silo", "Jian"}
# Alle studenten die PROG volgen
prog_studenten = {"Merlijn", "Emil", "Lucas", "Ticho"}

print("Emil" in prog_studenten)
print("Emil" not in csc_studenten)

# Met union vinden we het totaal van alle elementen (geen dubbele)
print(prog_studenten.union(csc_studenten))

# Wie volgt er beide vakken?
print(prog_studenten.intersection(csc_studenten))