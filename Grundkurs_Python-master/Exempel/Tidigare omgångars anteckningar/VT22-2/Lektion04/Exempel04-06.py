# Generera en multiplikationstabell med loopar inuti loopar.

table_size = int(input("Hur många kolumner ska vi ha?"))
kolumnbredd = 5

kolumn = 1
while kolumn <= table_size:
    # Mata ut en rad med värden.
    rad = 1
    while rad <= table_size:
        print(str(kolumn * rad).rjust(kolumnbredd), end="")
        rad += 1
    print()   # mata ut en radbrytning för att avsluta raden

    kolumn += 1
