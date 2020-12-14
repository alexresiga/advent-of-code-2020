import re


def modify_bit(n, _p, b):
    _mask = 1 << _p
    return (n & ~_mask) | ((b << _p) & _mask)


def indices(new_idx, floating):
    if len(floating) == 0:
        return [new_idx]
    else:
        b0 = floating[0]
        rest = floating[1:]
        ans = indices(new_idx, rest) + indices(new_idx + 2 ** b0, rest)
        return ans


def modify_value(_value, _mask):
    new_value = 0
    for ii, bit in enumerate(reversed(_mask)):
        if bit == 'X':
            new_value += (_value & (2 ** ii))
        elif bit == '1':
            new_value += 2 ** ii
        elif bit == '0':
            pass
        else:
            assert False
    return new_value


def modify_idx(_index, _mask):
    new_idx = 0
    floating = []
    for ii, bit in enumerate(reversed(_mask)):
        i_bit = _index & (2 ** ii)
        if bit == 'X':
            floating.append(ii)
        elif bit == '1':
            new_idx += 2 ** ii
        elif bit == '0':
            new_idx += i_bit
            pass
        else:
            assert False
    return indices(new_idx, floating)


lines = [x.strip() for x in open('data.in').readlines()]
positions = []
mask = 0
mem = {}
for line in lines:
    if line.startswith('mask'):
        positions = []
        for i, a in enumerate(line.split(' = ')[1]):
            if a != 'X':
                positions.append((35 - i, int(a)))
    else:
        a = list(map(int, re.findall('\d+', line)))
        x = a[1]
        for p in positions:
            x = modify_bit(x, p[0], p[1])
        mem[a[0]] = x

print(sum(mem.values()))
mask = ''
mem = {}
for line in lines:
    line = line.strip()
    if line.startswith('mask'):
        mask = line.split()[-1]
    else:
        assert len(mask) == 36
        idx, _, value = line.split()
        idx = int(idx.split('[')[-1][:-1])
        value = int(value)
        a = modify_idx(idx, mask)
        for idx2 in a:
            mem[idx2] = value

print(sum(mem.values()))
