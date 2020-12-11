
import string


f = open("input.txt")
valid = 0

code = []
i = 0

# parse input file, add line number, instruction, and number to a code list 
for line in f:
    list = [i]
    list2 = line.split(' ')
    list.append(list2[0])
    list.append(int(list2[1].strip()))
    code.append(list)
    i += 1

#print(code)

#run the code, and keep track of every line ran
lineRan = []
redone = -1
acc = 0
line = []
codeLine = 0
lastLine = -1
old = ''
finished = False
linetoswap = -1

# this outer loop is part 2, testing every line of code that is nop
# or jmp and swapping it to the other to see if we can make it to the end
for test in code:
    if (finished): #quit testing if we found the swap that works
        break
    if (test[1] == 'nop'):
        #print("Trying line " + str(test[0]))
        old = 'nop'
        code[test[0]][1] = 'jmp'
    elif (test[1] == 'jmp'):
        #print("Trying line " + str(test[0]))
        old = 'jmp'
        code[test[0]][1] = 'nop'
    else: # not swapping acc commands
        continue

    # important to reset these each time    
    codeLine = 0
    acc = 0
    lineRan = []
    # run the code
    while (True):
        line = code[codeLine]
        if line[0] in lineRan:
            redone = line[0]
            break
        lineRan.append(line[0])
        if (codeLine == 627): #we made it to the final line of code
            print("Done!")
            finished = True
            linetoswap = test[0]
            break
        elif(line[1] == 'acc'):
            acc += line[2]
            codeLine += 1
            #print(line, end=' ')
            #print("acc = " + str(acc))
        elif(line[1] == 'jmp'):
            lastLine = codeLine
            codeLine += line[2]
            #print(line, end=' ')
            #print('jmp to line ' + str(codeLine))
        elif(line[1] == 'nop'):
            lastLine = codeLine
            codeLine += 1

    # put code back to the way it was before        
    if (old == 'nop'):
        code[test[0]][1] = 'nop'
    elif (old == 'jmp'):
        code[test[0]][1] = 'jmp'
        

#print(redone)
print("Acc = " + str(acc))
print("Line to swap: " + str(linetoswap))
#print(lastLine)
    

f.close()
