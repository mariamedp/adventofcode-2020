import sys

try:
	fname = sys.argv[1]
except:
	fname = 'inputs/day01.txt'

with open(fname, 'r') as f:
	numbers = [int(n.strip()) for n in f.readlines()]

remainder = [2020 - n for n in numbers]

for r in remainder:
    try:
        numbers.index(r)
        print(r * (2020 - r))
        break
    except:
        pass

