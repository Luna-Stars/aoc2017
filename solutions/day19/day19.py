# Advent of Code
# Alex Johnson
# Day 19

# constants
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

# load input
input_file = open("input.txt", "r")
tube_map = input_file.readlines()
input_file.close()

# preprocess
for i in range(len(tube_map)):
    tube_map[i] = tube_map[i].strip("\n")

# part 1
print("[PART 1]")

# helpers
def proceed(row, col, direction):
    if direction == UP and row > 0:
        row -= 1
    elif direction == DOWN and row < len(tube_map) - 1:
        row += 1
    elif direction == LEFT and col > 0:
        col -= 1
    elif direction == RIGHT and col < len(tube_map[0]) - 1:
        col += 1
    else:
        return None
    return(row, col)

def next_step(row, col, direction):
    coords = proceed(row, col, direction)
    if coords == None:
        return None
    else:
        return tube_map[coords[0]][coords[1]]

# define variables
row = 0
col = -1
direction = DOWN
characters = []
steps = 0

# find start point
for i in range(len(tube_map[0])):
    if tube_map[0][i] == "|":
        col = i
        break

# travel
while True:
    steps += 1
    char = tube_map[row][col]
    if char not in "|-+": # check for character
        characters.append(char)

    step = next_step(row, col, direction)
    if step == None or step == " ":
        canContinue = True
        if direction in [UP, DOWN]:
            left = next_step(row, col, LEFT)
            right = next_step(row, col, RIGHT)
            if left != None and left != " ":
                direction = LEFT
            elif right != None and right != " ":
                direction = RIGHT
            else:
                canContinue = False
        else:
            up = next_step(row, col, UP)
            down = next_step(row, col, DOWN)
            if down != None and down != " ":
                direction = DOWN
            elif up != None and up != " ":
                direction = UP
            else:
                canContinue = False
        if not canContinue:
            break
    row, col = proceed(row, col, direction)

print("".join(characters))
print()
print("[PART 2]")
print(steps)
