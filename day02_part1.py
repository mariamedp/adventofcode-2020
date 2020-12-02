import sys

try:
	fname = sys.argv[1]
except:
	fname = 'inputs/day02.txt'

with open(fname, 'r') as f:
    passwords = [line.split(':') for line in f.readlines()]

nvalid = 0
for policy, pwd in passwords: 
    times, letter = policy.split(' ')
    mincount, maxcount = [int(n) for n in times.split('-')]
    if mincount <= pwd.count(letter) <= maxcount:
        nvalid += 1

print(nvalid)
