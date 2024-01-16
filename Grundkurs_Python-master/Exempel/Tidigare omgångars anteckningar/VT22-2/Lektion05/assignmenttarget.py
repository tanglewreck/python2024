# https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy
#
#   Mutable sequences can be changed after they are created. The
#   subscription and slicing notations can be used as the target of
#   assignment and del (delete) statements.
#

class Value:
    def __init__(self, initial_value=0):
        self._val = initial_value

    def __add__(self, other):
        print("add:", other)
        return type(self)(self._val + other)

    def __repr__(self):
        return "Value(%r)" % self._val


class MutableValue(Value):
    def __iadd__(self, other):
        print("iadd:", other)
        self._val += other
        return self

    def __repr__(self):
        return "MutableValue(%r)" % self._val


class ThingList(list):
    def __getitem__(self, key):
        print("getitem: index %r" % (key,))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print("setitem: index %r <- %r" % (key, value))
        super().__setitem__(key, value)


def main():
    x = Value(1)
    x_ref = x
    x += 1
    print(x)
    print(x_ref)
    print()

    y = MutableValue(1)
    y_ref = y
    y += 1
    print(y)
    print(y_ref)
    print()

    things = ThingList([x, y])
    things_ref = things
    things[0] += 1
    print(things)
    print(things_ref)
    print()

    things[1] += 1
    print(things)
    print(things_ref)
    print()


if __name__ == "__main__":
    main()
