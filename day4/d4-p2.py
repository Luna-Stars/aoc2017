# Advent of Code
# Day 4, Part 2

# read input
in_f = open("d4-input.txt", "r")
input_arr = in_f.readlines()
in_f.close()

# clean input
for i in range(len(input_arr)):
    input_arr[i] = input_arr[i].strip("\n")

# helper
def isAnagram(x, y):
    return sorted(x) == sorted(y)

valid_phrases = 0

# process line
for line in input_arr:
    valid = True
    l = line.split()
    seen = []
    for word in l:
        for other in seen:
            if isAnagram(word, other):
                valid = False
        seen.append(word)
    if valid:
        valid_phrases += 1

print(valid_phrases)
