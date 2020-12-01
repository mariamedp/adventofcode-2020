import sys

try:
	fname = sys.argv[1]
except:
	fname = 'inputs/day01.txt'

with open(fname, 'r') as f:
    numbers = [int(n.strip()) for n in f.readlines()]

remaindersum = [2020 - n for n in numbers]

for i in range(len(numbers)):
    
    remainder = [remaindersum[i] - n for n in numbers]
    
    for j in range(i, len(numbers)):
    
        try:
            numbers.index(remainder[j])
            print(remainder[j] * (remaindersum[i] - remainder[j]) * numbers[i])
            break
        except:
            pass
   
