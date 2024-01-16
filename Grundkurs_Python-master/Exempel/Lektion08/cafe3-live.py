# Orignal av: Henrik Tunedal
# Ett exempel av ett program för ett cafe, med dicts.


def main():
    beställning = input("Vad vill du beställa? ")

    if produkt_slutsåld(beställning):
        print("Tyvärr har vi sålt slut på " + beställning + ".")
    else:
        pris = produktpris(beställning)
        print("Varsågod, här är ditt " + beställning + ".")
        print("Det blir", pris, "kr, tack.")


if __name__ == "__main__":
    main()
