card, door = list(map(int, open('data.in').readlines()))
x = 0
while pow(7, x, 20201227) != card:
    x += 1
print(pow(door, x, 20201227))
