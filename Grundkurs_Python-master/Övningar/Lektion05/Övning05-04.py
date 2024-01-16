# Denna övning finns även i en variant med mycket mindre text och har siffror i listorna istället
# för strängar. Den filen heter "Övning05-04-siffror.py".

# Lägg till listan my_first_list till listan som ligger i my_second_list genom
# att använda er av vad vi gått igenom på Lektion05.
# my_first_list ska ligga efter den str som ligger där i.

# Att flytta listan manuellt är inte rätt svar, övningen handlar om att
# ändra på samlingar genom att skriva kod.
# Använd helst metoder istället för att skapa en ny lista.

# Resultatet som ska skrivas ut är (ert resultat kommer inte ha radbyten på samma
# ställen, det är inte viktigt):
# ['Det här är den yttre listan!',
# ['Efter den här strängen ska my_first_list läggas till.', ['Listor kan ligga i listor.',
# ['Man kan till och med ha listor i listor som ligger i listor', ['Spännande, va?']]]],
# 'Nästlade listor kan vara krångliga ibland.']

# OBS!
# OBS! Notera exakt var parenteserna ligger i det förväntade resultatet. OBS!
# OBS!

my_first_list = ["Listor kan ligga i listor.", ["Man kan till och med ha listor i listor som ligger i listor",
                                                ["Spännande, va?"]]]

my_second_list = ["Det här är den yttre listan!", ["Efter den här strängen ska my_first_list läggas till."],
                  "Nästlade listor kan vara krångliga ibland."]
# Ovanstående rader ska INTE ändras.


print(my_second_list)
