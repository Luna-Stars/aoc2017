# Advent of Code
# Alex Johnson
# Day 15

input_a = 591
input_b = 393

# define functions
def a(val):
    return (val * 16807) % 2147483647

def b(val):
    return (val * 48271) % 2147483647

# input
a_val = input_a
b_val = input_b

# part 1

print("[PART 1]")
count = 0
for i in range(40000000):
    if bin(a_val)[-16:] == bin(b_val)[-16:]:
        count += 1
    a_val = a(a_val)
    b_val = b(b_val)

print(count)
print()

# part 2
print("[PART 2]")

# define generators
def gen_a(start):
    val = start
    while True:
        val = (val * 16807) % 2147483647
        if val % 4 == 0:
            yield val

def gen_b(start):
    val = start
    while True:
        val = (val * 48271) % 2147483647
        if val % 8 == 0:
            yield val

count = 0
A = gen_a(input_a)
B = gen_b(input_b)
for i in range(5000000):
    if bin(next(A))[-16:] == bin(next(B))[-16:]:
        count += 1

print(count)
