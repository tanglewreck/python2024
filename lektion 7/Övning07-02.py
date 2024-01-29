# Övning 07-02: Skapa en modul med funktioner för kattläten
# och lägg till anrop på den nya modulens funktioner i den här
# modulens main-funktion.

# from exempelpaket import animals
from dogs import bark, barkloudly
from cats import mjau, mjauloudly

def main():
    bark()
    barkloudly()
    mjau()
    mjauloudly()

main()
