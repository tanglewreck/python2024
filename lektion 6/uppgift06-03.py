# Original av: Henrik Tunedal

# Denna övning finns i två varianter:

# uppgift06-03.py har namnen på funktioner och variabler på engelska vilket är
# hur man bör skriva men kanske rör till det för vissa.

# uppgift06-03-sv.py har namnen på funktioner och variabler på svenska vilket
# orsaka problem på vissa datorer och bör undvikas.

# NI BEHÖVER BARA GÖRA EN AV DESSA. De är identiska utöver språket på namnen i
# filen.


# Övning 06-03: Komplettera funktionen evaluate_temperature så att den
# returnerar lämpliga bedömningar, från fall till fall, av
# badtemperaturen som den får som argument. Bedömningen kan t.ex. vara
# "för kallt", "lagom" eller "för varmt".
# Som minst efterfrågas tre bedömningsnivåer, t.ex. de ovan, men ni kan lägga
# till fler om ni vill.

# NOTERA: Det är ENDAST i funktionen evaluate_temperature som ni ska göra ändringar


def evaluate_temperature(degrees_celsius):
    if degrees_celsius < 16:
        return "för kallt"
    elif degrees_celsius >=16 and degrees_celsius < 20:
        return "knappt badbart"
    elif degrees_celsius >= 20 and degrees_celsius < 22:
        return "badbart"
    elif degrees_celsius >= 22 and degrees_celsius < 30:
        return "nice!"
    elif degrees_celsius >= 30 and degrees_celsius < 35:
        return "super nice!"
    elif degrees_celsius >= 35 and degrees_celsius < 40:
        return "svettigt"
    elif degrees_celsius >= 40:
        return "för hett"
    else:
        return "av okänd badvänlighet"


# Allt efter denna rad ska vara oförändrat. Kommentarerna på följande rader
# finns enbart där för att förklara vad som händer.


def main():
    # Följande tre rader slumpar fram fem temperaturer så att vi testar om
    # funktionen klarar av både förutbestämda och slumpade temperaturer.
    from random import choices
    random_temp = choices(range(1, 60), k=5)
    temperatures = [0, 25, 10, 50] + random_temp

    for temperature in temperatures:
        # Här anropar vi vår funktion evaluate_temperature och får
        # tillbaka en bedömning.
        assessment = evaluate_temperature(temperature)

        print("Vid", temperature, "grader anses badvattnet vara", assessment)


# Här anropar vi funktionen main. Namnet är konventionellt för den
# funktion där programmet tar sin början, men man kan egentligen kalla
# den vad man vill.
main()



# Allt efter denna rad ska vara oförändrat. Kommentarerna på följande rader
# finns enbart där för att förklara vad som händer.


def main():
    # Följande tre rader slumpar fram fem temperaturer så att vi testar om
    # funktionen klarar av både förutbestämda och slumpade temperaturer.
    from random import choices
    random_temp = choices(range(1, 60), k=5)
    temperatures = [0, 25, 10, 50] + random_temp

    for temperature in temperatures:
        # Här anropar vi vår funktion evaluate_temperature och får
        # tillbaka en bedömning.
        assessment = evaluate_temperature(temperature)

        print("Vid", temperature, "grader anses badvattnet vara", assessment)


# Här anropar vi funktionen main. Namnet är konventionellt för den
# funktion där programmet tar sin början, men man kan egentligen kalla
# den vad man vill.
main()
