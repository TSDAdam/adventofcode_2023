with open('./04.in') as file:
    data = [line.strip() for line in file]

mycards = []
winningnums = []
cardcopies = {}  # dict for part two to keep track of how many copies of each card there is
p1 = 0
for i, row in enumerate(data):  # parse the cards
    cardcopies[i] = 1
    card, nums = row[row.find(':') + 2:].split('|')
    mycards.append([int(c) for c in card.split()])
    winningnums.append([int(n) for n in nums.split()])

# part 1
for i in range(len(mycards)):
    t = 0
    for x in mycards[i]:
        for n in winningnums[i]:
            if x == n:
                if t == 0:
                    t = 1
                else:
                    t *= 2
    p1 += t

print(p1)

# part 2
for i in range(len(mycards)):
    for _ in range(cardcopies[i]):
        t = 0
        for x in mycards[i]:  # similar to part one, just add 1 for each match
            for n in winningnums[i]:
                if x == n:
                    t += 1
        for y in range(t):  # the add 1 to each dict item for the number of matches
            cardcopies[i + y + 1] += 1


p2 = 0
for k, v in cardcopies.items():
    p2 += v

print(p2)
