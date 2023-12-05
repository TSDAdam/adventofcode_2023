from collections import defaultdict

with open('./05.in') as file:
    data = [line.strip() for line in file]
_, seednums = data[0].split(':')
seeds = [int(s) for s in seednums.strip().split()]

maps = defaultdict()

i = 2
while i < len(data):
    if len(data[i]) > 0 and data[i][-1] == ':':
        mapname = data[i][:data[i].find(' ')]
        maps[mapname] = []
        i += 1
    elif len(data[i]) > 0:
        maps[mapname].append([int(n) for n in data[i].split(' ')])
        i += 1
    else:
        i += 1

# part 1

seedlocations = []
for seed in seeds:
    for k, v in maps.items():
        for map in v:
            destination = map[0]
            source = map[1]
            r = map[2]
            if seed in range(source, source + r):
                offset = seed - source
                seed = destination + offset
                break
    seedlocations.append(seed)

print(len(seedlocations), seedlocations)
print("part 1: ", min(seedlocations))

# part 2
seedstarts = [seeds[0], seeds[2]]
seedranges = [seeds[1], seeds[3]]
seedlocations = 1000000000000
for i in range(2):
    for seed in range(seedstarts[i], seedstarts[i] + seedranges[i]):
        for k, v in maps.items():
            for map in v:
                destination = map[0]
                source = map[1]
                r = map[2]
                if seed in range(source, source + r):
                    offset = seed - source
                    seed = destination + offset
                    break
        seedlocations = min(seedlocations, seed)


print("part 2: ", seedlocations)
