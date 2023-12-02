with open('./02.in') as file:
    data = [line.strip() for line in file]
    maxr = 12  # set max values for r, g, and b for part 1.
    maxg = 13
    maxb = 14
    t = 0  # answer for part 1
    tpower = 0  # answer for part 2
    possible = True
    for row in data:
        minr, ming, minb = 0, 0, 0  # set low min values for part 2
        # these lines parse the input and cut it up
        game = row.replace(':', ';')
        gameid = int(game[5:game.find(';')])  # ""
        chunks = game.split('; ')  # ""
        for grab in chunks[1:]:
            colours = grab.split(', ')
            for colour in colours:
                numcubes = int(colour[:colour.find(' ')])
                col = colour[colour.find(' ') + 1:]
                if col == 'red':
                    # for each colour check if the number drawn is the biggest yet. If so, record it.
                    minr = max(minr, numcubes)
                    if numcubes > maxr:
                        possible = False  # checks for part 1 to see if the number of cubes exceeds the maximums
                elif col == 'green':
                    ming = max(ming, numcubes)
                    if numcubes > maxg:
                        possible = False
                elif col == 'blue':
                    minb = max(minb, numcubes)
                    if numcubes > maxb:
                        possible = False
        if possible == True:  # if the combinations were all possible for part 1, add the game id to the running total
            t += gameid
        possible = True  # and make sure the flag is reset

        # just add on the multiplied totals to the part 2 answer
        tpower += (minr * ming * minb)

print("Part 1 : ", t)

print("Part 2: ", tpower)
