# Advent of Code 2017
# Alex Johnson
# Day 2

# Load input
with open("input.txt", "r") as infile:
    lines = [list(map(int, line.strip("\n").split("\t"))) for line in infile]

# Part 1
print("[Part 1]")
checksum = 0
for line in lines:
    checksum += max(line) - min(line)

print(checksum)

# Part 2
print("[Part 2]")
divsum = 0
for line in lines:
    for i in range(len(line)):
        cur = line[i]
        for j in range(i + 1, len(line)):
            comp = line[j]
            quotient = -1
            # check for evenly dividing pair
            if cur % comp == 0:
                quotient = cur // comp
            elif comp % cur == 0:
                quotient = comp // cur
            if quotient != -1:
                divsum += quotient
                break

print(int(divsum))
