# Advent of Code
# Day 9

# load input from file into variable input_txt
input_file = open("input.txt", "r")
input_txt = input_file.readline().strip("\n")
input_file.close()

# declare variables
inGarbage = False
score = 0
group_depth = 1
character_i = 0
numGarbageChars = 0

# iterate over each character
while character_i < len(input_txt):
    cur_c = input_txt[character_i]
    if cur_c == "!": # check for skipping
        character_i += 1
    elif inGarbage: # handle garbage
        if cur_c == ">":
            inGarbage = False
        else:
            numGarbageChars += 1
    else: # handle stuff that actually matters
        if cur_c == "{":
            group_depth += 1
        elif cur_c == "}":
            group_depth -= 1
            score += group_depth
        elif cur_c == "<":
            inGarbage = True
    # move to next character
    character_i += 1

print(score)
print(numGarbageChars)
