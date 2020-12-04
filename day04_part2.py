import re


# fname = 'inputs/day04.test.invalid.txt'
# fname = 'inputs/day04.test.valid.txt'
fname = 'inputs/day04.txt'

with open(fname, 'r') as f:
    lines = [l.strip() for l in f.readlines()]


FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

VALIDATORS = {
    'byr': lambda x: (len(x) == 4) & (1920 <= int(x) <= 2002),
    'iyr': lambda x: (len(x) == 4) & (2010 <= int(x) <= 2020),
    'eyr': lambda x: (len(x) == 4) & (2020 <= int(x) <= 2030),
    'hgt': lambda x: ((x[-2:] == 'cm') & (150 <= int(x[:-2]) <= 193)) | ((x[-2:] == 'in') & (59 <= int(x[:-2]) <= 76)),
    'hcl': lambda x: re.fullmatch('#[0-9a-f]{6}', x),
    'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda x: re.fullmatch('[0-9]{9}', x),
    'cid': lambda x: True
}

def is_valid(field, value):
    try:
        return VALIDATORS[field](value)
    except:
        return False

nvalid = 0
passport_fields = {}
for data in lines + ['']:
    if data:
        passport_fields.update(dict(kvpair.split(':') for kvpair in data.split(' ')))
    else:
        passport_valid = all(k in passport_fields for k in FIELDS) & all(is_valid(k, v) for k,v in passport_fields.items())
        nvalid += passport_valid
        passport_fields = {}

print(nvalid)
