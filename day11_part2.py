
# fname = 'inputs/day11.test.txt'
fname = 'inputs/day11.txt'

with open(fname, 'r') as f:
    map = [list(line.strip()) for line in f.readlines()]

map_width = len(map[0])
map_height = len(map)


seats = [(i,j) for i in range(map_width) for j in range(map_height) if map[j][i] != '.']

def find_seats_adjacent(i, j):
    adjseats = []
    for (x, y) in [(0,1), (1,0), (1,1), (1,-1)]:
        candidate_seats = [s for s in seats if (s[0] - i)*x - (s[1] - j)*y == 0 if s != (i, j)]
        dist = {s: (s[0]-i)*y + (s[1]-j)*x for s in candidate_seats}
        seats_left = [s for s in candidate_seats if dist[s] < 0]
        seats_right = [s for s in candidate_seats if dist[s] > 0]
        if seats_left:
            adjseats.append(max(seats_left, key=lambda s: dist[s]))
        if seats_right:
            adjseats.append(min(seats_right, key=lambda s: dist[s]))
    return adjseats

seats_adjacent = {s: find_seats_adjacent(s[0], s[1]) for s in seats}


changes_to_occuppied = seats
changes_to_empty = []
while changes_to_occuppied or changes_to_empty:

    for i,j in changes_to_occuppied:
        map[j][i] = '#'
    for i,j in changes_to_empty:
        map[j][i] = 'L'
    changes_to_occuppied, changes_to_empty = [], []

    for i,j in seats:
        noccupied = sum(map[v][u] == '#' for u,v in seats_adjacent[(i,j)])
        if noccupied == 0 and map[j][i] == 'L':
            changes_to_occuppied.append((i,j))
        elif noccupied >= 5 and map[j][i] == '#':
            changes_to_empty.append((i,j))

print(sum(map[j][i] == '#' for i,j in seats))
