# Här skriver vi två olika matematiska funktioner.
# I ordning så gör de addition respektive multiplikation
# av två argument som man anger när man kör funktionen.

# Uppgiften är att utöka den här filen så att den hanterar fler räknesätt
# eller operatorer.
# Lägg till minst två nya funktioner, helst några fler. Max fem nya.
# Om du inte vet vad du ska välja för räknesätt så är förslagen
# subtraktion (d.v.s. minus) och division (d.v.s. delat med).

# Länk till exempel på operatorer ( Endast de som är markerade med fet stil
# är relevanta för grundkursen:
# https://misaab-my.sharepoint.com/:w:/g/personal/johan_marmen_misa_se/ESehIlchRdpFoetFBbWIeSwBx3dZnTMy0XUxAA9_GJLpxA?e=2eE3tf


# Lägg även till anrop på dina nya funktioner så som jag gör längst ned i denna fil.


def add(int1, int2):
    print(str(int1), "+", str(int2), "=", int1 + int2)

def subtract(int1, int2):
    print(str(int1), "-", str(int2), "=", int1 - int2)


def multiply(int1, int2):
    print(str(int1), "x", str(int2), "=", int1 * int2)

def divide(float1, float2):
    if float2 == 0:
        print("cannot divide by zero")
        return 0
    try:
        print(str(float1), "/", str(float2), "=", float1 / float2)
    except:
        print("divide by zero")

def main():
    while True:
        try:
            number1 = int(input("n1? "))
        except:
            print("please input a number")
        try:
            number2 = int(input("n2? "))
        except:
            print("please input a number")
        add(number1, number2)
        subtract(number1, number2)
        multiply(number1, number2)
        divide(number1, number2)

main()