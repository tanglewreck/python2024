# Original av Henrik Tunedal
# Ett exempel av ett program för ett kafé, utan samlingar.

kaffepris = 20
tepris = 15
ölpris = 50

kaffe_slutsålt = False
te_slutsålt = False
öl_slutsålt = True


def produktpris(produkt):
    if produkt == "kaffe":
        return kaffepris
    elif produkt == "te":
        return tepris
    elif produkt == "öl":
        return ölpris


def produkt_slutsåld(produkt):
    if produkt == "kaffe":
        return kaffe_slutsålt
    elif produkt == "te":
        return te_slutsålt
    elif produkt == "öl":
        return öl_slutsålt


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
