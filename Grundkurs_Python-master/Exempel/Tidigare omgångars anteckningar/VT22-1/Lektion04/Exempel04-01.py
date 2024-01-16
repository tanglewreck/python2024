# Demonstration av slicing och metoder på listor, tuples och dicts.

my_fruit_list = ["päron", "äpplen", "apelsiner", "citroner", "vindruvor"]

# Jag hämtar och skriver ut de tre första elementen ur my_fruits_list på
# två olika sätt
print(my_fruit_list[0:3])
print(my_fruit_list[:3])

# Jag gör detsamma med de tre elementen i mitten.
print(my_fruit_list[1:4])

# Slutligen, de tre sista. På tre olika sätt.
print(my_fruit_list[2:5])
print(my_fruit_list[2:])
print(my_fruit_list[-3:])

# Splicing fungerar även på strängar.
print("1234567890"[0:5])
