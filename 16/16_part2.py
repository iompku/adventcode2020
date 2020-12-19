

f = open("input.txt")

rules = {}
ruleNames = []
allValidNumbers = []
valids = []
#There are 20 different categories
for i in range(0,20):
    category = []
    valids.append(category)

#print(len(valids))

# First read in the rules for valid input
for line in f:
    if line == '\n':
        break

    i = 0
    ruleName = line.split(": ")[0]
    ruleNames.append(ruleName)
    ruleRange = line.split(": ")[1].strip()
    rules[ruleName] = ruleRange
    r1 = ruleRange.split(" or ")[0]
    r1a = int(r1.split('-')[0])
    r1b = int(r1.split('-')[1])
    for i in range(r1a, r1b):
        if i not in allValidNumbers:
            allValidNumbers.append(i)
    r2 = ruleRange.split(" or ")[1].strip()
    r1a = int(r2.split('-')[0])
    r1b = int(r2.split('-')[1])
    for i in range(r1a, r1b):
        if i not in allValidNumbers:
            allValidNumbers.append(i)
    
#print(allValidNumbers)
#print(rules)
print(ruleNames)
myTicket = []

invalidNums = []
# do the tickets
skip = True
getnext = False
for line in f:
    if (getnext):
        myTicket = line.strip().split(',')
        getnext = False
    elif (skip):
        if "your ticket:" in line:
            getnext = True
        if "nearby tickets:" not in line:
            continue
        else:
            skip = False
            continue

    ticketValid = True
    nums = line.strip().split(',')
    for n in nums:
        if int(n) not in allValidNumbers:
            #print(n + " not valid")
            ticketValid = False
            break
    if (ticketValid):
        category = 0
        # insert into sorted categories
        for n in nums:
            valids[category].append(int(n))
            category += 1
        

# print categories
#print("Printing categories..")
i = 0
catsPossible = []
for c in valids:
    #print(sorted(c))
    valids[i] = sorted(c)

    # TODO: determine which rule sets are valid and invalid for this category
    # There are 20 categories, start with all 20 being a possibility
    possibility = [True] * 20
    pobI = 0
    for ruleRange in rules.values():
        r1 = ruleRange.split(" or ")[0]
        r1a = int(r1.split('-')[0])
        r1b = int(r1.split('-')[1])+1
        r1 = ruleRange.split(" or ")[1]
        r2a = int(r1.split('-')[0])
        r2b = int(r1.split('-')[1])+1
        for number in c:
            if (number not in range(r1a,r1b)) and (number not in range(r2a,r2b)):
                possibility[pobI] = False
                #if (i == 12):
                
                    #print("Number " + str(number) + " not found in category " +
                    #      str(i) + " range " + ruleRange + " " + str(r1a)  + "-" + str(r1b)
                    #       + " " + str(r2a) + "-" + str(r2b))
                break
        pobI += 1
        
        #range1 = rules
        r1 = 1
        #if number not in range()
    catsPossible.append(possibility)
    
    #print(len(valids[i]))
    i += 1

# We have narrowed down a large truth table at this point, we just need to
# figure out where they all fit together
#catsPossible.sort()
myTicketFullInfo = {}
claimed = [False] * 20
for cat in sorted(catsPossible):
    
    # This is the index of the next category in line to pick which rule description it gets
    # catsPossible.index(cat)
    # This is the column of numbers that contain one allowalbe Truth

    #get next true that hasn't already been claimed
    i = 0
    
    while True:
        testIndex = cat.index(True)
        if (claimed[testIndex] == True):
            #keep looking
            cat[testIndex] = False
            continue
        else:
            # claim it
            myTicketFullInfo[ruleNames[testIndex]] = int(myTicket[int(catsPossible.index(cat))])
            claimed[testIndex] = True
            print("claiming column " + str(testIndex) + " for " + ruleNames[testIndex])
            break
        i += 1
print(myTicketFullInfo)
    

accumulator = 1
for key in myTicketFullInfo.keys():
    if 'departure' in key:
        accumulator *= myTicketFullInfo[key]

print(accumulator)




f.close()
