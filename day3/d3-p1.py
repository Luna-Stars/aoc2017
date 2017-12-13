# Advent of Code 2017
# Alex Johnson
# Day 3, Problem 1

# Imports
import math

# Input
INPUT = 368078
print("Input: " + str(INPUT))
print()

# Compute ring width
ring_raw = math.ceil(math.sqrt(INPUT))
ring = int(ring_raw)
if ring % 2 == 0:
    ring += 1
ring_square = ring * ring

print("Ring width: " + str(ring))
print("Ring square: " + str(ring_square))
print()

# Compute distance to ring
ring_dist = ring // 2
print("Distance to ring: " + str(ring_dist))
print()

# Compute ring midpoints
bottom_midpoint = ring_square - ring_dist
left_midpoint = bottom_midpoint - (ring_dist * 2)
top_midpoint = left_midpoint - (ring_dist * 2)
right_midpoint = top_midpoint - (ring_dist * 2)

print("Bottom midpoint: " + str(bottom_midpoint))
print("Left midpoint: " + str(left_midpoint))
print("Top midpoint: " + str(top_midpoint))
print("Right midpoint: " + str(right_midpoint))
print()

# Minimum distance walk
min_dist = min([abs(INPUT - bottom_midpoint), abs(INPUT - left_midpoint), abs(INPUT - top_midpoint), abs(INPUT - right_midpoint)])
print("Walk from midpoint: " + str(min_dist))
print()

# Total walk
print("Total walk: " + str(min_dist + ring_dist))
