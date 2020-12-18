



# create an array of 100,000 ints, initialized to 0
#mem = [0] * 100000 #68719476736 36 bits technically
# changing to a map, not going to use all those values anyways
mem = {}

mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def updateMemory(address, value):
    decodeAddressAndWrite(address, value)
    

def updateMask(newMask):
    global mask
    mask = newMask

def find(string, char):
    return [i for i, ltr in enumerate(string) if ltr == char]

def decodeAddressAndWrite(address, value):
    global mask

    tempAddress = ''
    i = 35
    for c in mask:
        # if it is a number, either allow address to pass (0 | address) or force it to be a one (1 | anything)
        if ((c == '1') or (c == '0')):
            tempAddress = tempAddress + str(int(c) | int((address/(2**i)%2))) #index inde binary space
        elif (c == 'X'):
            tempAddress = tempAddress + 'X'
        else:
            print("Error, unexpected character in newMask at "+str(i)+": " + c)
        i -= 1
            
    xs = find(tempAddress, 'X') #create list of all indexes X is at

    # Create a value that represents all 1s in binary for the amount of Xs
    updateXValues = 2**len(xs) - 1
    # Create all addresses with 0 and 1 combinations for Xs and write values
    while (updateXValues >= 0):
        i = 0
        newAddress = list(tempAddress)
        while i < len(xs):
            newAddress[xs[i]] = str(int((updateXValues/(2**i)%2)))
            i += 1
        #converting from list of string chars, to string, to an int from base 2 binary
        addr = int("".join(newAddress), 2)
        #add to dictionary
        mem[addr] = value
        updateXValues -= 1
    


f = open("input.txt")

for line in f:
    if (line[0:3] == "mem"):
        address = int(line.split('[')[1].split(']')[0])
        value = int(line.split('= ')[1].strip())
        updateMemory(address, value)
        
        
    elif (line[0:4] == "mask"):
        newMask = line.split('= ')[1].strip()
        updateMask(newMask)
    else:
        print("Error, unexpected line reading file: " + line)


#get sum of all values current in memory
accumulator = 0
for m in mem:
    accumulator += mem[m]

print(accumulator)

f.close()
