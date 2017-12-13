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
base_node = list(node_parents.keys())[0]

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

def get_children(node):
    global node_parents
    children = []
    for key in node_parents.keys():
        if node_parents[key] == node:
            children.append(key)
    return children

def get_unbalanced(node):
    """Return the node that needs to be rebalanced."""
    global node_weights
    print("balancing " + node)
    children = get_children(node)
    weights = {}
    base_weights = {}
    weight_frequency = {}
    base_weight_frequency = {}
    for child in children:
        weight = get_weight(child)
        weights[child] = weight
        base_weights[child] = node_weights[child]
        if weight in weight_frequency.keys():
            weight_frequency[weight] += 1
        else:
            weight_frequency[weight] = 1
        if base_weights[child] in base_weight_frequency.keys():
            base_weight_frequency[base_weights[child]] += 1
        else:
            base_weight_frequency[base_weights[child]] = 1
    if len(base_weight_frequency.keys()) > 1:
        print("ONE OF THE DIRECT CHILDREN OF "+node+" IS UNBALANCED")
    if len(weight_frequency.keys()) > 1:
        # find unbalanced child
        min_weight_freq = min(weight_frequency.values())
        problem_child = None
        for child in children:
            if weight_frequency[weights[child]] == min_weight_freq:
                problem_child = child
                break
        print("problem child is " + problem_child)
        return get_unbalanced(problem_child)
    else:
        print("CHILDREN OF NODE " + node + " ARE BALANCED")
        return node

rebalance_node = get_unbalanced(base_node)
print("Weight of problem child: " + str(get_weight(rebalance_node)))
siblings = get_children(node_parents[rebalance_node])
if siblings[0] == rebalance_node:
    siblings = siblings[1:]
weight_goal = get_weight(siblings[0])
weight_children = 0
children = get_children(rebalance_node)
for child in children:
    weight_children += get_weight(child)
print(weight_goal - weight_children)
