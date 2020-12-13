from math import prod


def crt(p):
    m = 1
    for x, mx in p:
        m *= mx
    total = 0
    for x, mx in p:
        b = m // mx
        total += x * b * pow(b, mx - 2, mx)
        total %= m
    return total


with open('data.in') as f:
    t = int(f.readline())
    times = f.readline().strip().split(',')
print(prod(min(list(map(lambda x: (x, ((t // x) * x) - t) if (t // x) * x >= t else (x, ((t // x) * x + x) - t),
                        list(map(int, filter(lambda x: x != 'x', times))))), key=lambda x: x[1])))

pairs = []
for i, n in enumerate(times):
    if n == 'x':
        continue
    n = int(n)
    pairs.append((n - i, n))
print(crt(pairs))
