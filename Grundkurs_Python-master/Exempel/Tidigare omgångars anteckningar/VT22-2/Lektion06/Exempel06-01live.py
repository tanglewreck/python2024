# Funktioner (också kallade procedurer eller subrutiner) används
# för att separera och namnge en del av programmet, som ett eget
# litet miniprogram, så att man kan återanvända den.

# En simpel funktion som skriver ut en hälsning på skärmen.

def hello_world():
    print("Hello World!")

# Man kan också ge funktioner data som den behöver, i form av
# s.k. argument, som inte behöver delas i hela programmet.

# I det här exemplet accepterar vår funktion ett argument, ett namn,
# som vi vill att programmet ska hälsa på.

def hello(name):
    print("Hej ", name, "!", sep="")


# Funktioner kan också ge värden tillbaka, vilket man kallar
# att returnera ett värde. De liknar på det sättet funktioner
# inom matematiken.

def f(x):
    return x * 2


print(f(2))
hello("Johan")
hello("Pelle")
hello_world()
