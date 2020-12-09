l = [int(x.strip()) for x in open('data.in').readlines()]
next(print(t := e) for i, e in enumerate(l[25:], start=25) if not any(x for x in l[i - 25: i] if e - x in l[i - 25: i]))
next(print(sum([min(e), max(e)])) for i in range(len(l) - 1) for j in range(i, len(l)) if sum(e := l[i:j + 1]) == t)
