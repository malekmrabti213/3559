#!/usr/bin/env python3
import sys
add_arrays = __import__('0-add').add_arrays
a1, a2 = [1], [2]
a = add_arrays(a1, a2)
if type(a) is not list or a is a1 or a is a2:
    print("Not a new array")
    sys.exit(1)
print("OK")
