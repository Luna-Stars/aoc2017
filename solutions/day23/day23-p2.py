# Advent of Code 2017
# Alex Johnson
# Day 23

# TODO decompile input.txt
b = 65
c = 65
b *= 100
b += 100000
c = b
c += 17000
h = 0

while True:
    f = 1
    d = 2
    while True:
        e = 2
        while True:
            g = d
            g *= e
            g -= b
            if g == 0:
                f = 0
            e += 1
            g = e
            g -= b
        g += 8
        d += 1
        g = d
        g -= b
    if f == 0:
        h += 1
    g = b
    g -= c
    if g == 0:
        break
    b += 17

print(h)
