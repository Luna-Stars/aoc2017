# Advent of Code 2017
# Day 5, Problem 1
# Alex Johnson

# variables
jumps = []
index = 0
steps = 0

# read input
input_file = open("d5-input.txt", "r")
for line in input_file.readlines():
    jumps.append(int(line.strip("\n")))
input_file.close()

# loop
while index < len(jumps):
    # get jump to make and increment
    cur_val = jumps[index]
    if jumps[index] >= 3:
        jumps[index] -= 1
    else:
        jumps[index] += 1
    # make jump
    index += cur_val
    # update step count
    steps += 1

# print output
print(steps)

