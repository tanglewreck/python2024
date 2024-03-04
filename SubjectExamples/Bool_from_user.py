jag_vill_ha_en_bool = input("True eller False? ")
print(jag_vill_ha_en_bool)
if jag_vill_ha_en_bool == "True":
    min_bool = True
elif jag_vill_ha_en_bool == "False":
    min_bool = False
else:
    print("Programmet kommer nu krascha, skriv in vad som efterfrågas nästa gång.")

print(type(min_bool))
print(min_bool)
