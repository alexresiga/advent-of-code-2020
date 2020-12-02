lines = open('data.in').readlines()
result = 0
for line in lines:
    limits, letter, password = line.split()
    low, high = map(int, limits.split('-'))
    # result += low <= password.count(letter[0]) <= high
    result += (password[low - 1] == letter[0]) ^ (password[high - 1] == letter[0])

print(result)
