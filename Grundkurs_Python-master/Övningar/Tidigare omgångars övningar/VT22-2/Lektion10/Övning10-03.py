# Nu vill vi hämta in variabler och en funktion från filen exercise.py
# och från listan personer skapa en dict där varje person är ett
# element med sitt namn som nyckeln och en lista för ålder och längd som värde.
# T.ex. "Anna Andersson":(23, 172)

# VARNING: Svår!

# Lägg till något så att vi importerar exercise
import exercise

print("Personerna från listan är:", exercise.alphabetic_list_of_first_names)


# Raden nedan är början på ett sätt att lösa uppgiften men
# använder något som kallas för comprehensions, vi har bara
# nämnt det i förbifarten så ni kan behöva en ledtråd eller kolla lite
# online.
dict_personer = {for person in exercise.personer}

print(dict_personer)
