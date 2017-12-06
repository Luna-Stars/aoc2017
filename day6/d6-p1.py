# Advent of Code 2017
# Day 6, Problem 1
# Alex Johnson

# Variables
mem_banks = []
seen = []
cur_bank = ""
iters = 0

# Load Input
input_file = open("input.txt", "r")
for line in input_file.readlines():
    mem_banks.append(int(line.strip("\n")))
input_file.close()

# More Variables
div_val = len(mem_banks) - 1

print(mem_banks)

# Algorithm
while cur_bank not in seen:
    # increment iteration count
    iters += 1
    # mark state as visited
    seen.append(cur_bank)
    # get max val mem bank
    max_bank_val = max(mem_banks)
    i = mem_banks.index(max_bank_val)
    mem_banks[i] = 0
    # make additions to other banks
    while max_bank_val > 0:
        i += 1
        if i == len(mem_banks):
            i = 0
        max_bank_val -= 1
        mem_banks[i] += 1
    # assemble bank string
    cur_bank = ""
    for bank in mem_banks:
        cur_bank += str(bank) + ","

print("Number of iterations to previously-seen state:", iters)
print("Index of first instance of state:", seen.index(cur_bank))
print("Difference:", iters - seen.index(cur_bank))
