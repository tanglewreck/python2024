# Exempel04-03 fast med både en while och en for-loop.
# Ibland kan använda den typ av loop man föredrar.

my_int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for element in my_int_list:
    print(element)

print()
i = 0
while i <len(my_int_list):
    element = my_int_list[i]
    i += 1
    print(element)
