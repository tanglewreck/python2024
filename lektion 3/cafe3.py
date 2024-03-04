# Orignal av: Henrik Tunedal
# Ett exempel av ett program för ett cafe, med dicts.

priser = {"kaffe": 20, "te": 15, "öl": 50}

slutsålt = {"öl"}


def produktpris(produkt):
    return priser[produkt]


def produkt_slutsåld(produkt):
    return produkt in slutsålt


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
