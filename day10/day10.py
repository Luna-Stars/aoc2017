# Advent of Code
# Day 10
# Alex Johnson

# define variables
circular_list = list(range(256))
lengths = [157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30]  # input
cur_pos = 0
skip_size = 0

# helper functions
def get_sublist(l, start, length):
    end = start + length
    if end < len(l):
        return l[start:end]
    else:
        end -= len(l)
        return l[start:] + l[0:end]

def put_back(ilist, start, sublist):
    i = 0
    while i < len(sublist):
        ilist_i = i + start
        while ilist_i >= len(ilist):
            ilist_i -= len(ilist)
        ilist[ilist_i] = sublist[i]
        i += 1

# perform hash
for length in lengths:
    to_reverse = get_sublist(circular_list, cur_pos, length)
    to_reverse.reverse()
    put_back(circular_list, cur_pos, to_reverse)
    cur_pos += length + skip_size
    cur_pos = cur_pos % len(circular_list)
    skip_size += 1

print(circular_list[0] * circular_list[1])
