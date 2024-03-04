# Exempel som visar hur man kan läsa ut data ur en samling, behandla
# datan och sen lagra i en annan samling.

my_int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_squared_list = []

for number in my_int_list:
    print(number)
    square = number * number
    print(square)
    my_squared_list.append(square)
    print(my_squared_list)
