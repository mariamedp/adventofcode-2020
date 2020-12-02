import sys

try:
	fname = sys.argv[1]
except:
	fname = 'inputs/day02.txt'

with open(fname, 'r') as f:
    passwords = [line.split(':') for line in f.readlines()]

nvalid = 0
for policy, pwd in passwords: 
    positions, letter = policy.split(' ')
    positions = [int(i) for i in positions.split('-')]
    nmatches = sum(pwd[i] == letter for i in positions) 
    if nmatches == 1:
        nvalid += 1

print(nvalid)
