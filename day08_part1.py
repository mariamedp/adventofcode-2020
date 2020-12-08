
# fname = 'inputs/day08.test.txt'
fname = 'inputs/day08.txt'

with open(fname, 'r') as f:
    instructions = [l.strip().split(' ') for l in f.readlines()]

executed = set()
i, accumulator = 0, 0
while i not in executed:
    executed.add(i)
    instruction, num = instructions[i]
    if instruction == 'acc':
        accumulator += int(num)
    if instruction == 'jmp':
        i += int(num)
    else:
        i += 1

print(accumulator)
    
