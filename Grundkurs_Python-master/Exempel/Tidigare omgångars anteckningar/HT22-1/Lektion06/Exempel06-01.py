# Funktioner (också kallade procedurer eller subrutiner) används
# för att separera och namnge en del av programmet, som ett eget
# litet miniprogram, så att man kan återanvända den.
#
# I det här exemplet skriver vi en simpel funktion som skriver
# ut en hälsning på skärmen.
def hello_world():
    print("Hello World")


# Man kan också ge funktionen data som den behöver, i form av
# s.k. argument, som då inte behöver delas i hela programmet.
#
# I det här exemplet accepterar vår funktion ett argument, ett namn,
# som vi vill att programmet ska hälsa på.
def hello(name):
    print("Hej ", name, "!", sep="")


# Funktioner kan också ge värden tillbaka, vilket man kallar
# att returnera ett värde. De liknar på det sättet funktioner
# inom matematiken.
#
# I det här exemplet returnerar vi argumentet upphöjt till två,
# d.v.s. kvadraten.
def f(x):
    return x ** 2


hello_world()
hello("Johan")
