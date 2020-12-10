from collections import defaultdict

lines = [int(x.strip()) for x in open('data.in').readlines()]
a = [0] + sorted(lines) + [max(lines) + 3]
diff = defaultdict(int)
for i in range(len(a) - 1):
    diff[a[i + 1] - a[i]] += 1
print(diff[1] * diff[3])

ways = [1] + [0] * (sorted(lines)[-1])
for n in sorted(lines):
    ways[n] = ways[n - 3] + ways[n - 2] + ways[n - 1]
print(ways[-1])
