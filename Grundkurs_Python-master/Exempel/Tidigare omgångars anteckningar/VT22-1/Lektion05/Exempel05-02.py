# Exempel som visar hur While-loopar fungerar och kan användas.

my_int = 1
my_second_int = 10

while my_int < my_second_int:
    if my_int % 2 == 0:
        print(my_int)
        # "Råka" lägga in my_int = my_int +1 här.
    else:
        print("Här är ett udda tal!")
    my_int = my_int + 1
print("Nu är loopen över!")
