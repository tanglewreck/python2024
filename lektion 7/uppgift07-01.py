# Här försöker vi använda funktionen choice från paketet random men
# något är fel med koden. Rätta till så att det fungerar.

import random

my_list = ["Funktionen", "ska", "välja", "en", "av", "dessa", "strängar", "slumpmässigt"]

print("random val från my_list: " + random.choice(my_list))
