# Advent of Code 2017
# Day 1, Problem 1
# Alex Johnson

# Read input #
input_f = open("d1-input.txt", "r")
input_txt = input_f.readline().strip("\n")
input_f.close()

# Process #
running_sum = 0
for i in range(len(input_txt)):
    cur_char = input_txt[i]
    compare_to = input_txt[0] if i == len(input_txt) - 1 else input_txt[i + 1]
    if cur_char == compare_to:
        running_sum += int(cur_char)

print(running_sum)
