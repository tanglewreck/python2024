# Exempel som demonstrerar att olika namn kan användas i olika
# sammanhang (i det här fallet olika funktioner) för att referera till
# ett och samma objekt (i det här fallet en lista).


def lägg_till_ingredienser(bunke):
    bunke.append("ägg")
    bunke.append("mjölk")


def lägg_till_verktyg(verktygslåda):
    verktygslåda.append("hammare")
    verktygslåda.append("såg")


def main():
    allmänlåda = []
    lägg_till_ingredienser(allmänlåda)
    lägg_till_verktyg(allmänlåda)
    print(allmänlåda)


if __name__ == "__main__":
    main()
