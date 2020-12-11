
import string


f = open("input.txt")
valid = 0

passportDone = False
count = 0

class Node:
    def __init__(self, color):
        self.color = color
        self.contains = {}
        self.containedBy = {}

    def addToContains(self, bagColor, amount):
        if (False == self.bagAlreadyContains(bagColor)):
            self.contains[bagColor] = amount
        else:
            self.contains[bagColor] += amount

    def addToContainedBy(self, bagColor, amount):
        if (False == self.bagAlreadyContainedBy(bagColor)):
            self.containedBy[bagColor] = amount
        else:
            self.containedBy[bagColor] += amount

##    def getColor(self):
        return self.color

    def getBagsContain(self):
        return self.contains

    def getBagsContainedBy(self):
        return self.containedBy

    def bagAlreadyContains(self, bag):
        if bag in self.contains:
            return True
        else:
            return False

    def bagAlreadyContainedBy(self, bag):
        if bag in self.containedBy:
            return True
        else:
            return False

class Hashmap:
    def __init__(self):
        self.dict = {}

    def getBag(self, bagColor):
        if self.hasBag(bagColor):
            return self.dict[bagColor]
        else:
            return None

    def hasBag(self, bagColor):
        if bagColor in self.dict:
            return True
        else:
            return False

    def addBag(self, bagColor):
        if (False == self.hasBag(bagColor)):
            bag = Node(bagColor)
            self.dict[bagColor] = bag

    def addBagContains(self, bagColor, bagContains, amount):
        if (self.hasBag(bagColor)):
            self.dict[bagColor].addToContains(bagContains, amount)
            if (False == self.hasBag(bagContains)):
                self.addBag(bagContains)
            self.dict[bagContains].addToContainedBy(bagColor, amount)                


def getMoreBags(bag, listy, hashMap):
    moreBags = hashMap.getBag(bag).getBagsContainedBy()
    for b in moreBags:
        if b not in listy:
            listy.append(b)
        getMoreBags(b, listy, hashMap)

def getbagsValue(bag, hashMap):
    count = 1
    moreBags = hashMap.getBag(bag).getBagsContain()
    for b in moreBags:
        print("add " + str(moreBags[b]) + " to...")
        count += moreBags[b] * getbagsValue(b, hashMap)
    return count


#Parse the file for the needed values
hashMap = Hashmap()
for line in f:
    mainBag, containBags = line.split(" contain ")
    mainBag = mainBag[:-5] # get rid of " bags" at the end
    hashMap.addBag(mainBag)
    containBags = containBags[:-2].replace("bags", "bag") #get rid of period at the end
    containBags = containBags.split(', ')
    #print(mainBag + " contains " + str(containBags))
    for bag in containBags:
        if bag == 'no other bag':
            break
        amount = int(bag[0])
        bag = bag[2:-4] #get just the color, ditch the number and " bag"
        hashMap.addBagContains(mainBag, bag, amount)

theBags = []
shinyGold = hashMap.getBag('shiny gold')
bags = shinyGold.getBagsContain()

print(shinyGold)
print(bags)
count = 0


for b in bags:
    print("add " + str(bags[b]) + " to...")
    count += bags[b] * getbagsValue(b, hashMap)

print(count)

#this portion is for part 1
'''
print(bags)
count = len(bags)

print("amount is: " + str(count))
for bag in bags:
    if bag not in theBags:
        theBags.append(bag)
    getMoreBags(bag, theBags, hashMap)

print(theBags)
print(str(len(theBags)))
'''
    
#print(shinyGold.getBagsContain())

f.close()
