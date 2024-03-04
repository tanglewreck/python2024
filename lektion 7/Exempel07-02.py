# Första gången vi importerar en modul i vårt program laddas
# den från disk och koden i modulen körs.
print("Importerar modulen tobeimported...")
import tobeimported
print("Importerad modul:", tobeimported)

# Observera att koden i tobeimported inte körs andra gången,
# om vi importerar modulen igen eftersom vi har laddat den
# tidigare.
print()
print("Importerar samma modul igen!")
import tobeimported
print("Fortfarande samma modul:", tobeimported)
