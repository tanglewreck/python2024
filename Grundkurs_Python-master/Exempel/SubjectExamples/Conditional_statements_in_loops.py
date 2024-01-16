# Det finns, utan att gå in i mer avancerade metoder, några olika sätt att ha
# conditional statements (villkorssatser på svenska) i loopar.


int1 = 1
int10 = 10
list123 = [1, 2, 3]
listintstr = [1, "två", 3]

# if-sats i loopen:
x = int1
while x < int10:
    userinput = input("Ska vi höja eller sänka värdet på x? Lämna tomt för"
                      " att avbryta programmet. >>>")
    if userinput.lower() in {"h", "hö", "höj", "höja"}:
        x += 1
    elif userinput == "":
        break
    elif userinput.lower() in {"s", "sä", "sän", "sänk"}:
        x -= 1
    else:
        print("Ogiltigt svar, vänlig skriv in vad som efterfrågas.")
    print("Nuvarande värdet på x är", x, "\nOm x når 10 så är vi färdiga.")
print("'If-satser i loopar'-exemplet är nu slut.\n\n")


# while-loopar som har flera krav som måste uppfyllas för att något ska ske:
forbidden_number = 4
x = int1
special_exception = input("Ska vi tillåta det förbjudna numret? Ja eller Nej: ")
while ((x < int10 and (x != forbidden_number or special_exception.lower() == "ja"))
        and special_exception != ""):
    print(x)
    x += 1
print("'While-loopar med vilkorssatser'-exemplet är nu slut.\n\n")

# Comprehensions, i detta exemplet List Comprehensions. Det finns ingen svensk
# term för detta, Listförståelse är en bokstavlig översättning men är inget som
# någon använder.
# Se exempel "Comprehensions.py" för fler exempel på detta.

listcomp = [x for x in listintstr if type(x) == int]
print("Vår nya lista med bara siffror:", listcomp)