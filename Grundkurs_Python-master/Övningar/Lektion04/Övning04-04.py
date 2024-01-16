# Här försöker vi hämta alla element i en lista och lägga till dem i en ny lista.
# När vi lägger till varje element i listan kollar vi om det är en integer eller
# float och om så är fallet vill vi addera 5 till det elementet.
# Se övning04-03 för ledtrådar.

# Sista raden ska INTE ändras på och när programmet körs så ska vi få ut:
# [6, 7, 8, 9, 10, 'Här', 'är', 'några', 'strängar!', 11, 12, ['En', 'lista', 'i', 'listan!'], 13, 14]

my_mixed_list = [1, 2, 3, 4, 5, "Här", "är", "några", "strängar!", 6, 7,
                 ["En", "lista", "i", "listan!"], 8, 9]
my_new_list = []
# Ovanstående kod ska inte ändras på.


for element in my_mixed_list:
    # Nedanstående rad skulle kunna kunna skrivas "if type(element) == int or type(element) == float:"
    if type(element) in {int, float}:
    my_new_list.a
    else:
    my_new_list.a

print(my_new_list)
