höjd = 3

while höjd > 0:
    print("Din fågel flyger på", höjd, "meters höjd.")

    kommando = input("Vad ska fågeln göra: flaxa eller slöa? ")
    print()

    if kommando == "flaxa":
        print("Åååå hej!")
        höjd = höjd + 1
    elif kommando == "slöa":
        höjd = höjd - 1
    else:
        print("Va?")

print("Duns! Aj! Din fågel har trillat ner på marken.")
print("Game over.")
