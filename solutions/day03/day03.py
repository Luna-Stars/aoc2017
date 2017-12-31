# Advent of Code 2017
# Alex Johnson
# Day 3

# Imports
import math

# Input
with open("input.txt", "r") as infile:
    INPUT = int(infile.readline().strip())

# Solve part 1
print("[Part 1]")

# Compute ring width
ring = int(math.ceil(math.sqrt(INPUT)))
if ring % 2 == 0: ring += 1  # ring width is always odd; round up
ring_square = ring * ring

# distance to the ring is just half of the width
ring_dist = ring // 2

# Compute ring midpoints - count backwards by multiples of the ring's width
m_bottom = ring_square - ring_dist
m_left = m_bottom - ring
m_top = m_left - ring
m_right = m_top - ring
midpoints = [m_bottom, m_left, m_top, m_right]

# find the closest midpoint
min_dist = min(list(map(lambda x: abs(INPUT - x), midpoints)))
total_walk = min_dist + ring_dist

print(total_walk)

# Part 2: sequence is stored at https://oeis.org/A141481
# seq.txt holds the first 150 entries, taken from that site

print("[PART 2]")

with open("seq.txt", "r") as seqf:
    seq = [int(x.split(" ")[1]) for x in seqf.readlines()]

for x in seq:
    if x > INPUT:
        print(x)
        break
