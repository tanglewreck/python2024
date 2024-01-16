# Henriks exempel från lektion02

height = 3

while height > 0:
    print("Din fågel flyger på", height, "meters höjd.")

    command = input("Vad ska fågeln göra: flaxa eller slöa? ")
    print()

    if command == "flaxa":
        print("Åååå hej!")
        height = height + 1
    elif command == "slöa":
        height = height - 1
    else:
        print("Va?")

print("Duns! Aj! Din fågel har trillat ner på marken.")
print("Game over.")
