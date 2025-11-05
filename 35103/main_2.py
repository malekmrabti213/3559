#!/usr/bin/env python3
import sys
mat_mul = __import__('1-multiply').mat_mul
m1 = [[6, -3], [5, 2], [8, 4]]
m2 = [[9, 0, 10, 5], [2, 3, 7, 1]]
m = mat_mul(m1, m2)
if type(m) is not list or m is m1 or m is m2 or not len(m) or type(m[0]) is not list:
    print("Not a new matrix")
    sys.exit(1)
if m != [[48, -9, 39, 27], [49, 6, 64, 27], [80, 12, 108, 44]]:
    print("Incorrect output")
    sys.exit(1)
print("OK", end="")
