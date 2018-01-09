# Advent of Code 2017
# Alex Johnson
# Day 22, part 1

# direction constants
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

# helper functions
def chash(x, y):
    return str(x) + '#' + str(y)

def turn_left(d):
    return (d + 1) % 4

def turn_right(d):
    return (d - 1) % 4

def infected(x, y, g):
    if chash(x, y) in g:
        return g[chash(x, y)]
    return False

def toggle(x, y, g):
    if chash(x, y) in g:
        g[chash(x, y)] = not g[chash(x, y)]
        return g[chash(x, y)]
    g[chash(x, y)] = True
    return True

def move(x, y, d):
    if d == UP:
        return (x - 1, y)
    elif d == DOWN:
        return (x + 1, y)
    elif d == LEFT:
        return (x, y - 1)
    elif d == RIGHT:
        return (x, y + 1)

grid = {}

# read input
with open('input.txt', 'r') as infile:
    lines = [line.strip() for line in infile]
    offset = len(lines) // 2  # calculate the midpoint of the grid
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                grid[chash(i-offset,j-offset)] = True

# initialize virus
xpos = 0
ypos = 0
direction = UP

# solve part 1
print("[PART 1]")

def burst(x, y, d, virus_map):
    if infected(x, y, virus_map):
        d = turn_right(d)
    else:
        d = turn_left(d)
    res = toggle(x, y, virus_map)
    x, y = move(x, y, d)
    return (x, y, d, res)

infection_count = 0
for i in range(10000):
    xpos, ypos, direction, res = burst(xpos, ypos, direction, grid)
    infection_count += 1 if res else 0

print(infection_count)
