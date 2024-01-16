# Den här filen ska kunna importeras från ÖvningExtra-02 och ÖvningExtra-03.py.

# I den här filen så finns en rad uppgifter. Vissa bygger på varandra och
# vissa måste lösas för att ÖvningExtra-02 ska fungera. Fastnar ni nånstans,
# fortsätt till nästa uppgift och kom tillbaka senare så kanske ni kommer
# på en ny lösning.

# Glöm inte att göra uppgifterna i main(), nedan; det är fem (5) uppgifter i
# denna fil.


personer = [("Anna Andersson", 23, 172), ("Bertil Bengtsson", 27, 186),
            ("Harold Hasselblad", 52, 184), ("Gustav Grip", 47, 176),
            ("Felicia Fagerholm", 28, 190), ("Emma Eriksson", 21, 185),
            ("Caesar Carlander", 43, 178), ("David Dahlgren", 34, 177),
            ]


# Övning: Skriv om koden nedan så att listan alphabetic_list_of_first_names
# endast innehåller personers förnamn och att de står i alfabetisk ordning.
# Det går att lösa på bara en rad men upp till åtta är rimligt.
# (Ni kan döpa om listan, det långa namnet är bara för tydlighet. Glöm inte
# att ändra i main() i så fall.)
alphabetic_list_of_first_names = personer


# Övning: Skriv om raden nedan så att list_of_names bara innehåller namnen på
# de personer som finns i listan "personer".
list_of_names = personer


# Övning: Den här funktionen ska kunna hämta ut en specifik person från listan personer
# och returnera en lista med den personens information (namn, ålder och längd).
# Komplettera nedanstående kod så att man får ut en lista med en persons
# information istället för en lista om alla personer eller en tuple om bara en person.
def personal_info(lista, vem):
    info = lista
    vem
    return info


def main():

    print("Om du ser den här texten när du kör programmet från ÖvningExtra-02"
          " har något gått snett.")

    # Övning: Skriv färdigt den här loopen så att det skrivs ut hela meningar
    # med namn, ålder och längd om varje person.
    for p in personer:
        print("är""år gammal""cm lång.")

    # Övning: Skriv färdigt den här loopen så att vi får ut en lista över namnen på
    # de som är äldre än 30år i den print() som kommer efter loopen.
    over_30 = []
    #in personer:

    print("De som är över 30 ifrån listan är: ", over_30)

    print("En alfabetisk lista av personers förnamn:", alphabetic_list_of_first_names)
    print("Här ska du se information om Bertil:", personal_info(personer, "Bertil"))


if __name__ == '__main__':
    main()
