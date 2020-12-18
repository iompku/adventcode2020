


# using a dictionary instead
numbers = {18:0, 11:1, 9: 2, 0:3, 5:4}

# assume start with starting numbers....
i = 5
lastNum = 1
while True:
    if (lastNum in numbers):
        nextNum = i - numbers[lastNum]
    else:
        nextNum = 0

    numbers[lastNum] = i
    lastNum = nextNum
    i += 1
    if (i == 29999999):
        print(nextNum)
        #print(numbers)
        break


