# Exempel på hur man kan importera funktioner från andra
# moduler och hur man refererar till dem i koden.

import tobeimported_live

tobeimported_live.my_function()

print(__name__)
print(tobeimported_live.__name__)


if __name__ == "__main__":
    print("Exempel är main")
