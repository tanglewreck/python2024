# Här skriver vi fyra olika matematiska funktioner.
# I ordning så gör de: addition, subtraktion, multiplikation, division
# av två argument som man anger när man kör/kallar på funktionen.

def add(int1, int2):
    print(int1 + int2)


def subtract(int1, int2):
    print(int1- int2)


def multiply(int1, int2):
    print(int1 * int2)


def divide(int1, int2):
    print(int1 / int2)


def squared(x):
    print(x ** 2)



#add(3, 2)
#subtract(3, 2)
#multiply(3, 2)
#divide(3, 2)
#squared(3)

for number in range(5):
    if number == 3:
        squared(number)
    else:
        squared(number+3)

