#!/usr/bin/env python3
import sys
sys.path.insert(0, '/root')

mat_mul = __import__('1-multiply').mat_mul
m1 = [[1, 2],
      [[3, 2], 4],
      [5, 6]]
m2 = [[9, 0, 5], [2, 3, 1]]
m = mat_mul(m1, m2)
if m is not None:
    print("Incorrect output")
    sys.exit(1)
print("OK", end="")