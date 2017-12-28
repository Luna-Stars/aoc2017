# Advent of Code 2017
# Alex Johnson
# Day 20

from operator import add
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

def add(p1, p2):
    new = []
    for i in range(len(p1)):
        new.append(p1[i] + p2[i])
    return new

# Solve part 1
print("[PART 1]")

# To solve part 1, extract all points with minimum acceleration,
# then minimum velocity, then minimum position.
min_acc = extract_mins(points, ACC)
min_vel = extract_mins(min_acc, VEL)
min_pos = extract_mins(min_vel, POS)
print(points.index(min_pos[0]))

# Solve part 2
print("[PART 2]")

def move(point):
    acc = point[ACC]
    vel = add(point[VEL], acc)
    pos = add(point[POS], vel)
    return [pos, vel, acc]

def deep_eq(p1, p2):
    for i in range(len(p1)):
        if p1[i] != p2[i]: return False
    return True

def pos_checksum(pos):
    return str(pos[0]) + "/" + str(pos[1]) + "/" + str(pos[2])

for i in range(1000):  # TODO detect that points aren't moving towards eachother
    pts = {}
    for j in range(len(points)):
        chk = pos_checksum(points[j][POS])
        if chk in pts.keys():
            pts[chk].append(points[j])
        else:
            pts[chk] = [points[j]]

    for key in pts.keys():
        if len(pts[key]) > 1:
            for p in pts[key]:
                points.remove(p)

    for j in range(len(points)):
        points[j] = move(points[j])

print(len(points))
