# Ändra koden nedan så att bara det element som innehåller "är" skrivs ut.
# Skapandet av listan ska INTE ändras på och att skriva in "är"
# manuellt i print() är inte rätt.

en_lista = ["Det", "här", "är", "en", "lista."]
# Ovanstående rad ska INTE ändras på

print(en_lista[2])
# en_lista.pop()
# en_lista.pop()
# en_lista = list( (en_lista[2]) )
en_lista = [en_lista[en_lista.index("är")],]
en_lista = en_lista[en_lista.index("är")]
print('Här ska det stå "är" utan citattecken:', en_lista)