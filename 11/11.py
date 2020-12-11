
import string

def arrayV(char):
    if ('#' == char):
        return 1
    return 0

def calcValuePart1(array, i, j):
    sum = 0
    #corner cases, don't want to index outside array
    #top...
    if (i != 0):
        #left
        if (j != 0):
            sum += arrayV(array[i-1][j-1])
        # middle
        sum += arrayV(array[i-1][j])
        #right
        if (j != (len(array[0])-1)):
            sum += arrayV(array[i-1][j+1])

    #middle left
    if (j != 0):
        sum += arrayV(array[i][j-1])

    #middle right
    if (j != (len(array[0])-1)):
        sum += arrayV(array[i][j+1])

    #bottom...
    if (i != (len(array)-1)):
        #left
        if (j != 0):
            sum += arrayV(array[i+1][j-1])
        #middle
        sum += arrayV(array[i+1][j])
        #right
        if (j != (len(array[0])-1)):
            sum += arrayV(array[i+1][j+1])

    return sum

#Part 2
def calcValue(array, indexI, indexJ):
    sum = 0
    i = indexI
    j = indexJ
    #corner cases, don't want to index outside array
    #top left
    while ((i != 0) and (j != 0)):
        #sum += arrayV(array[i-1][j-1])
        if (array[i-1][j-1] == 'L'):
            break
        elif (array[i-1][j-1] == '#'):
            sum += 1
            break
        i -= 1
        j -= 1
    
    i = indexI
    j = indexJ
    
    # top middle
    while (i != 0):
        #sum += arrayV(array[i-1][j])
        if (array[i-1][j] == 'L'):
            break
        elif (array[i-1][j] == '#'):
            sum += 1
            break
        i -= 1

    i = indexI    
    # topright
    while ((i != 0) and (j != (len(array[0])-1))):
        #sum += arrayV(array[i-1][j+1])
        if (array[i-1][j+1] == 'L'):
            break
        elif (array[i-1][j+1] == '#'):
            sum += 1
            break
        i -= 1
        j += 1

    i = indexI
    j = indexJ
    #middle left
    while (j != 0):
        #sum += arrayV(array[i][j-1])
        if(array[i][j-1] == 'L'):
            break
        elif(array[i][j-1] == '#'):
            sum += 1
            break
        j -= 1

    j = indexJ
    #middle right
    while (j != (len(array[0])-1)):
        #sum += arrayV(array[i][j+1])
        if (array[i][j+1] == 'L'):
            break
        elif (array[i][j+1] == '#'):
            sum += 1
            break
        j += 1

    j = indexJ
    #bottom left
    while ((i != (len(array)-1)) and (j != 0)):
        if (array[i+1][j-1] == 'L'):
            break
        elif (array[i+1][j-1] == '#'):
            sum += 1
            break
        i += 1
        j -= 1

    i = indexI
    j = indexJ
    #bottom middle
    while (i != (len(array)-1)):
        #sum += arrayV(array[i+1][j])
        if (array[i+1][j] == 'L'):
           break
        elif (array[i+1][j] == '#'):
           sum += 1
           break
        i += 1

    i = indexI       
    #bottom right
    while ((i != (len(array)-1) and (j != (len(array[0])-1)))):
        #sum += arrayV(array[i+1][j+1])
        if (array[i+1][j+1] == 'L'):
           break
        elif (array[i+1][j+1] == '#'):
           sum += 1
           break
        i += 1
        j += 1

    return sum



f = open("input.txt")
valid = 0

# read input, 2d array of seats and floors
# rep as an array of strings.
# values read in as L or .
array = []
#2d array of weights rather than thing
#values = [][]

# parse input file, add to list 
for line in f:
    array.append(line.strip())
    v = []
    for c in line.strip():
        if ('L' == c):
            v.append(0)
        elif ('.' == c):
            v.append(0)
    #values.append(v)

count = 0
# do game of life shit
while (True):
    #print(array)
    i = 0
    newArray = []
    #newvalues = [][]
    for line in array:
        st = ''
        #newvalue = []
        j = 0
        while (j < len(line)):
            if ('.' == line[j]):
                st += '.'
            elif('L' == line[j]):
                
                if (0 == calcValue(array,i,j)):
                    st += '#'
                else:
                    st += 'L'
            elif('#' == line[j]):
                if (calcValue(array,i,j) >= 5):
                    st += 'L'
                else:
                    st += '#'
            j += 1
        newArray.append(st)
        i += 1
    count += 1
    if (array == newArray):
        print("FOUND IT!")
        break
    array = newArray
    #if (count > 3000000):
        #break
                
print(array)

count = 0
for line in array:
    for c in line:
        if (c == '#'):
            count += 1

print("Num seats occupied: " + str(count))
    
f.close()
