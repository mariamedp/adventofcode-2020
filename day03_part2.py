import sys

try:
	fname = sys.argv[1]
except:
	fname = 'inputs/day03.txt'

with open(fname, 'r') as f:
    map = [line.strip() for line in f.readlines()]

SLOPE_OPTIONS = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

mult = 1
for slope_right, slope_down in SLOPE_OPTIONS:
    x, y = 0, 0
    ntrees = 0
    while y < len(map):

        location = map[y][x % len(map[y])]
        if location == '#':
            ntrees += 1

        x += slope_right
        y += slope_down

    mult *= ntrees

print(mult)
