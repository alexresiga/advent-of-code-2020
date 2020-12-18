import re


class A(int):
    def __mul__(self, b):
        return A(int(self) + b)

    def __add__(self, b):
        return A(int(self) + b)

    def __sub__(self, b):
        return A(int(self) * b)


def ev(expr, part2=False):
    expr = re.sub(r"(\d+)", r"a(\1)", expr)
    expr = expr.replace("*", "-")
    if part2:
        expr = expr.replace("+", "*")
    return eval(expr, {}, {"a": A})


lines = [x.strip() for x in open('data.in').readlines()]
print("part 1:", sum(ev(line) for line in lines))
print("part 2:", sum(ev(line, part2=True) for line in lines))
