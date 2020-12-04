

# fname = 'inputs/day04.test.txt'
fname = 'inputs/day04.txt'

with open(fname, 'r') as f:
    lines = [l.strip() for l in f.readlines()]


FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

nvalid = 0
passport_fields = set()
for data in lines + ['']:
    if data:
        passport_fields |= set(kvpair.split(':')[0] for kvpair in data.split(' '))
    else:
        nvalid += len(FIELDS - passport_fields) == 0
        passport_fields = set()

print(nvalid)
