# Här definierar vi saker som vi kan hämta från andra moduler.

def my_function():
    print("Jag kommer från en annan modul!")


# För att tydliggöra hur importfinessen fungerar visar vi ett meddelande
# här, vilket man i vanliga fall inte skulle göra i en modul som är
# tänkt att importeras.
print("Den här strängen ligger i tobeimported")

if __name__ == "__main__":
    print("tobeimported är main")
