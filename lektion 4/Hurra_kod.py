print("Välkommen")
namn = input("Vad heter du? ")

if namn == "hemligt":
    print("Din integritet är viktig för oss. Ha en bra dag.")
else:
    print("Ett fyrfaldigt leve för " + namn +"!")
    for i in range(4):
        print("Hurra!")
