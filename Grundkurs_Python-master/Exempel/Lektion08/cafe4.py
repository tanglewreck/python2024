# Ett exempel där vi skapar en klass för dryck och sen skapar instanser
# av objektet.
# Av: Henrik Tunedal


class Dryck:
    def __init__(self, namn, pris, slutsålt=False):
        self.namn = namn
        self.pris = pris
        self.slutsålt = slutsålt


class Lager:
    def __init__(self):
        self.produkter = {}

    def registrera_produkt(self, produkt):
        namn = produkt.namn
        self.produkter[namn] = produkt

    def produktpris(self, namn):
        produkt = self.produkter[namn]
        return produkt.pris

    def produkt_slutsåld(self, namn):
        produkt = self.produkter[namn]
        return produkt.slutsålt


lager = Lager()
lager.registrera_produkt(Dryck("kaffe", 20))
lager.registrera_produkt(Dryck("te", 15))
lager.registrera_produkt(Dryck("öl", 50, slutsålt=True))
lager.registrera_produkt(Dryck("finöl", 70))


def produktpris(produktnamn):
    return lager.produktpris(produktnamn)


def produkt_slutsåld(produktnamn):
    return lager.produkt_slutsåld(produktnamn)


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
