# Advent of Code 2017
# Alex Johnson
# Day 4

# input
with open("input.txt", "r") as in_file:
    lines = [line.strip().split() for line in in_file]

# part 1
print('[PART 1]')

count = 0
for line in lines:
    valid = True
    found = []
    for word in line:
        if word in found:
            valid = False
            break
        else:
            found.append(word)
    count += 1 if valid else 0

print(count)


# part 2
def str_sort(x):
    return "".join(sorted(x))


print('[PART 2]')
count = 0
for line in lines:
    valid = True
    seen = []
    for word in line:
        if str_sort(word) in seen:
            valid = False
        else:
            seen.append(str_sort(word))
    count += 1 if valid else 0

print(count)
