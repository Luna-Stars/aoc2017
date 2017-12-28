# Advent of Code
# Alex Johnson
# Knot Hashes

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

def knot_hash(hash_input):
    # get lengths for hash
    lengths = []
    for char in hash_input.encode('ascii'):
        lengths.append(char)  # get ascii for each character

    # add extra lengths
    lengths += [17, 31, 73, 47, 23]

    # define variables
    circular_list = list(range(256))
    cur_pos = 0
    skip_size = 0

    # get sparse hash
    for i in range(64):
        for length in lengths:
            to_reverse = get_sublist(circular_list, cur_pos, length)
            to_reverse.reverse()
            put_back(circular_list, cur_pos, to_reverse)
            cur_pos += length + skip_size
            cur_pos = cur_pos % len(circular_list)
            skip_size += 1

    dense_hash = ""

    # compute dense hash
    for i in range(16):
        sublist_start = i * 16
        sublist_end = (i + 1) * 16
        output_num = circular_list[sublist_start]
        for val in circular_list[sublist_start + 1:sublist_end]:
            output_num = output_num ^ val
        hex_val = hex(output_num)[2:]
        if len(hex_val) != 2:
            hex_val = '0' + hex_val
        dense_hash += hex_val

    return dense_hash
