
# fname = 'inputs/day10.test.txt'
# fname = 'inputs/day10.test2.txt'
fname = 'inputs/day10.txt'

with open(fname, 'r') as f:
    numbers = [int(l.strip()) for l in f.readlines()]

numbers = [0] + sorted(numbers)
differences = [numbers[i] - numbers[i-1] for i in range(1, len(numbers))]

if any(d not in (1, 2, 3) for d in differences):
    raise ValueError()

print(differences.count(1), differences.count(3) + 1)
print(differences.count(1) * (differences.count(3) + 1))
