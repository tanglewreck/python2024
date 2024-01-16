# Ett simpelt exempel av arv.


class Animal:
    sound = "Jag låter som alla andra djur."

    def speak(self):
        print(self.sound)


class Dog(Animal):
    sound = "Woof!"


class Cat(Animal):
    pass


def main():
    animals = [Dog(), Cat()]
    for a in animals:
        a.speak()


main()
