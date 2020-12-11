
# fname = 'inputs/day11.test.txt'
fname = 'inputs/day11.txt'

with open(fname, 'r') as f:
    map = [list(line.strip()) for line in f.readlines()]

map_width = len(map[0])
map_height = len(map)

seats = [(i,j) for i in range(map_width) for j in range(map_height) if map[j][i] != '.']

def seats_adjacent()
changes_to_occuppied = seats
changes_to_empty = []
while changes_to_occuppied or changes_to_empty:

    for i,j in changes_to_occuppied:
        map[j][i] = '#'
    for i,j in changes_to_empty:
        map[j][i] = 'L'
    changes_to_occuppied, changes_to_empty = [], []

    for i,j in seats:

        seats_adjacent = 

        noccupied = sum(map[v][u] == '#' 
                        for u in (i-1, i, i+1) for v in (j-1, j, j+1) 
                        if (u,v) != (i,j) and 0 <= u < map_width and 0 <= v < map_height)
        if noccupied == 0 and map[j][i] == 'L':
            changes_to_occuppied.append((i,j))
        elif noccupied >= 4 and map[j][i] == '#':
            changes_to_empty.append((i,j))

print(sum(map[j][i] == '#' for i,j in seats))
