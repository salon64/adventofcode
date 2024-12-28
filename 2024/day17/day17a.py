import time
from collections import defaultdict, deque as queue
start_time = time.time()
with open('2024/day17/day_17_input.txt', 'r') as file: # day_17_input.txt
    data = file.read().strip().splitlines()

registers = [0, 0, 0]
instructions = []
for i, line in enumerate(data):
    if i < 3:
        tmp = line.split()
        registers[i] = int(tmp[-1])
    elif i == 4:
        tmp = line[8:]
        tmp = tmp.split(",")
        instructions = [int(instr) for instr in tmp]
print(registers)
print(instructions)
print()

# 3 bit comp 0-7
# registers, can hold any int
# 8 instructions has opcode and operand (3bit)
# instruction pointer -> points to next instruction
#
# The value of a literal operand is the operand itself
# Combo operands 0 through 3 represent literal values 0 through 3.
# Combo operand 4 represents the value of register A.
# Combo operand 5 represents the value of register B.
# Combo operand 6 represents the value of register C.
# Combo operand 7 is reserved and will not appear in valid programs.
outputs = []
instr_pointer = 0
while instr_pointer in range(0, len(instructions)):
    # A, B, C = registers[:]
    opcode = instructions[instr_pointer]
    operand = instructions[instr_pointer+1]
    
    def get_combo():
        if operand >= 0 and operand <= 3:
            return operand
        elif operand == 4:
            return registers[0]
        elif operand == 5:
            return registers[1]
        elif operand == 6:
            return registers[2]
        elif operand == 7:
            print("no combo 7")
            return '-1'
    
    # print(f"opcode:{opcode}, operand:{operand}, combo:{combo}, A:{A}, B:{B}, C:{C}, instr_ptr:{instr_pointer}")
    if opcode == 0: # adv, divition
        registers[0] = registers[0] // (2**get_combo())

    elif opcode == 1: # bxl, bitwise xor
        registers[1] = registers[1] ^ operand # literal operand

    elif opcode == 2: # bst, modulo 8
        registers[1] = get_combo() % 8

    elif opcode == 3: # jnz, 
        if registers[0] == 0:
            #do nothing
            pass
        else:
            instr_pointer = operand # literal operand
            continue # does not add 2 to the instr_pointer after performing instruction

    elif opcode == 4: # bxc, bitwise XOR
        registers[1] = registers[1] ^ registers[2]
        # kanske ladda in en combo?

    elif opcode == 5: # out, 
        tmp = get_combo() % 8
        outputs.append(str(tmp))
        # print(tmp)

    elif opcode == 6: # bdv
        registers[1] = registers[0] // (2**get_combo())

    elif opcode == 7: # cdv
        registers[2] = registers[0] // (2**get_combo())

    instr_pointer += 2

print(",".join(outputs))





end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
