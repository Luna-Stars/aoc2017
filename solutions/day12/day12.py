# Advent of Code 2017
# Day 12
# Alex Johnson

# Define variables
input_data = {}

# Process input file
ifile = open("input.txt", "r")

# Process lines
for line in ifile:
    key = int(line.split("<->")[0].strip(" "))
    connections = line.split("<->")[1].strip("\n").split(", ")
    for i in range(len(connections)):
        connections[i] = int(connections[i].strip(" "))
    input_data[key] = connections

# Cleanup
ifile.close()

# Helper functions
def getGroup(key, touched):
    """Assembles a group, given a key."""
    global input_data
    group = [key]
    for conn in input_data[key]:
        if conn in touched:
            continue
        touched.append(conn)
        if conn not in group:
            group.append(conn)
        others = getGroup(conn, touched)
        for other in others:
            if other not in group:
                group.append(other)
    group.sort()
    return group

def deepEquals(g1, g2):
    if len(g1) != len(g2):
        return False
    for i in range(len(g1)):
        if g1[i] != g2[i]:
            return False
    return True

groups = []

for key in input_data:
    group = getGroup(key, [])
    isUnique = True
    for other in groups:
        if deepEquals(group, other):
            isUnique = False
            break
    if isUnique:
        groups.append(group)

print(len(groups))
