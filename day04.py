import re


def validate_height(inp):
    return 150 <= int(inp[:-2]) <= 193 if inp[-2:] == 'cm' else 59 <= int(inp[:-2]) <= 76


def validate_eye(inp):
    return inp in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


lines = ''.join(open('data.in').readlines()).split("\n\n")[:-1]
part1 = part2 = 0
for line in lines:
    data = re.split('[\n ]', line)
    values = dict(e.split(':') for e in data)
    if len(values.keys()) == 8 or len(values.keys()) == 7 and 'cid' not in values.keys():
        part1 += 1
        if 1920 <= int(values.get('byr', 0)) <= 2002 and \
                2010 <= int(values.get('iyr', 0)) <= 2020 and \
                2020 <= int(values.get('eyr', 0)) <= 2030 and \
                validate_height(values.get('hgt', '')) and \
                validate_eye(values.get('ecl', '')) and \
                re.match('^\d{9}$', values.get('pid', '')) and \
                re.match('^#[0-9a-f]{6}$', values.get('hcl', '')):
            part2 += 1

print(part1)
print(part2)
