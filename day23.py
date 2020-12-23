from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Node:
    val: int
    next: "Node" = None


cups = [int(x) for x in '284573961']
size = len(cups)
i = 0
for _ in range(100):
    current = cups[i]
    pick = [cups[(i + j) % size] for j in range(1, 4)]
    dest = current - 1
    while dest in pick or dest == 0:
        dest -= 1
        if dest <= 0:
            dest = max(cups)
    for p in pick:
        cups.pop(cups.index(p))
    d = cups.index(dest)
    for p in reversed(pick):
        cups.insert((d + 1) % size, p)
    i = (cups.index(current) + 1) % size

print(''.join(map(str, cups)))

MAX = 1000000
steps = 10000000
cups: List[int] = [int(x) for x in '284573961'] + list(range(10, 1000001))
lookup: Dict[int, Node] = dict()

for i in range(1, 1000000 + 1):
    lookup[i] = Node(i)

for i in range(len(cups)):
    lookup[cups[i]].next = lookup[cups[(i + 1) % len(cups)]]

cur: Node = lookup[cups[0]]

for i in range(10000000):
    if i % 100000 == 0:
        print(i)
    pick = cur.next
    cur.next = cur.next.next.next.next

    dest = cur.val

    while dest in [cur.val, pick.val, pick.next.val, pick.next.next.val]:
        dest -= 1
        if dest == 0:
            dest = MAX

    loc = lookup[dest]
    pick.next.next.next = loc.next
    loc.next = pick
    cur = cur.next
print(lookup[1].next.val * lookup[1].next.next.val)
