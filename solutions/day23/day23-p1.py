# Advent of Code 2017
# Alex Johnson
# Day 23

# prep registers
regs = {x: 0 for x in "abcdefgh"}
instr = 0

# define helpers
def val(x, regs):
    if x in regs.keys():
        return regs[x]
    return int(x)

# read input
with open("input.txt", "r") as infile:
    instrs = [line.strip("\n").split(" ") for line in infile]

# instruction ops
def setr(regs, x, y): regs[x] = val(y, regs)
def sub(regs, x, y): regs[x] -= val(y, regs)
def mul(regs, x, y): regs[x] *= val(y, regs)
def jmp(regs, x, y): return val(y, regs) if val(x, regs) != 0 else 0

# process
print("[PART 1]")

mul_count = 0
while instr < len(instrs):
    inst = instrs[instr]
    instn, x, y = inst[0], inst[1], inst[2]
    if instn == "set":
        setr(regs, x, y)
    elif instn == "sub":
        sub(regs, x, y)
    elif instn == "mul":
        mul_count += 1
        mul(regs, x, y)
    elif instn == "jnz":
        jmp_amt = jmp(regs, x, y)
        if jmp_amt != 0:
            instr += jmp_amt
            continue
    instr += 1

print(mul_count)
