#!/usr/bin/env python3

# Rätta till koden så att vi:
# 1. Skapar en funktion som skriver ut vad användaren skriver in.
# 2. Kör den skapade funktionen.

def my_func(userinput="foo"):
    myinput = input("Vad vill du att jag ska säga? ")
    if not myinput:
        myinput = userinput
    print("Jag blev ombedd att säga: ", myinput)


my_func()
