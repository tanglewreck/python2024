# Generera en multiplikationstabell genom loopar inuti loopar.

table_size = int(input("Hur många kolumner ska vi ha?"))
kolumnbredd = 5

kolumn = 1
while kolumn <= table_size:
    # Skriv ut första raden i tabellen
    rad = 1
    while rad <= table_size:
        print(str(kolumn*rad).ljust(kolumnbredd),end="")
        rad += 1
    print()  # mata ut en radbryting för att avsluta raden
    kolumn += 1
