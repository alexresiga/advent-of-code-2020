import re
from collections import defaultdict
from functools import reduce


def size(bag):
    return reduce(lambda x, y: x + y, [int(x) * size(y) for x, y in n[bag]], 1)


lines = open('data.in').readlines()
n = defaultdict(list)
p = defaultdict(list)
for line in lines:
    tmp = line.split(' ')
    key = f'{tmp[0]} {tmp[1]}'
    values = re.findall('(\d) ([a-z ]*) bag', line)
    for v in values:
        n[key].append(v)
        p[v[1]].append(key)

seen = set()
stack = ['shiny gold']
while stack:
    top = stack.pop()
    seen.add(top)
    for t in p[top]:
        stack.append(t)

print(len(seen) - 1)
print(size('shiny gold') - 1)
