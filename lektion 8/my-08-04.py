class Animal:
    sound = "foo"
    noOfLegs = 2
    def speak(self):
        print(self.sound)
  
class Cat(Animal):
    sound = "mjau"
    def __init__(self,  name, age, noOfLegs = 4, colour = "svart", spotty = False):
        self.name = name
        self.noOfLegs = noOfLegs
        self.colour = colour
        self.age = age
        self.spotty = spotty

myCat = Cat(name = "Issa", age = 8, colour = "röd", spotty = False)
print(myCat.name, myCat.noOfLegs, myCat.sound, myCat.colour)
myCat.speak
