# Hur många äggkartonger ska vi köpa?

store_sells_loaves_of_bread = True

# Vi behöver egentligen inte skriva " == True" men jag skrev det här för att göra det
# lättare att läsa.
if store_sells_loaves_of_bread == True:
    egg_boxes_to_buy = 2
else:
    egg_boxes_to_buy = 1

print("Det blev", egg_boxes_to_buy, "äggkartonger!")
