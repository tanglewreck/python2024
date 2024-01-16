# Av: Henrik Tunedal
# Övning 06-03: Komplettera funktionen bedöm_badtemperatur så att den
# returnerar lämpliga bedömningar, från fall till fall, av
# badtemperaturen som den får som argument. Bedömningen kan t.ex. vara
# "för kallt", "lagom" eller "för varmt".


def bedöm_badtemperatur(antal_grader_celsius):
    return "av okänd badvänlighet"


def main():
    for temperatur in [0, 25, 10, 50]:
        # Här anropar vi vår funktion bedöm_badtemperatur och får
        # tillbaka en bedömning.
        bedömning = bedöm_badtemperatur(temperatur)

        print("Vid", temperatur, "grader anses badvattnet vara", bedömning)


# Här anropar vi funktionen main. Namnet är konventionellt för den
# funktion där programmet tar sin början, men man kan egentligen kalla
# den vad man vill.
main()
