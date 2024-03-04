# Exempel på hur man kan definiera hur varje objekt som skapas från en klass
# ska se ut. Även exempel på instansvariabler och hur man definierar metoder.

class MyClass:
    my_int = 42
    my_str = "HEJ!"
    my_list = [1, 2]

    # När vi ska skapa en ny instans/ett nytt objekt av en klass så anropas
    # automatiskt metoden __init__.
    # __init__ är en så kallad konstruktor.
    # Notera att eftersom __init__ är en metod så måste första argumentet vara self.
    def __init__(self):
        self.my_instance_list = ["Jag ligger i en instans."]

my_instance = MyClass()
my_second_instance = MyClass()
print("Listan i klassen:", MyClass.my_list)
print("Listan i första instansen:", my_instance.my_list)
print("Listan i andra instansen:", my_second_instance.my_list)
print()

# Nästa rad kommer att krascha programmet så efter att vi bekräftat det så
# kommenterar vi bort den.
#print("Det finns ingen inre lista i klassen:", MyClass.my_instance_list)
print("Inre listan i första instansen:", my_instance.my_instance_list)
print("Inre listan i andra instansen:", my_second_instance.my_instance_list)
print()

my_instance.my_instance_list.append("Jag ska hamna i den första instansens lista!")
print("Inre listan i första instansen:", my_instance.my_instance_list)
print("Inre listan i andra instansen:", my_second_instance.my_instance_list)
