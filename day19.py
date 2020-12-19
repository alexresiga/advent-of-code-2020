import re


def get_rule(rule_num):
    if rule_num == '8':
        return f"{get_rule('42')}+"
    elif rule_num == '11':
        a = get_rule('42')
        b = get_rule('31')
        return f"({'|'.join(f'{a}{{{n}}}{b}{{{n}}}' for n in range(1, 5))})"
    rule = rules[rule_num]
    if re.fullmatch(r'"."', rule):
        return rule[1]
    else:
        parts = rule.split(' | ')
        res = []
        for part in parts:
            nums = part.split(' ')
            res.append(''.join(get_rule(num) for num in nums))
        return f"({'|'.join(res)})"


rules, strings = [line.rstrip('\n') for line in open('data.in').read().split('\n\n')]
rules = dict([rule.split(': ') for rule in rules.split('\n')])
z = get_rule('0')
print(sum(bool(re.fullmatch(z, string)) for string in strings.split('\n')))
