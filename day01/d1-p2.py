# Advent of Code 2017
# Day 1, Problem 2
# Alex Johnson

# Read Input #
input_f = open("d1-input.txt", "r")
input_txt = input_f.readline().strip("\n")
input_f.close()

# Process #
running_sum = 0
length_half = len(input_txt)//2

for i in range(len(input_txt)):
    current = input_txt[i]
    compare_to = input_txt[i - length_half] if i >= length_half else input_txt[i + length_half]
    if current == compare_to:
        running_sum += int(current)

print(running_sum)
