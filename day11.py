from copy import deepcopy


def change(i, j):
    taken = 0
    for d in dirs:
        ii = i + d[0]
        jj = j + d[1]
        while 0 <= ii < len(grid) and 0 <= jj < len(grid[ii]) and grid[ii][jj] == '.':
            ii += d[0]
            jj += d[1]
        if 0 <= ii < len(grid) and 0 <= jj < len(grid[ii]) and grid[ii][jj] == '#':
            taken += 1

    if grid[i][j] == 'L' and taken == 0:
        new[i][j] = '#'
    elif grid[i][j] == '#' and taken >= 5:  # 4
        new[i][j] = 'L'


grid = [list(x.strip()) for x in open('data.in').readlines()]
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
new = deepcopy(grid)
while True:
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            change(y, x)
    if new == grid:
        print(sum(line.count('#') for line in grid))
        break
    grid = deepcopy(new)
    new = deepcopy(grid)
