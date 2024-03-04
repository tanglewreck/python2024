# Exempel på kodblock. Notera att koden är helt poänglös och dessutom
# extremt otydligt skriven; denna fil är enbart
# för att användas som exempel vid en förklaring om nivåer av kodblock.

shall_we_demonstrate_code_blocks = True
is_program_running = True
list_to_iterate_over = [1, 2, "HI!", True, ["Let's add a list!"]]
list_to_transfer_to = []

if shall_we_demonstrate_code_blocks == True:
    print("It has already been decided that we shall demonstrate code blocks!")
    while is_program_running == True:
        is_it_time_to_demonstrate = input("Is it time to demonstrate now? Yes or No: ").lower()
        if is_it_time_to_demonstrate == "yes":
            print("I see! It's time to demonstrate! Then we shall transfer data!")
            for x in list_to_iterate_over:
                list_to_transfer_to.append(x)
                print("Added this:", x)
            print("We have copied the data from one list to another!")
            print("This is the new list:", list_to_transfer_to)
            shall_we_keep_the_data = input(
                "Shall we keep the data? Yes or No: ").lower()
            while shall_we_keep_the_data not in ["yes", "no"]:
                shall_we_keep_the_data = input(
                    "Hey! I asked for Yes or No! Try again! ")
            if shall_we_keep_the_data == "no":
                print("Okay! Resetting list_to_transfer_to!")
                list_to_transfer_to.clear()
                print("Data erased! This is the list now", list_to_transfer_to, end="\n\n")
            elif shall_we_keep_the_data == "yes":
                print("Okay! This is the list now:", list_to_transfer_to, end="\n\n")
        elif is_it_time_to_demonstrate == "no":
            print("Oh. I see...", end="\n\n")
            print("Well, we can't continue until it is time to demonstrate.")
            print("Let's check again!", end="\n\n")
        else:
            print("Hey! I asked for Yes or No! Try again!")
            print("Or did you want to stop?")
            want_to_stop = input("Yes or No: ").lower()
            if want_to_stop not in ["yes", "no"]:
                print("Well, if you won't give a proper answer we will continue!")
            elif want_to_stop in "yes":
                print("Alright, I'll BREAK the loop for you.")
                break
            elif want_to_stop in "no":
                print("Alright")



