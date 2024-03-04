# Exempel på hur man kan importera funktioner från andra moduler
# och hur man refererar till dem i koden.

import tobeimported

tobeimported.my_function()
print(__name__)
print(tobeimported.__name__)


if __name__ == '__main__':
    print("Exempel är main")
