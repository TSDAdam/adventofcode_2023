with open('./03.in') as file:
    data = [line.strip() for line in file]

from collections import defaultdict

numbers = defaultdict(list)  # used in part 2 to track the numbers found
maxx = len(data[0])
maxy = len(data)
t = 0

# this func is run every time we see the end of a number or row


def check(data, n, y, x, t):
    global maxx, maxy, numbers, gears
    found = False  # flag to check if we've seen a symbol
    for yy in range(y - 1, y + 2):  # loop through all neighbours
        for xx in range((x - 1) - len(n), x + 1):
            if xx >= 0 and yy >= 0 and xx < maxx and yy < maxy:
                # not a number or a period - must be a symbol
                if not data[yy][xx].isnumeric() and not data[yy][xx] == '.':
                    found = True
                if data[yy][xx] == '*':  # for part 2, did we see a gear?
                    gears.add((yy, xx))  # if so, add it to a set
    if found:
        for gear in gears:
            # add the found number to the gears set
            numbers[gear].append(int(n))
        t += int(n)  # add the number to the part 1 total
        gears = set()  # reset the gears set
    return (n, t)


# part 1
for y, row in enumerate(data):
    gears = set()
    n = ''
    for x, c in enumerate(row):
        if c.isnumeric():  # if this char is a number, add it and move on
            n += c
            continue
        if n != '':  # if we don't see a number, and the current number isn't empty
            n, t = check(data, n, y, x, t)  # go and check the neighbours
            n = ''
    n, t = check(data, n, y, x, t)  # this one catches numbers on ends of rows.

print("Part 1: ", t)

p2 = 0
for k, v in numbers.items():
    if len(v) == 2:
        # get product ONLY when there are two numbers for a gear
        p2 += v[0] * v[1]
print("Part 2: ", p2)
