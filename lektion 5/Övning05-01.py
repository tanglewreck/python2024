# Vänd på listan med hjälp av en metod så att vi får ut rätt svar från
# den print() som finns på sista raden.
# Raden där listan skapas ska vara oförändrad och likaså den sista raden.

# En lista på de metoder som finns för listor finns här:
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
en_lista = ["Det", "här", "är", "en", "lista."]
en_annan_list = list( ("Det", "här", "är", "en", "annan", "lista.") )
en_tredje_list = list(en_lista)

# Ovanstående rad ska vara oförändrad.

en_lista.reverse()



# Nästa rad ska vara oförändrad.
print("Här ska det stå ['lista.', 'en', 'är', 'här', 'Det']:", en_lista)

print(en_annan_list)
print(en_tredje_list)
print(en_lista.count("är"))