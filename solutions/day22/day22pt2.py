# Advent of Code
# Alex Johnson
# Day 22, part 2

# direction constants
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

# status constants
CLEAN = 0
WEAKENED = 1
INFECTED = 2
FLAGGED = 3

# direction helper functions
def turn_left(d): return (d + 1) % 4
def turn_right(d): return (d - 1) % 4
def reverse(d): return (d - 2) % 4

def update_dir(d, s):
    if s == CLEAN: return turn_left(d)
    elif s == INFECTED: return turn_right(d)
    elif s == FLAGGED: return reverse(d)
    return d

# coordinate helper
def chash(x, y): return str(x) + '#' + str(y)
def extract(x, y, m): return m[chash(x, y)] if chash(x, y) in m.keys() else CLEAN
def setv(x, y, s, m): m[chash(x, y)] = s

def move(x, y, d):
    if d == UP:
        return (x - 1, y)
    elif d == DOWN:
        return (x + 1, y)
    elif d == LEFT:
        return (x, y - 1)
    return (x, y + 1)

# status helper
def step(status): return (status + 1) % 4

grid = {}

# get input
with open('input.txt', 'r') as infile:
    lines = [line.strip() for line in infile]
    offset = len(lines) // 2
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                setv(i-offset, j-offset, INFECTED, grid)

# initialize virus
xpos, ypos = 0, 0
direction = UP
count_infected = 0

for i in range(10000000):
    status = extract(xpos, ypos, grid)
    direction = update_dir(direction, status)
    status = step(status)
    setv(xpos, ypos, status, grid)
    xpos, ypos = move(xpos, ypos, direction)
    if status == INFECTED:
        count_infected += 1

print(count_infected)
