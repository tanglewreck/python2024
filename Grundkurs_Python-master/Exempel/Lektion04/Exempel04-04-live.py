# Exempel som visar hur For-loopar fungerar och kan användas.

my_int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
summa_av_int = 0

for element in my_int_list:
    summa_av_int = summa_av_int + element # Kan även skrivas summa_av_int += element
    print(element)
    print(summa_av_int)
    print()

print()
# Vi kollar genomsnittet på my_int_list:
print(len(my_int_list))
print("Genomsnittet är:", summa_av_int / len(my_int_list))
