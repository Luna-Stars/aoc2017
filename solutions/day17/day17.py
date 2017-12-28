# Advent of Code
# Day 17
# Alex Johnson

step = 337

# part 1
print("[PART 1]")
spinlock = [0]
pos = 0
for i in range(1,2018):
    pos = (pos + step) % len(spinlock)
    pos += 1
    spinlock.insert(pos, i)

print(spinlock[(spinlock.index(2017) + 1) % len(spinlock)])

print("[PART 2]")
pos = 0
second = -1
for i in range(1, 5000000001):
    pos = (pos + step) % i
    pos += 1
    if pos == 1:
        second = i

print(second)
