# Advent of Code 2017
# Alex Johnson
# Day 18

# input
input_file = open("input.txt", "r")
instrs = input_file.readlines()
input_file.close()

for i in range(len(instrs)):
  instrs[i] = instrs[i].strip("\n")

print("[PART 1]")
# run instructions
registers = {}
last_sound = 0
pos = 0

def touch(v):
  if v not in registers.keys():
    registers[v] = 0

def is_reg(v):
  return v in "abcdefghijklmnopqrstuvwxyz"

while pos < len(instrs):
  print(instrs[pos])
  instr = instrs[pos].split(" ")
  key = instr[0]
  reg = instr[1]
  val = 0
  touch(reg)
  if len(instr) == 3:
    val = instr[2]
    if is_reg(val):
      touch(val)
      val = registers[val]
    else:
      val = int(val)

  # handle instructions
  if key == "snd":
    last_sound = registers[reg]
  elif key == "set":
    registers[reg] = val
  elif key == "add":
    registers[reg] += val
  elif key == "mul":
    registers[reg] *= val
  elif key == "mod":
    registers[reg] = registers[reg] % val
  elif key == "rcv":
    if registers[reg] != 0:
      print("Recovered " + str(last_sound))
      break
  elif key == "jgz":
    if registers[reg] > 0:
      pos += val
      continue
  pos += 1

print("[PART 2]")
