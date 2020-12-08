lines = [x.strip() for x in open('data.in').readlines()]
exp = 0
while True:
    acc = jmp_count = loop = 0
    seen = set()
    i = 0
    while i < len(lines):
        if i in seen:
            loop = 1
            break
        seen.add(i)
        instr, arg = lines[i].split(' ')
        if instr == 'jmp':
            jmp_count += 1
            if jmp_count == exp:
                i += 1
            else:
                i += int(arg)
        elif instr == 'acc':
            acc += int(arg)
            i += 1
        else:
            i += 1

    if not loop:
        print(acc)
        break

    exp += 1
