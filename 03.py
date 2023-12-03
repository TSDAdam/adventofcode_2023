with open('./03.in') as file:
    data = [line.strip() for line in file]

from collections import defaultdict

numbers = defaultdict(list)
maxx = len(data[0])
maxy = len(data)
t = 0
t2 = 0


def check(data, n, y, x, t):
    global maxx, maxy, numbers, gears
    found = False
    for yy in range(y - 1, y + 2):
        for xx in range((x - 1) - len(n), x + 1):
            if xx >= 0 and yy >= 0 and xx < maxx and yy < maxy:
                # not a number or a period - must be a symbol
                if not data[yy][xx].isnumeric() and not data[yy][xx] == '.':
                    found = True
                if data[yy][xx] == '*':
                    gears.add((yy, xx))
    if found:
        for gear in gears:
            numbers[gear].append(int(n))
        t += int(n)
        gears = set()
    return (n, t)


# part 1
for y, row in enumerate(data):
    gears = set()
    n = ''
    for x, c in enumerate(row):
        if c.isnumeric():
            n += c
            continue
        if n != '':
            n, t = check(data, n, y, x, t)
            n = ''
    n, t = check(data, n, y, x, t)

print("Part 1: ", t)

p2 = 0
for k, v in numbers.items():
    if len(v) == 2:
        p2 += v[0] * v[1]
print("Part 2: ", p2)
