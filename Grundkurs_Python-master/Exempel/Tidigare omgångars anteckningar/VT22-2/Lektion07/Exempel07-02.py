# Första gången vi importerar om modul i vårt program laddas
# den från disk och koden i modulen körs.
print("Importerar modulen tobeimported...")
import tobeimported
print("Importerad modul:", tobeimported)

# Observera att koden i tobeimported inte körs andra gången,
# eftersom vi redan har laddat den tidigare.
print("Importerar samma modul igen!")
import tobeimported
print("Fortfarande samma modul:", tobeimported)
