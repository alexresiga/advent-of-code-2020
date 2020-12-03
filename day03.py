from itertools import starmap
from math import prod

grid = [list(x.strip()) for x in open('data.in').readlines()]


def trajectory(a, b):
    result = 0
    i = j = 0
    while i < len(grid):
        if grid[i][j] == '#':
            result += 1
        j = (j + b) % len(grid[i])
        i += a
    return result


print(prod(starmap(trajectory, [(1, 3)])))
print(prod(starmap(trajectory, [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)])))
