def f():
    b = 20
    a = 1000
    print("Hej från f, där a är", a, "och b är", b)
    g()
    print("Hej en gång till från f, där b fortfarande är", b)


def g():
    b = 30
    print("Hej från g, där a är", a, "och b är", b)


a = 10


print("Här börjar vi och a är:", a)
f()
print("Nu är det slut och a är:", a)

