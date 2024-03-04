# Created by: Henrik Tunedal

antal_te = 0
antal_kaffe = 0
antal_rooibos = 0

while dryck := input("Önskad dryck? "):
    if dryck == "te":
        antal_te += 1
    elif dryck == "kaffe":
        antal_kaffe += 1
    elif dryck == "rooibos":
        antal_rooibos += 1

print(antal_te, "personer vill ha te.")
print(antal_kaffe, "personer vill ha kaffe.")
print(antal_rooibos, "personer vill ha rooibos.")
