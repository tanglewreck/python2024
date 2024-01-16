# Den här koden kör oändligt. Rätta till så att den inte gör det.

def print_and_increment(my_inner_int):
    print(my_inner_int)
    return my_inner_int + 1


amount = int(input("Hur många gånger ska jag köra? "))
my_int = 0
while my_int < amount:
    print_and_increment(my_int)

