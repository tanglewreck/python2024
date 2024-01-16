class MyObject:

    def __init__(self, value):
        self.value = value

    def __add__(self, otherMyObject):
        if type(otherMyObject) == int:
            return MyObject(self.value + otherMyObject)
        else:
            return MyObject(self.value + otherMyObject.value)

a = MyObject(23)
b = 27

c = a + b
print(c.value)
