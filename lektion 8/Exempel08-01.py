# Exempel på hur man definierar en klass och hur man kan lagra data
# däri, vi hoppar över metoder i detta exempel.

# Vi skapar en klass genom att använda oss av detta mönster:
# Det reserverade ordet "class"
# Namnet på vår klass. Namnet bör börja med stor bokstav och ha en stor bokstav
# i början av varje ord. Bör inte innehålla åäö eller andra tecken som inte
# finns på ett engelskt tangentbord.
# OM vi ska ha ett arv så har man parenteser också, vi går igenom det senare.
# Ett kolon (:) för att visa att nu börjar ett kodblock.



class MyClass:

    # I klassen kan vi lagra variabler.
    my_int = 42
    my_str = "HEJ"
    my_list = [1, 2]


# Om vi vill skapa en INSTANS av klassen skriver vi så här:
my_instance = MyClass()

# Notera att det finns en lista i vår nyskapade instans/vårt objekt.
print("Listan i instansen:", my_instance.my_list)
