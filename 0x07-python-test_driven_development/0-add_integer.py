#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, int):
        raise TypeError('a must be an integer')
    if not isinstance(b, int):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, 1))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)