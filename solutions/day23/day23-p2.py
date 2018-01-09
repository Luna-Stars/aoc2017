# Advent of Code 2017
# Alex Johnson
# Day 23
# decompiled assembly

import math

start = (65 * 100) + 100000
count = 0

def prime(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

for i in range(start, start + 17001, 17):
    if not prime(i):
        count += 1

print(count)
