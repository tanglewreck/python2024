# Exempel på hur klassvariabler och instansvariabler interagerar.

class MyClass:
    my_int = 42
    my_str = "HEJ!"
    my_list = [1, 2]

    def __init__(self):
        self.my_list = []
        self.my2_list = [1]


mc = MyClass()
print("Listan i instansen:", mc.my_list)
print("Listan i klassen:", MyClass.my_list)
mc.my_list.append("Detta ska bara hamna i instansen")
print()
print("Listan i instansen:", mc.my_list)
print("Listan i klassen:", MyClass.my_list)
MyClass.my_list.append("Detta ska hamna i klassen")
print()
print("Listan i instansen:", mc.my_list)
print("Listan i klassen:", MyClass.my_list)
mc2 = MyClass()
print()
print("Listan i instansen:", mc.my_list)
print("Listan i andra instansen:", mc2.my_list)
print("Listan i klassen:", MyClass.my_list)
mc2.my_list.append("Detta ska bara hamna i andra instansen")
print()
print("Listan i instansen:", mc.my_list)
print("Listan i andra instansen:", mc2.my_list)
print("Listan i klassen:", MyClass.my_list)
print()
print("Lista 2 i instansen:", mc.my2_list)
print("Lista 2 i andra instansen:", mc2.my2_list)
