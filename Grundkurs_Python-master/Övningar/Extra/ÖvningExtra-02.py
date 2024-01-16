# Nu vill vi hämta in variabler från filen extra_exercises.py
# och definiera en ny klass som vi kan skapa objekt ifrån och lägga i de skapade
# objekten i en lista.


# Övning: Lägg till något så att vi importerar "extra_exercises" men kallar
# modulen för "exercise" i denna namnrymd.
import extra_exercises

print("Personerna från listan är:", exercise.alphabetic_list_of_first_names)


# Övning: Komplettera klassen nedan så att en persons information lagras i ett
# nytt objekt när det skapas.
class Person:
    name = str()
    age = int()
    height = int()

    def __init__(self, pers_tuple):
        self.name


# Övning: Komplettera koden nedan så att varje person från personer läggs in
# i obj_personer:
obj_personer = []
for person in exercise.personer:
    pass


print("Här är alla personerna i listan:")
for person in obj_personer:
    print(person.name, person.age, person.height)