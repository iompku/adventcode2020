

numbers = [18,11,9,0,5,1]

# assume start with starting numbers....
i = 6
lastNum = 1
while True:
    if (numbers.count(lastNum) > 1):
        #take all but literally last number entered...
        #reverse the list
        #and find the index of the "first" element
        nextNum = numbers[:-1][::-1].index(lastNum) + 1
    elif (numbers.count(lastNum) == 1):
        nextNum = 0
    else:
        print("error cannot find " + str(lastNum))

    numbers.append(nextNum)
    lastNum = nextNum
    i += 1
    if (i == 2020):
        print(nextNum)
        break
