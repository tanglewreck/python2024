# Exempel på hur for-loopar fungerar och kan användas.

my_str_list = ["Från", "den", "här", "listan", "kan", "vi", "hämta", "text!"]
my_int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


for element in my_str_list:
    print(element)
print("Vi kan fortfarande läsa element utanför loopen:", element)

print()
for element in my_int_list:
    print(element)
