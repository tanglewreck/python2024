# Här försöker vi hämta alla element i en lista, lägga till 5 om
# elementet i listan är en integer eller float och sen skapa en ny lista.

my_mixed_list = [1, 2, 3, 4, 5, "Här", "är", "några", "strängar!", 6, 7,
                 ["En", "lista", "i", "listan!"], 8, 9]
my_int_list = [1,2,3,4,5,6,7,8]
my_new_list = []

for element in my_mixed_list:
    # Nedanstående rad skulle kunna kunna skrivas "if type(element) == int or type(element) == float:"
    if type(element) in {int, float}:
    my_new_list.a
    else:
    my_new_list.a

print(my_new_list)
