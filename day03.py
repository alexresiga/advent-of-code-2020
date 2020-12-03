from itertools import starmap
from math import prod

grid = [list(x.strip()) for x in open('data.in').readlines()]
for line in grid:
    line.extend(line * len(grid))


def trajectory(a, b):
    result = 0
    i = j = 0

    while i < len(grid) and j < len(grid[i]):
        if i < len(grid) and j < len(grid[i]) and grid[i][j] == '#':
            result += 1
        i += a
        j += b
    return result


print(prod(starmap(trajectory, [(1, 3)])))
print(prod(starmap(trajectory, [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)])))
