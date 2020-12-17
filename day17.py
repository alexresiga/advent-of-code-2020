from copy import deepcopy
from itertools import product


def neighbours(i, j, k, l):
    n = set()
    for x, y, z, w in product([-1, 0, 1], repeat=4):
        if x == y == z == w == 0:
            continue
        else:
            n.add((i + x, j + y, k + z, l + w))
    return n


grid = [list(x.strip()) for x in open('data.in').readlines()]
initial = set()
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == '#':
            initial.add((c, r, 0, 0))
for _ in range(6):
    min_x, max_x = min([x[0] for x in initial]) - 1, max(list([x[0] for x in initial])) + 1
    min_y, max_y = min([x[1] for x in initial]) - 1, max(list([x[1] for x in initial])) + 1
    min_z, max_z = min([x[2] for x in initial]) - 1, max(list([x[2] for x in initial])) + 1
    min_w, max_w = min([x[3] for x in initial]) - 1, max(list([x[3] for x in initial])) + 1
    new = deepcopy(initial)
    for a in range(min_x, max_x + 1):
        for b in range(min_y, max_y + 1):
            for c in range(min_z, max_z + 1):
                for d in range(min_w, max_w + 1):
                    active = [x for x in neighbours(a, b, c, d) if x in initial]
                    if (a, b, c, d) in initial:
                        if len(active) < 2 or len(active) > 3:
                            new.remove((a, b, c, d))
                    elif len(active) == 3:
                        new.add((a, b, c, d))
    initial = deepcopy(new)
print(len(new))
