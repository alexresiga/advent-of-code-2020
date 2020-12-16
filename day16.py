import re

groups = ''.join(open('data.in').readlines()).split("\n\n")[:-1]
rules = re.findall('(.+): (.+)-(.+) or (.+)-(.+)\n', groups[0])
rules = {name: [range(int(a), int(b) + 1), range(int(c), int(d) + 1)] for name, a, b, c, d in rules}
tickets = [list(map(int, line.split(','))) for line in groups[2].split('\n')[1:]]
part1 = sum(n for t in tickets for n in t if not any(n in rule[0] or n in rule[1] for rule in rules.values()))

part2, used = 1, set()
mine = [list(map(int, line.split(','))) for line in groups[1].split('\n')[1:]][0]
valid = [t for t in tickets if all(any(n in rule[0] or n in rule[1] for rule in rules.values()) for n in t)]
possible = {n: {j for j in range(20) if all((v[j] in r[0] or v[j] in r[1]) for v in valid)} for n, r in rules.items()}
for p in sorted(possible, key=lambda l: len(possible[l])):
    if p.startswith('departure'):
        part2 *= mine[(possible[p] - used).pop()]
    used.update(possible[p])

print(f'{part1}\n{part2}')
