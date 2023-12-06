with open('./06.in') as file:
    data = [line.strip() for line in file]

timestring = " ".join(data[0].split())
times = [int(x) for x in timestring.split(':')[1].split()]

recordstring = " ".join(data[1].split())
records = [int(x) for x in recordstring.split(':')[1].split()]


def calc(times, records):
    beatenarr = []
    for n, time in enumerate(times):
        beaten = 0
        for i in range(time + 1):
            distance = (time - i) * i
            if distance > records[n]:
                beaten += 1
        beatenarr.append(beaten)
    t = 1
    for b in beatenarr:
        t *= b
    return (t)


# part 1
p1 = calc(times, records)
print(p1)

# part 2
time = [int("".join(str(x) for x in times))]
record = [int("".join(str(x) for x in records))]
p2 = calc(time, record)
print(p2)
