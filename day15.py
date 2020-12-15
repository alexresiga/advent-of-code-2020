lines = [int(x) for x in open('data.in').readline().strip().split(',')]
d = {n: i for i, n in enumerate(lines[:-1])}
n = lines[-1]
for i in range(len(lines), 30000000):
    if n in d:
        new = i - d[n] - 1
    else:
        new = 0
    if i == 2020:
        print(n)
    d[n] = i - 1
    n = new
print(n)
