lines = [(x[0], int(x.strip()[1:])) for x in open('data.in').readlines()]
dirs = {'E': (0, 1), 'S': (-1, 0), 'W': (0, -1), 'N': (1, 0)}
y = x = facing = 0
# part 1
for line in lines:
    if line[0] == 'F':
        y += list(dirs.values())[facing][0] * line[1]
        x += list(dirs.values())[facing][1] * line[1]
    if line[0] in 'NESW':
        y += dirs[line[0]][0] * line[1]
        x += dirs[line[0]][1] * line[1]
    if line[0] in 'LR':
        facing = (facing + line[1] // 90) % 4 if line[0] == 'R' else (facing - line[1] // 90) % 4
print(abs(x) + abs(y))
# part 2
yw, xw = 1, 10
y, x = 0, 0
for line in lines:
    if line[0] == 'F':
        y += yw * line[1]
        x += xw * line[1]
    if line[0] in 'NESW':
        yw += dirs[line[0]][0] * line[1]
        xw += dirs[line[0]][1] * line[1]
    if line[0] in 'LR':
        for _ in range(line[1] // 90):
            (yw, xw) = (-xw, yw) if line[0] == 'R' else (xw, -yw)

print(abs(x) + abs(y))
