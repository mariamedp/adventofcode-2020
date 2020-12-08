
# fname = 'inputs/day08.test.txt'
fname = 'inputs/day08.txt'

with open(fname, 'r') as f:
    instructions = [l.strip().split(' ') for l in f.readlines()]


def run_program(instructions):
    executed = set()
    i, accumulator = 0, 0
    while i not in executed and i < len(instructions):
        executed.add(i)
        instruction, num = instructions[i]
        if instruction == 'acc':
            accumulator += int(num)
        if instruction == 'jmp':
            i += int(num)
        else:
            i += 1
    
    return accumulator, i == len(instructions)
    

for i in range(len(instructions)):
    instruction, num = instructions[i]
    if instruction == 'acc':
        continue

    instruction_changed = 'jmp' if instruction == 'nop' else 'nop'
    instructions_corrected = instructions[:i] + [(instruction_changed, num)] + instructions[i+1:]
    accumulator, finished = run_program(instructions_corrected)
    if finished:
        print(accumulator)
        break

    
