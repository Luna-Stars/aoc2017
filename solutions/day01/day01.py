# Advent of Code 2017
# Alex Johnson
# Day 1

# Load input
with open("input.txt", "r") as infile:
    intxt = infile.readline().strip()

# Part 1
# Sum the digits that match the following digit, looping at the end
print("[Part 1]")
total = 0
for i in range(len(intxt)):
    cur = intxt[i]
    comp = intxt[0] if i == len(intxt) - 1 else intxt[i + 1]
    if cur == comp:
        total += int(cur)

print(total)

# Part 2
# Sum the digits that match the digit halfway around the list
print("[Part 2]")
total = 0
half = len(intxt) // 2

for i in range(len(intxt)):
    cur = intxt[i]
    comp = intxt[i - half] if i >= half else intxt[i + half]
    if cur == comp:
        total += int(cur)

print(total)
