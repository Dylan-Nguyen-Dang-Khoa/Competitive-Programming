import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Mixed Fraction
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

n = 0
d = 0

# Read the input.
n, d = map(int, input().strip().split())

# TODO: This is where you should compute the answer and store them into the
# variables a and b.

a = 0
b = 0
a = n // d
b = n % d
# Write the answer.
if b != 0:
    print(a, f"{b}/{d}")
else:
    print(a)