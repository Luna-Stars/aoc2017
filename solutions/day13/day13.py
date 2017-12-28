# Advent of Code 2017
# Day 13
# Alex Johnson

firewall_data = {}

# Read input file
input_file = open("input.txt", "r")
for line in input_file.readlines():
    preprocess = line.strip("\n").split(": ")
    key = int(preprocess[0])
    val = int(preprocess[1])
    firewall_data[key] = val

input_file.close()

# helper functions
def get_scanner_pos(tick, r):
    mod = (r * 2) - 2
    pos = tick % mod
    if pos >= r:
        diff = (pos - r + 1) * 2
        pos = pos - diff
    return pos

def simulate(firewall, delay):
    """Returns an array of all the layers in which the packet will be caught."""
    collisions = []
    max_firewall_layer = max(firewall.keys()) + 1
    for i in range(max_firewall_layer):
        tick = i + delay
        if i in firewall.keys():
            if get_scanner_pos(tick, firewall[i]) == 0:
                collisions.append(i)
    return collisions

# solve part 1
no_delay = simulate(firewall_data, 0)
severity = 0
for entry in no_delay:
    severity += entry * firewall_data[entry]

print("[PART 1]")
print("Severity of trip with no delay: " + str(severity))
print()

# solve part 2
print("[PART 2]")

delay = -1
num_hits = 1

while num_hits > 0:
    delay += 1
    num_hits = len(simulate(firewall_data, delay))

print("Delay that results in 0 hits: " + str(delay))
