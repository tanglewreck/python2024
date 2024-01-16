# Den här koden kör oändligt.
# Rätta till den så att det inte längre händer.

# MEN programmets funktionalitet ska inte ändras!
# D.v.s. loopen ska vara kvar och raden "while my_int < amount:" ska INTE ändras.

def print_and_increment(my_inner_int):
    print(my_inner_int)
    return my_inner_int + 1


amount = int(input("Hur många gånger ska jag köra? "))
my_int = 0
while my_int < amount:
    print_and_increment(my_int)
