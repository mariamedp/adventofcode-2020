import sys

try:
	fname = sys.argv[1]
except:
	fname = 'inputs/day03.txt'

with open(fname, 'r') as f:
    map = [line.strip() for line in f.readlines()]

SLOPE_RIGHT, SLOPE_DOWN = 3, 1

x, y = 0, 0
ntrees = 0
while y < len(map):

    location = map[y][x % len(map[y])]
    if location == '#':
        ntrees += 1

    x += SLOPE_RIGHT
    y += SLOPE_DOWN

print(ntrees)
