#!/usr/bin/env python3

# Rätta till While-loopen så att den fungerar och skriver ut rader enligt
# mönstret nedan när programmet körs:
# 27
# 34
# 41
# etc.

my_first_int = 20
my_second_int = 300
# Ovanstående kod ska inte ändras på.
mysequence = [x for x in range(20,300,7)]

while my_first_int < my_second_int:
    my_first_int = my_first_int + 7
    print(my_first_int)

