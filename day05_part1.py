

# fname = 'inputs/day05.test.txt'
fname = 'inputs/day05.txt'

with open(fname, 'r') as f:
    lines = [l.strip() for l in f.readlines()]

row_numbers = [int(l[:-3].replace('F', '0').replace('B', '1'), 2) for l in lines]
column_numbers = [int(l[-3:].replace('L', '0').replace('R', '1'), 2) for l in lines]
seat_ids = [r*8 + c for r,c in zip(row_numbers, column_numbers)]

print(max(seat_ids))
