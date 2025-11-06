#!/usr/bin/env python3
import sys
sys.path.insert(0, '/root')

add_arrays = __import__('0-add').add_arrays
a1, a2 = [], [1]
a = add_arrays(a1, a2)
b1, b2 = [1], []
b = add_arrays(b1, b2)
c1, c2 = [7, 4, 9], [1, 2]
c = add_arrays(c1, c2)
d1, d2 = [5, 7, 8, 3], [4, 2, 7, 9, 4]
d = add_arrays(d1, d2)
if a is not b is not c is not d is not None:
    print("Incorrect output")
    sys.exit(1)
print("OK", end="")