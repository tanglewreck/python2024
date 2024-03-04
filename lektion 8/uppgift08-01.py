# Lägg till fler attribut till Animal som kan ärvas av andra klasser.
# Förslag: Ålder, vikt, etc.

# Lägg även till en ny klass av något annat djur som inte har fyra ben.

# Pröva också att skapa en instans av djuret i main() och lägg in det
# i listan animals.

class Animal:
    sound = "Jag låter som alla andra djur."
    number_of_legs = 4

    def speak(self):
        print(self.sound, end=" ")


class Dog(Animal):
    sound = "Woof!"

    def __init__(self, name, legs=4):
        self.name = name
        self.number_of_legs = legs


class Cat(Animal):

    def __init__(self, name, prickig):
        self.name = name
        self.prickig = prickig


def main():
    fido = Dog("Fido")
    pelle = Cat("Pelle", True)
    animals = [fido, pelle]
    for a in animals:
        a.speak()
        print("Jag har", a.number_of_legs, "ben.")


main()
