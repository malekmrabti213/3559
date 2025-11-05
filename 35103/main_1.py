#!/usr/bin/env python3
import sys
mat_mul = __import__('1-multiply').mat_mul
m1 = [[6, -3], [5, 2]]
m2 = [[9, 0], [24, 3]]
m = mat_mul(m1, m2)
if type(m) is not list or m is m1 or m is m2 or not len(m) or type(m[0]) is not list:
    print("Not a new matrix")
    sys.exit(1)
if m != [[-18, -9], [93, 6]]:
    print("Incorrect output")
    sys.exit(1)
print("OK", end="")
