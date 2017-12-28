# Advent of Code
# Alex Johnson
# Day 14

import knot_hash

input_14 = "hwlqcszp"

print("[PART 1]")

# compute raw hashes
hashes_raw = []
for i in range(128):
    hashes_raw.append(knot_hash.knot_hash(input_14 + "-" + str(i)))

print("Hashes computed.")

# convert to binary
binary_hashes = []
for hash_hex in hashes_raw:
    hash_binary = str(bin(int(hash_hex, 16))[2:])
    while len(hash_binary) < 128:
        hash_binary = "0" + hash_binary
    binary_hashes.append(hash_binary)

print("Hashes converted to binary.")

# count number of squares used
used = 0
for h in binary_hashes:
    for char in h:
        if char == '1':
            used += 1

print("Squares used: " + str(used))
print()

print ("[PART 2]")

# prep hashes for DFS
hash_grid = binary_hashes[:]
for i in range(len(hash_grid)):
    hash_grid[i] = hash_grid[i].replace('1', '*')
    hash_grid[i] = hash_grid[i].replace('0','.')
    hash_grid[i] = list(hash_grid[i])

# helper functions
def exists_unmarked():
    global hash_grid
    for h in hash_grid:
        if '*' in h:
            return True
    return False

def get_first_unmarked():
    global hash_grid
    for i in range(len(hash_grid)):
        h = hash_grid[i]
        for j in range(len(h)):
            if h[j] == '*':
                return [i, j]
    return None

def mark(coords, group):
    global hash_grid
    x = coords[0]
    y = coords[1]
    if hash_grid[x][y] != "*":
        return
    hash_grid[x][y] = str(group)
    if x > 0:
        mark([x - 1, y], group)
    if x < 127:
        mark([x + 1, y], group)
    if y > 0:
        mark([x, y - 1], group)
    if y < 127:
        mark([x, y + 1], group)


group = 1
while exists_unmarked():
    mark(get_first_unmarked(), group)
    group += 1

group -= 1

print("Number of groups on disk: " + str(group))
