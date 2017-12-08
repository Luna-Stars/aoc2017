# Advent of Code 2017
# Alex Johnson
# Day 3, Problem 1

# Imports
import math

# Input
INPUT = 368078

# Compute ring width
ring_raw = math.ceil(math.sqrt(INPUT))
ring = int(ring_raw)
if ring % 2 == 0:
    ring += 1

print(ring)

# Compute distance to ring
ring_dist = ring // 2
print(ring_dist)