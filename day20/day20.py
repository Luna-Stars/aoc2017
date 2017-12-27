# Advent of Code 2017
# Alex Johnson
# Day 20

import sys, math

# Parse input
with open("input.txt", "r") as infile:
    # TODO break this down and make it readable - processes each line of input.txt into [p,v,a] where p, v, a are arrays [x, y, z]
    points = [list(map(lambda x: list(map(int,x[3:-1].split(","))), line.strip("\n").split(", "))) for line in infile]

# constants
POS = 0
VEL = 1
ACC = 2

# Helper functions
def dist(point, i):
    if i != 0:
        return math.sqrt(pow(point[0], 2) + pow(point[1], 2) + pow(point[2], 2))
    return abs(point[0]) + abs(point[1]) + abs(point[2])

def extract_mins(points, i):
    min_val = sys.maxsize
    mins = []
    for point in points:
        val = dist(point[i], i)
        if val < min_val:
            min_val = val
            mins = [point]
        elif val == min_val:
            mins.append(point)
    return mins

# Solve part 1
print("[PART 1]")

# To solve part 1, extract all points with minimum acceleration,
# then minimum velocity, then minimum position.
min_acc = extract_mins(points, ACC)
print(min_acc)
min_vel = extract_mins(min_acc, VEL)
print(min_vel)
min_pos = extract_mins(min_vel, POS)
print(points.index(min_pos[0]))
