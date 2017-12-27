# Advent of Code
# Alex Johnson
# Day 25

state = 'A'
steps = 12481997

rules = {}
rules['A'] = [1,1,'B',0,-1,'C']
rules['B'] = [1,-1,'A',1,1,'D']
rules['C'] = [0,-1,'B',0,-1,'E']
rules['D'] = [1,1,'A',0,1,'B']
rules['E'] = [1,-1,'F',1,-1,'C']
rules['F'] = [1,1,'D',1,1,'A']

tape = {}
pos = 0

for i in range(steps):
    rule_offset = (tape[pos] if pos in tape.keys() else 0) * 3
    rule = rules[state][rule_offset:rule_offset + 3]
    tape[pos] = rule[0]
    pos += rule[1]
    state = rule[2]

count_1 = 0
for key in tape.keys():
    if tape[key] == 1:
        count_1 += 1

print(count_1)
