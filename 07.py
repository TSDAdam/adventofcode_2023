from collections import defaultdict

with open('./07.ex') as file:
    data = [line.strip() for line in file]
hands = {}
types = {}
for row in data:
    hand, bid = row.split(' ')
    hands[hand] = int(bid)

# types: 5 of a kind, 4 of a kind, full house, three of a kind, two pair, one pair, high card

for hand, bid in hands.items():
    counts = defaultdict(int)
    for c in hand:
        counts[c] += 1
    if 5 in counts.values():  # 5 of a kind
        types[hand] = 0
    elif 4 in counts.values():  # 4 of a kind
        types[hand] = 1
    elif 3 in counts.values() and 2 in counts.values():  # full house
        types[hand] = 2
    elif 3 in counts.values():  # 3 of a kind
        types[hand] = 3
