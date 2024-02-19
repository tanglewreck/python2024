# Lägg till en IF-sats så att greeting inte ändras så länge
# we_want_to_mess_with_greeting är False.

# Uppgiften är att använda en if-sats och att ta bort en av definitionerna
# helt är inte rätt svar.

we_want_to_mess_with_greeting = False
we_want_to_mess_with_greeting = True

greeting = "Hej och tack! Jag blev inte borttagen!"

if (we_want_to_mess_with_greeting):
    greeting = "Ånej! Jag blev ändrad!"

print(greeting)


