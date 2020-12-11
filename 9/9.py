
import string


f = open("input.txt")
valid = 0

#File is just a punch of ints, easy peasy  

preamble = []
i = 0
badLine = -1
magicNumber = 57195069
summ = 0

# parse input file, add line number, instruction, and number to a code list 
for line in f:
    line = int(line.strip())
    if (i < 25):
        preamble.append(line)
        i += 1
        continue
    preamble.append(line)
    summ = 0
    for num in preamble:
        summ += num
    if (summ == magicNumber):
        print("We did it!")
        break
    elif (summ > magicNumber):
        #too many, need to start deleting
        while (summ > magicNumber):
            del preamble[0]
            summ = 0
            for num in preamble:
                summ += num
        if (summ == magicNumber):
            print("We did it!")
            break

    i += 1
    #print(preamble)

print(preamble)
    
    #This section was for part 1
'''
    #First determine if this next line is valid or not
    
    #print(preamble)
    validFound = False
    for item in preamble:
        j = 0
        if (validFound == False):
            while (j < 25):
                if (preamble[j] == item):
                    j+=1
                    continue
                elif ((preamble[j] + item) == line):
                    validFound = True
                    break
                j += 1

    if(validFound == False):
        badLine = line
        break
    
    # update preamble
    del preamble[0]
    preamble.append(line)
    i += 1
    '''
print("Length = " + str(len(preamble)) + " at index " + str(i))

preamble.sort()
print("Smallest = " + str(preamble[0]) + " biggest = " + str(preamble[-1]))
print("sum = " + str(preamble[0] + preamble[-1]))

    
f.close()
