with open('./01.in') as file:
    data = [line.strip() for line in file]


def reduce(s):  # used in part two
    global done
    numbers = ['zero', 'one', 'two', 'three', 'four',
               'five', 'six', 'seven', 'eight', 'nine']
    for i, c in enumerate(s):
        for number in numbers:
            # for each character in the string, check to see if it matches the starting letter of a written number.
            if c == number[0]:
                # if it does match, check forwards the number of characters to see if matches the whole word.
                if s[i:i + len(number)] == number:
                    s = s.replace(
                        number, (number[0] + str(numbers.index(number)) + number[-1]))  # replace the written number with a combination of the first and last chars of the word
                    # and put the number in the middle. Accounts for shared letters.
                    return s
    # if the function gets this far, it didn't fine a match. This flag tells the original loop to stop.
    done = True
    return s


# function to grab the first and last digits from a string.
def getNumbers(rows):
    nums = []
    for row in rows:
        alldigits = ''
        digits = ''
        for c in row:
            if c.isnumeric():  # if the current character is a digit
                alldigits += c  # add it to a string of found numbers
        # grab the first and last found numbers
        digits = alldigits[0] + alldigits[-1]
        nums.append(int(digits))  # add the integer values to a list of values
    print(sum(nums))  # print the sum of the values - the answer
    return


# part 1 answer
getNumbers(data)

done = False
newrows = []
for row in data:
    s = row
    while done == False:  # keep passing the current row to the reduce function to replace words with digits
        s = reduce(s)
    newrows.append(s)  # when it's reduced, add it to a list
    done = False

# part 2 answer
getNumbers(newrows)
