from collections import defaultdict

with open('./07.ex') as file:
    data = [line.strip() for line in file]
hands = {}
types = []
ranks = '123456789TJQKA'
for row in data:
    hand, bid = row.split(' ')
    hands[hand] = int(bid)

# types: 5 of a kind, 4 of a kind, full house, three of a kind, two pair, one pair, high card

for hand, bid in hands.items():
    counts = defaultdict(int)
    for c in hand:
        counts[c] += 1
    if 5 in counts.values():  # 5 of a kind
        types.append((hand, 0))
    elif 4 in counts.values():  # 4 of a kind
        types.append((hand, 1))
    elif 3 in counts.values() and 2 in counts.values():  # full house
        types.append((hand, 2))
    elif 3 in counts.values():  # 3 of a kind
        types.append((hand, 3))
    elif sum(1 for v in counts.values() if v == 2) == 2:  # check for two pairs
        types.append((hand, 4))
    elif 2 in counts.values():  # check for one pair
        types.append((hand, 5))
    else:  # high card is only option left
        types.append((hand, 6))

types = sorted(types, key=lambda item: item[1], reverse=True)


def sortthem():
    madeaswap = False
    global types
    global ranks
    for i in range(len(types) - 1):
        if types[i][1] == types[i+1][1] and types[i][1] < 6:
            # print("comparing ", types[i][0], " and ", types[i+1][0])
            for x in range(len(types[i][0])):
                thishandchar = ranks.find(types[i][0][x])
                nexthandchar = ranks.find(types[i+1][0][x])
                # print("comparing ", types[i][0][x], " to ", types[i+1][0][x])
                if thishandchar == nexthandchar:
                    continue
                if nexthandchar < thishandchar:
                    types[i], types[i+1] = types[i+1], types[i]
                    madeaswap = True
                    break
                else:
                    break
    return madeaswap


madeaswap = True
while madeaswap == True:
    madeaswap = sortthem()


print(types)
t = 0
for i in range(len(hands)):
    t += ((i+1) * hands[types[i][0]])

print(t)
