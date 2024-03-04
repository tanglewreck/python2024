# Generera en multiplikationstabell med loopar inuti loopar.

table_size = int(input("Hur många kolumner ska vi ha?"))
kolumnbredd = 5

rad = 1 # RAD
while rad <= table_size:
    # Mata ut en rad med värden.
    kolumn = 1 # KOLUMN
    while kolumn <= table_size:
        # print(str(rad * kolumn).rjust(kolumnbredd), end="")
        print(str(rad * kolumn), "\t", sep="", end="")
        kolumn += 1
    print()   # mata ut en radbrytning för att avsluta raden

    rad += 1
