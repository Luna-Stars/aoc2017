# Advent of Code 2017
# Alex Johnson
# Day 24

# load input
with open("input.txt", "r") as infile:
    parts = [list(map(int,line.split("/"))) for line in infile]

def sort(l):
    for item in l:
        item.sort()
    l.sort()

sort(parts)

# solve part 1
print("[Part 1]")
bridges = []

def build_bridges(bridge):
    current_port = bridge[-1][1]
    bridges = [bridge]
    for part in parts:
        if part in bridge: continue
        if part[0] == current_port:
            bridges += build_bridges(bridge + [part])
        elif part[1] == current_port:
            part.reverse()
            bridges += build_bridges(bridge + [part])
    return bridges

def strength(bridge):
    strength = 0
    for part in bridge:
        strength += part[0] + part[1]
    return strength

for part in parts:
    parts.sort()
    if part[0] == 0:
        bridges += build_bridges([part])

max_strength = 0
for bridge in bridges:
    bridge_st = strength(bridge)
    max_strength = bridge_st if bridge_st > max_strength else max_strength

print(max_strength)

# solve part 2
print("[Part 2]")
max_length = 0
long_bridges = []

for bridge in bridges:
    lbridge = len(bridge)
    if lbridge > max_length:
        max_length = lbridge
        long_bridges = [bridge]
    elif lbridge == max_length:
        long_bridges.append(bridge)

strengths = [strength(bridge) for bridge in long_bridges]
print(max(strengths))
