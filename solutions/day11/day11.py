# Advent of Code 2017
# Day 11
# Alex Johnson

# Using x and y hex coordinates
# Good descriptive article:
# http://3dmdesign.com/development/hexmap-coordinates-the-easy-way

# Load input
ifile = open("input.txt")
path = ifile.readline().strip("\n").split(",")
ifile.close()

# Declare variables
x = 0
y = 0
current_distance = 0
max_distance = 0

# Execute instructions
for step in path:
    if step == 'n':
        y += 1
    elif step == 's':
        y -= 1
    elif step == 'ne':
        x += 1
        y += 1
    elif step == 'sw':
        x -= 1
        y -= 1
    elif step == 'se':
        x += 1
    elif step == 'nw':
        x -= 1
    # Compute hex distance
    delta = y - x
    current_distance = max(abs(x), abs(y), abs(delta))
    if current_distance > max_distance:
        max_distance = current_distance

print("Distance from (0,0): "+str(current_distance))
print("Maximum distance from (0,0): "+str(max_distance))
