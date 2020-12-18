



# create an array of 100,000 ints, initialized to 0
mem = [0] * 100000 #68719476736 36 bits technically
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
mask0upper = 262143 #binary 111111111111111111
mask0lower = 262143
mask1upper = 0
mask1lower = 0

def updateMemory(address, value):
    #need to examine mask first
    global mask0upper
    global mask0lower
    global mask1upper
    global mask1lower
    
    mem[address] = value
    mem[address] |= (mask1upper << 18)
    mem[address] |= mask1lower
    mem[address] &= ((mask0upper << 18) | mask0lower) #might not work in 32 bit

    

def updateMask(newMask):
    global mask0upper
    global mask0lower
    global mask1upper
    global mask1lower
    i = 17
    for c in newMask[0:18]:
        if (c == '1'):
            mask0upper = mask0upper | (1 << i)
            mask1upper = mask1upper | (1 << i)
        elif (c == '0'):
            mask0upper = mask0upper & (~(1 << i))
            mask1upper = mask1upper & (~(1 << i))
        elif (c == 'X'):
            mask0upper = mask0upper | (1 << i)
            mask1upper = mask1upper & (~(1 << i))
        else:
            print("Error, unexpected character in newMask at "+str(i+18)+": " + c)
        i -= 1
            
    i = 17
    for c in newMask[18:]:
        if (c == '1'):
            mask0lower = mask0lower | (1 << i)
            mask1lower = mask1lower | (1 << i)
        elif (c == '0'):
            mask0lower = mask0lower & (~(1 << i))
            mask1lower = mask1lower & (~(1 << i))
        elif (c == 'X'):
            mask0lower = mask0lower | (1 << i)
            mask1lower = mask1lower & (~(1 << i))
        else:
            print("Error, unexpected character in newMask at "+str(i)+": " + c)
        i -= 1
    mask = newMask #not really needed other than debugging


f = open("input.txt")

for line in f:
    if (line[0:3] == "mem"):
        #print("Mem")
        address = int(line.split('[')[1].split(']')[0])
        value = int(line.split('= ')[1].strip())
        updateMemory(address, value)
        
        
    elif (line[0:4] == "mask"):
        #print("mask")
        newMask = line.split('= ')[1].strip()
        updateMask(newMask)
    else:
        print("Error, unexpected line reading file: " + line)


#get sum of all values current in memory
accumulator = 0
for m in mem:
    accumulator += m

print(accumulator)

f.close()
