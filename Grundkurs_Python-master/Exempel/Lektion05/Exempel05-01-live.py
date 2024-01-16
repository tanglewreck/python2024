# Demonstration av slicing på listor och strängar
# Tuples fungerar för detta syfte precis som listor.

my_fruit_list = ["Päron", "Äpplen", "Apelsiner", "Citroner", "Vindruvor"]

# Skriv ut hela listan
print(my_fruit_list)

# Hämta och skriv ut det första elementet
print(my_fruit_list[0])

# Hämta och skriv ut, som en lista, de tre första elementen ur my_fruit_list
# på två olika sätt.
print(my_fruit_list[0:3])
print(my_fruit_list[:3])

# Hämta och skriv ut, som en lista, de tre elementen i mitten.
print(my_fruit_list[1:4])

# Hämta och skriv ut, som en lista, de tre sista elementen ur my_fruit_list
# på tre olika sätt. Plus en bonus.
print(my_fruit_list[2:5])
print(my_fruit_list[2:])
print(my_fruit_list[-3:])
print(my_fruit_list[len(my_fruit_list)-3:])


#Slicing fungerar även på strängar.
print("123456789"[0:5])

# När man hämtar från en dict så använder man samma syntax för att hämta ett
# element
johan = {"namn":"Johan", "ålder":34, "längd":180}
print(johan["ålder"])
