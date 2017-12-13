# Advent of Code 2017
# Day 7
# Alex Johnson

# Variables
input_file_name = "d7-input.txt"
node_weights = {}
node_parents = {}

# Read input
input_file = open(input_file_name, "r")

for line in input_file.readlines():
    split_line = line.strip("\n").split(" ")
    node_name = split_line[0]
    node_weight = int(split_line[1][1:-1])
    node_weights[node_name] = node_weight
    if len(split_line) > 2:
        for entry in split_line[3:]:
            entry_clean = entry.strip(",")
            node_parents[entry_clean] = node_name

input_file.close()


# Find bottom node (part 1)
base_node = node_parents.keys()[0]

while base_node in node_parents.keys():
    base_node = node_parents[base_node]

print("Base node: " + base_node)


# Find unbalanced node (part 2)
def get_weight(node):
    global node_weights
    global node_parents
    total_weight = node_weights[node]
    for key in node_parents.keys():
        if node_parents[key] == node:
            total_weight += get_weight(key)
    return total_weight


def find_unbalanced(node):
    if node in node_parents.keys():
