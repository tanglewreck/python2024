# Övning 07-02: Lägg till en modul för kattläten och anropa den
# från det här programmets main-funktion.

from exempelpaket.animals.mammals.dogs import bark, bark_loudly


def main():
    bark()
    bark_loudly()


main()
