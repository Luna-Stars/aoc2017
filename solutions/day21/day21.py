# Advent of Code 2017
# Alex Johnson
# Day 21

# input
with open("input.txt", "r") as infile:
    rules = {}
    for line in infile:
        splitline = line.split(" => ")
        rules[splitline[0].strip()] = splitline[1].strip()

# starting grid
art = [['.','#','.'],['.','.','#'],['#','#','#']]

# helper functions
def flatten(grid):
    return "/".join(["".join(x) for x in grid])

def expand(flat):
    return [list(x) for x in flat.split("/")]

def rotate(grid):
    return [list(x) for x in zip(*grid[::-1])]

def flip_horiz(grid):
    return [x[::-1] for x in grid]

def flip_vert(grid):
    return grid[::-1]

def match_straight(grid, rule):
    return flatten(grid) == rule

def match_flip(grid, rule):
    return match_straight(grid, rule) or match_straight(flip_vert(grid), rule) or match_straight(flip_horiz(grid), rule) or match_straight(flip_horiz(flip_vert(grid)), rule)

def match(grid, rule):
    return match_flip(grid, rule) or match_flip(rotate(grid), rule) or match_flip(rotate(rotate(grid)), rule) or match_flip(rotate(rotate(rotate(grid))), rule)

def slice2d(matrix, start_row, end_row, start_col, end_col):
    return [row[start_col:end_col] for row in matrix[start_row:end_row]]

def transplant(matrix, sub_block, start_row, start_col):
    for i in range(len(sub_block)):
        mi = i + start_row
        print(i)
        for j in range(len(sub_block)):
            mj = j + start_col
            matrix[mi][mj] = sub_block[i][j]

# logic functions
def iterate(art, rules):
    # determine number of squares in a row
    squares = len(art)//2 if len(art) % 2 == 0 else len(art)//3
    size = 2 if len(art) % 2 == 0 else 3
    # compute size of new grid
    grid_width = squares * (size + 1)
    # build new grid
    grid = [[None]*squares]*squares
    # identify rules
    for i in range(0,len(art),size):
        for j in range(0,len(art[0]),size):
            block = slice2d(art, i, i+size, j, j+size)
            for key in rules.keys():
                if match(block, key):
                    new_block = expand(rules[key])
                    grid[i//size][j//size] = new_block
    # join rules
    new_art = []
    for row in grid:
        for i in range(size+1):
            next_row = []
            for rule in row:
                next_row += rule[i]
            new_art.append(next_row)
    return new_art

print("[PART 1]")

for i in range(2):
    art = iterate(art, rules)

count_on = 0
for line in art:
    print("".join(line))
