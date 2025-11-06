#!/usr/bin/env python3
import sys
sys.path.insert(0, '/root')

mat_mul = __import__('1-multiply').mat_mul
m1 = [[1]]
m2 = [[2]]
m = mat_mul(m1, m2)
if type(m) is not list or m is m1 or m is m2 or not len(m) or type(m[0]) is not list:
    print("Not a new matrix")
    sys.exit(1)
print("OK", end="")
