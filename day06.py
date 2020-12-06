print(sum([len(set.union(*map(set, t.split('\n')))) for t in ''.join(open('data.in').readlines()).split("\n\n")]))
print(sum([len(set.intersection(*map(set, t.split('\n')))) for t in ''.join(open('data.in').readlines()).split('\n\n')]))
