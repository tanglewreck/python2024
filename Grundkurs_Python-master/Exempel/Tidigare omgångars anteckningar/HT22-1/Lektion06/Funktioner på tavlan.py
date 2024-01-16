def hello_world():
    print("Hello World")

def hello(name):
    print("Hej, ", name, "!", sep="")

hello("Johan")

def squared(x):
    print(x ** 2)

squared(3)

for number in range(5):
    if number == 3:
        squared(number)
    else:
        squared(number+3)
