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
def turn_right(d): return (d - 1) % 4s

# coordinate helper
def chash(x, y): return str(x) + '#' + str(y)
