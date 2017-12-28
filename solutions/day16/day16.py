# Advent of Code
# Alex Johnson
# Day 16

# helper functions
def swap(l, i, j):
    """swaps the element at index i & at index j of l."""
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def perform_dance(dancers, move):
    """Processes and performs a single dance move."""
    move_type = move[0]
    move_content = move[1:]
    d = dancers[:]

    # handle each type of move
    if move_type == "s":  # PERFORM SPIN
        spin_amt = int(move_content)
        end_dancers = d[-spin_amt:]
        beginning_dancers = d[0:-spin_amt]
        d = end_dancers + beginning_dancers

    elif move_type == "x":  # PERFORM EXCHANGE
        exchange = move_content.split("/")
        exchange[0] = int(exchange[0])
        exchange[1] = int(exchange[1])
        swap(d, exchange[0], exchange[1])

    elif move_type == "p":  # PERFORM PAIR
        pair = move_content.split("/")
        ex1 = dancers.index(pair[0])
        ex2 = dancers.index(pair[1])
        swap(d, ex1, ex2)

    return d

# get input.
input_file = open("input.txt", "r")
dance = input_file.readline().strip("\n").split(",")
input_file.close()

# generate all permutations before the thing starts to loop.
permutations = []
dancers = "abcdefghijklmnop"
original_dancers = dancers

while len(permutations) == 0 or dancers != original_dancers:
    permutations.append(dancers)
    d = list(dancers)
    for move in dance:
        d = perform_dance(d, move)
    dancers = "".join(d)

# get solutions.
print("[Part 1]")
print(permutations[1])
print()
print("[Part 2]")
print(permutations[1000000000%len(permutations)])
