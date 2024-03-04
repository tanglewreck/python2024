run = True

while run:
    namn = input("Hej, vad heter du? ")
    if namn == "quit":
        run = False
    else:
        print("Hej, ", namn, "!")
    

while True:
    namn = input("NAMN?")
    if namn == "quit":
        break
    else:
        print("Hej, ", namn)
