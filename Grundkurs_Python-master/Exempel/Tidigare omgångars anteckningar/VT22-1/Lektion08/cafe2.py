produkter = ["kaffe", "te", "öl"]
priser = [20, 15, 50]
slutsålt = [False, False, True]


def produktpris(produkt):
    index = 0
    for p in produkter:
        if p == produkt:
            return priser[index]
        else:
            index += 1


def produkt_slutsåld(produkt):
    index = 0
    for p in produkter:
        if p == produkt:
            return slutsålt[index]
        else:
            index += 1


def main():
    produkt = input("Vad vill du beställa? ")

    if produkt_slutsåld(produkt):
        print("Tyvärr har vi sålt slut på " + produkt + ".")
    else:
        pris = produktpris(produkt)
        print("Varsågod, här är ditt " + produkt + ".")
        print("Det blir", pris, "kr, tack.")


if __name__ == "__main__":
    main()
