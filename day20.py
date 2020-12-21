import re
from math import prod


def get_borders(image):
    b = [
        image[0],
        image[-1],
        "".join([line[0] for line in image]),
        "".join([line[-1] for line in image])
    ]
    return b + [b[::-1] for b in b]


def pretty_print(array_2d):
    print('\n' + '\n'.join([''.join(a) for a in array_2d]) + '\n')


def intersect(a, b):
    return len([i for j in b for i in a if i == j])


lines = [line.rstrip('\n') for line in open('data.in').read().split('\n\n')]
tiles = {}
for line in lines:
    line = line.split('\n')
    tiles[int(re.findall('\d+', line[0])[0])] = line[1:]

borders = {i: get_borders(t) for i, t in tiles.items()}
shared = {k: sum(intersect(borders[k], borders[p]) for p in tiles if k != p) // 2 for k in tiles}
corners = [i for i in tiles if shared[i] == 2]

print(prod(corners))
