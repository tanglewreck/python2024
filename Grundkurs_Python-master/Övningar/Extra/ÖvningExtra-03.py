# Övning: Nu vill vi hämta in variabler och en funktion från filen
# extra_exercises.py och från listan personer skapa en dict där varje person
# är ett element med sitt namn som nyckeln och en lista för ålder och längd
# som värde.
# T.ex. "Anna Andersson":[23, 172]

# VARNING: Svår!

# Övning: Lägg till något så att vi importerar "extra_exercises" men kallar
# modulen för "exercise" i denna namnrymd.
import extra_exercises

print("Personerna från listan är:", exercise.alphabetic_list_of_first_names)


# Raden nedan är början på ett av de möjliga sätt att lösa uppgiften men
# använder något som kallas för comprehensions. Vi har bara
# nämnt det i förbifarten så ni kan behöva en ledtråd, titta på exemplet
# Comprehensions.py som ligger i SubjectExamples eller kolla lite
# online.
dict_personer = {for person in exercise.personer}

print(dict_personer)
