# Advent of Code 2017
# Alex Johnson
# Day 8

# Variables
registers = {}
highest_val = 0
input_file = "d8-input.txt"


# Methods
def touch_register(r):
    global registers
    if r not in registers.keys():
        registers[r] = 0
    return r


# read input
input_f = open(input_file, "r")

# process lines
for line in input_f.readlines():
    line_raw = line.strip("\n").split(" ")
    # get components of line
    mod_r = touch_register(line_raw[0])  # register to modify
    op = line_raw[1]  # operation
    mod_val = int(line_raw[2])
    cond_r = touch_register(line_raw[4])  # register to check
    cond_op = line_raw[5]  # comparison operation
    cond_val = int(line_raw[6])  # value to compare cond_r to
    # process
    if op == "dec":
        mod_val = -mod_val
    # check conditional:
    perform_op = False
    if cond_op == "==":
        perform_op = registers[cond_r] == cond_val
    elif cond_op == ">":
        perform_op = registers[cond_r] > cond_val
    elif cond_op == "<":
        perform_op = registers[cond_r] < cond_val
    elif cond_op == "<=":
        perform_op = registers[cond_r] <= cond_val
    elif cond_op == ">=":
        perform_op = registers[cond_r] >= cond_val
    elif cond_op == "!=":
        perform_op = registers[cond_r] != cond_val

    if perform_op:
        registers[mod_r] += mod_val

    if max(registers.values()) > highest_val:
        highest_val = max(registers.values())

input_f.close()

print(max(registers.values()))
print(highest_val)
