#!/usr/bin/env python3
import sys
sys.path.insert(0, '/root')

add_arrays = __import__('0-add').add_arrays
a1, a2 = [-5, 7, -3, -2, 8], [1, -4, -6, 3, 9]
a = add_arrays(a1, a2)
if type(a) is not list or a is a1 or a is a2:
    print("Not a new array")
    sys.exit(1)
if a != [-4, 3, -9, 1, 17]:
    print("Incorrect output")
    sys.exit(1)
print("OK", end="")
