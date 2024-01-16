# Exempel på hur man kan definiera hur man interagerar med objekt

# Detta är ett simplistiskt exempel men i fortsättningskursen går man
# igenom mer i detalj hur man kan använda sig av detta.

# VARNING: Det här kan bli ganska avancerat mot slutet.

class MyObject:

    # Vi definierar vad som händer när man skapar ett nytt objekt från
    # vår klass, vår mall.
    def __init__(self, value):
        self.value = value

    # Vi definierar hur MyObjekt-objekt reagerar när man försöker addera två
    # separata instanser.
    def __add__(self, other):
        return MyObject(self.value + other.value)


# Skapa två nya objekt från mallen MyObject
a = MyObject(23)
b = MyObject(27)

# Vi adderar de två objekten och skapar ett nytt objekt med det nya värdet.
# Eftersom vi inte har förklarat för Python vad som händer när man använder
# print() så måste vi skriva ut ett int-objekt som ligger i vårt MyObject-objekt.
c = a + b
print(c.value)
