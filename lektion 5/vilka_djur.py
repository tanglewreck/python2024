pet_store_inventory = ["Katt", "Hund", "Hamster", "Fisk"]

print("Butikens utbud är:", pet_store_inventory)
desired_animal = input("Vilket djur vill du köpa? ")

if desired_animal in pet_store_inventory:
    print("Grattis!", desired_animal, "finns i butiken!")
    want_to_purchase = input("Vill du köpa djuret? Ja eller Nej? ")

    if want_to_purchase == "Ja":
        print("Du har nu köpt önskat djur:", desired_animal)
        pet_store_inventory.remove(desired_animal)
        print("Butikens utbud är nu:", pet_store_inventory)
    else:
        print("Okej, välkommen åter!")
        print("Butikens utbud är fortfarande:", pet_store_inventory)

else:
    print("Tyvärr!", desired_animal, "är inte tillgängligt just nu.")
