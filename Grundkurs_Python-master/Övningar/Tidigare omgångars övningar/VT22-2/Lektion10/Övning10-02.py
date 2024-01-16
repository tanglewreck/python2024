# Nu vill vi hämta in variabler från filen exercise.py
# och skapa en ny klass som vi kan skapa objekt att lägga i en ny lista.

# Lägg till något så att vi importerar exercise
import exercise

print("Personerna från listan är:", exercise.alphabetic_list_of_first_names)


# Komplettera koden så att en persons information lagras i ett nytt objekt
# när det skapas.
class Person:
    name = str()
    age = int()
    height = int()

    def __init__(self, pers_tuple):
        self.name


# Komplettera koden så att varje person från personer läggs in i obj_personer:
obj_personer = []
for person in exercise.personer:
    pass


print("Här är alla personerna i listan:")
for person in obj_personer:
    print(person.name, person.age, person.height)