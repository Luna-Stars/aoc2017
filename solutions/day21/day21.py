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

# logic functions
def iterate(art, rules):
    pass
