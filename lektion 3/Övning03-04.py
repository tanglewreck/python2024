# Skriv färdigt programmet så att det skriver ut namnet på den månad som
# representeras av den inskrivna siffran.
# Programmet ska också säga åt användaren an skriva in ett giltigt tal
# nästa gång OM användaren skriver in något som är utanför önskat
# spann på 1 till 12.

month = int(input("Skriv in en siffra mellan 1 och 12: "))
if month == 1:
    print("Januari")
elif month == 2:
    print("Februari")
elif month == 3:
    print("Mars")
elif month == 4:
    print("April")
elif month == 5:
    print("Maj")
elif month == 6:
    print("Juni")
elif month == 7:
    print("Juli")
elif month == 8:
    print("Augusti")
elif month == 9:
    print("September")
elif month == 10:
    print("Oktober")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Vänligen skriv in en giltig siffra nästa gång.")