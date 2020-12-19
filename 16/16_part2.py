# Not done yet, see TODO

f = open("input.txt")

rules = {}
allValidNumbers = []
valids = []
#There are 20 different categories
for i in range(0,20):
    category = []
    valids.append(category)

print(len(valids))


# First read in the rules for valid input
for line in f:
    if line == '\n':
        break

    i = 0
    ruleName = line.split(": ")[0]
    ruleRange = line.split(": ")[1]
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

invalidNums = []
# do the tickets
skip = True
for line in f:
    if (skip):
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
for c in valids:
    #print(sorted(c))
    valids[i] = sorted(c)

    # TODO: determine which rule sets are valid and invalid for this category
    
    #print(len(valids[i]))
    i += 1



#get sum of all values current in memory

accumulator = 0
for i in invalidNums:
    accumulator += i

print(accumulator)


f.close()
