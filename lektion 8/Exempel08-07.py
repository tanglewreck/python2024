class MyObject:
    

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if type(self.value) == type(other.value):
            return MyObject(self.value + other.value)
        else:
            return "Ogiltig operation"

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)

    


a = MyObject(2)
b = MyObject(2)
d = a


c = a + b
print(a==b)
print(a==d)
print(c)
print(str(c))
print(str(c)+"Hej")
