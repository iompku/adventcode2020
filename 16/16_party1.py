

f = open("input.txt")

rules = {}
allValidNumbers = []

# First read in the rules for valid input
for line in f:
    if line == '\n':
        break
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

    nums = line.strip().split(',')
    for n in nums:
        if int(n) not in allValidNumbers:
            print(n + " not valid")
            invalidNums.append(int(n))

#get sum of all invalid numbers
accumulator = 0
for i in invalidNums:
    accumulator += i

print(accumulator)


f.close()
