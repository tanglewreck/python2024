# Comprehensions, ingen svensk term finns, är något man använder för att
# skapa en samling ifrån en eller flera andra samlingar.
#
int1 = 1
int10 = 10

list123 = [1, 2, 3]
liststr = ["ett", "två", "tre"]
listintstr = [1, "två", 3]
listlistintstr = [[1,"ett"], [2, "två"], [3,"tre"]]

tuple123 = (1, 2, 3)
tupleintstr = (1, "två", 3)

dict123 = {1:1, 2:2, 3:3}
dictintstr = {1:"ett", 2:"två", 3:"tre"}

range10 = range(10)


print("Här börjar List Comprehensions")
# List Comprehensions, med if och utan if.
complist = [x for x in listintstr]
comlistif = [x for x in listintstr if type(x) == int]
print("Utan if: ", complist)
print("Med if: ", comlistif)

# Man behöver inte hämta från en lista för att göra en List Comprehension:
complistif2 = [x for x in tupleintstr if type(x) == int]
print("Hämtad från en tuple: ", complistif2)

# Vi kan även skapa en lista av samlingar som hämtas från ett dict:
complistdict = [(x, dictintstr[x]) for x in dictintstr]
print("Från ett dict: ", complistdict)

# Vi kan även hämta från flera olika samlingar och para ihop element:
complist123str = [[x, y] for x in list123 for y in liststr]
print("En sammanslagning av två listor: ", complist123str)

# Vi kan även skapa listor från så kallade generatorer:
complistrange = [x for x in range10]
print("Från en generator (ett rangeobjekt): ", complistrange)



print("\n\nHär börjar Dict Comprehensions")
# Dict Comprehensions är helt enkelt att skapa ett dictionary från en eller
# flera samlingar. Lättast är om vi redan har en samling med element som i sig
# bara består av två element:
compdict = {x: y for x, y in listlistintstr}
print("Från en lista med listor: ", compdict)

# Vill vi koppla samman två samlingar till ett dict använder vi lättast
# något som kallas för zip():
compdictzip = {x : y for x,y in zip(list123, liststr)}
print("Kombination av två olika listor: ", compdictzip)