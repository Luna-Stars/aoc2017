# Advent of Code 2017
# Alex Johnson
# Day 21

# helpers
def flatten(grid): return "/".join(["".join(row) for row in grid])
def expand(flat): return [list(row) for row in flat.split("/")]
def slice2d(grid, ox, oy, ix, iy): return [row[ix:iy] for row in grid[ox:oy]]
def rotate(grid): return [list(row) for row in zip(*grid[::-1])]
def flip_horiz(grid): return [row[::-1] for row in grid]
def flip_vert(grid): return grid[::-1]

def get_match(rule, rules):
    if flatten(rule) in rules.keys():
        return rules[flatten(rule)]
    return None

def get_match_flip(rule, rules):
    keys = []
    keys.append(rule)
    keys.append(flip_horiz(rule))
    keys.append(flip_vert(rule))
    for key in keys:
        val = get_match(key, rules)
        if val: return val
    return None

def match(rule, rules):
    keys = []
    for i in range(4):
        keys.append(rule)
        rule = rotate(rule)
    for key in keys:
        val = get_match_flip(key, rules)
        if val: return val
    return None


# get input
rules = {}
with open('input.txt', 'r') as infile:
    lines = [line.strip().split(" => ") for line in infile]
    for line in lines:
        rules[line[0]] = line[1]

# perform loop
grid = [list(".#."), list("..#"), list("###")]

# perform iterations
for Z in range(18):
    # step 1: determine the size and count of the subpatterns
    size = 3
    if len(grid) % 2 == 0: size = 2
    count = len(grid) // size
    # step 2: break the grid into subpatterns
    patterns = []
    for i in range(0, len(grid), size):
        row = []
        for j in range(0, len(grid), size):
            subpattern = slice2d(grid, i, i+size, j, j+size)
            row.append(subpattern)
        patterns.append(row)
    # step 3: match each pattern with a rule and swap
    for i in range(len(patterns)):
        for j in range(len(patterns)):
            new_pattern = match(patterns[i][j], rules)
            patterns[i][j] = new_pattern
    # step 4: expand patterns into arrays
    for i in range(len(patterns)):
        for j in range(len(patterns)):
            patterns[i][j] = expand(patterns[i][j])
    # step 5: join patterns
    new_grid = []
    for i in range(len(patterns)):
        for j in range(len(patterns[i][0])): # row of pattern to join
            new_row = []
            for pattern in patterns[i]:
                new_row += pattern[j]
            new_grid.append(new_row)
    grid = new_grid

count_on = 0
for line in grid:
    for char in line:
        if char == '#':
            count_on += 1
print(count_on)
