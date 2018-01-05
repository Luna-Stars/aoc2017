# Advent of Code 2017
# Alex Johnson
# Day 18

import sys

# input
with open("input.txt", "r") as infile:
    instrs = [i.strip() for i in infile]


# helper functions
def touch(v, regs):
    if v not in regs.keys():
        regs[v] = 0


def is_reg(v):
    return v in "abcdefghijklmnopqrstuvwxyz"


def get_val(v, regs):
    if is_reg(v):
        touch(v, regs)
        return regs[v]
    else:
        return int(v)


# functions to perform register operations
def snd(x, queue, regs):
    queue.append(get_val(x, regs))


def set(reg, val, regs):
    regs[reg] = get_val(val, regs)


def add(reg, val, regs):
    regs[reg] += get_val(val, regs)


def mul(reg, val, regs):
    regs[reg] *= get_val(val, regs)


def mod(reg, val, regs):
    regs[reg] = regs[reg] % get_val(val, regs)


def rcv(reg, queue, regs):
    if get_val(reg, regs) != 0:
        print(queue.pop())


def jgz(reg, val, regs):
    if get_val(reg, regs) > 0:
        return get_val(val, regs)
    else:
        return 0


class ProgramState:
    def __init__(self, instrs, in_queue):
        self.regs = {}
        self.out_queue = []
        self.in_queue = in_queue
        self.instrs = instrs
        self.pos = 0
        self.can_continue = True

    def advance(self):
        instr = instrs[self.pos].split(" ")
        key = instr[0]
        reg = instr[1]
        touch(reg, self.regs)
        val = 0
        if len(instr) == 3:
            val = instr[2]

        # handle instructions
        if key == "snd":
            snd(reg, self.out_queue, self.regs)
        elif key == "set":
            set(reg, val, self.regs)
        elif key == "add":
            add(reg, val, self.regs)
        elif key == "mul":
            mul(reg, val, self.regs)
        elif key == "mod":
            mod(reg, val, self.regs)
        elif key == "rcv":
            if len(self.in_queue) == 0:
                self.can_continue = False
            else:
                rcv(reg, self.in_queue, self.regs)
        elif key == "jgz":
            jmp = jgz(reg, val, self.regs)
            if jmp != 0:
                self.pos += jmp
                return
        self.pos += 1


print("[PART 1]")
# run instructions
ps = ProgramState(instrs, [])

while ps.can_continue:
    ps.advance()

print(ps.out_queue[-1])

print("[PART 2]")
