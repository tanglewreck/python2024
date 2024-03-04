class AdditionObject:
    def __init__(self, thisvalue):
        self.value = thisvalue

    def __add__(self, that):
        return(self.value + that.value)

a = AdditionObject(10)
b = AdditionObject(20)

print(a + b)
