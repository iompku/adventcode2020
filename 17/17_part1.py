
import traceback
import string

# Make it 3 dimensional
# make it expand in all directions
# array.insert(i,x) Insert a new item with value x in the array before
# position i. Negative values are treated as being relative to the end
# of the array.

def arrayV(char):
    if ('#' == char):
        return 1
    return 0

def calcValue(array3d, z, i, j):
    sum = 0
    #corner cases, don't want to index outside array
    try:
        for zz in range(-1,2):
            zi = z + zz
            if ((zi >= 0) and (zi < len(array3d))):
                array = array3d[zi]
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

                # middle of the plane when zz != 0
                if (zz != 0):
                    sum += arrayV(array[i][j])

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
                    if (j < (len(array[0])-1)):
                        sum += arrayV(array[i+1][j+1])
    except IndexError as err:
        print("Index Error on z = " + str(z) + " i = " + str(i) + " j = " + str(j) + " len(array[0]) = " + str(len(array[0])))
        print(array3d)
        print(array)
        print(err)
        traceback.print_exc()
        s = input()

    return sum

f = open("input.txt")
valid = 0

# read input, starts as 2d array 
array = []
#2d array of weights rather than thing
#values = [][]

# parse input file, add to list 
for line in f:
    array.append(line.strip())

array3d = [array]

count = 0
# do game of life stuff
while (True):
    #expand array out if needed, work inside out
    #inside is a square shape, staring height and width of 8
    print(array3d)

    # This section expands each plane, assuming square plane. Adds '.' around it for expansion
    planeI = 0
    for plane in array3d:
        #print("array before")
        #print(array3d[planeI])
        
        #this works for a square shape only, because we assume len of all will work
        newPlane = []
        #top row
        s = ''
        for yy in range(0, len(plane[0].strip())+2):
            s += '.'
        newPlane.append(s)
        #add outside columns
        for line in plane:
            s = '.' + line.strip() + '.'
            newPlane.append(s)
        s = ''
        #bottom row
        for yy in range(0, len(plane[0].strip())+2):
            s += '.'
        newPlane.append(s)
        array3d[planeI] = newPlane
        #print("array after")
        #print(array3d[planeI])
        planeI += 1
    
    #create new planes if needed (don't bother if there are no # in the outer planes
    # just going to assume there are
    #if ('#' in array3d[0]):
    #create array of just '.' characters
    x = []
    for xx in range(0, len(array3d[0])):
        s = ''
        for yy in range(0, len(array3d[0][0])):
            s += '.'
        x.append(s)
    #stick it in the front and the back
    array3d.insert(0, x)
    array3d.append(x)
    #print("Uprint(array3d)pdated")
    print(array3d)
    #sssss = input()
        
    z = 0
    new3dArray = []
    for plane in array3d:
        #print(array)
        i = 0
        newArray = []
        for line in plane:
            st = ''
            j = 0
            while (j < len(line.strip())):
                #print(line)
                #print(len(line))
                # if a cube is inactive
                if ('.' == line[j]):
                    # but exactly 3 of it's neighbors are active
                    if (3 == calcValue(array3d,z,i,j)):
                        st += '#' # the cube becomes active
                    else: #Otherwise, the cube remains inactive.
                        st += '.'
                # if a cube is active
                elif('#' == line[j]):
                    val = calcValue(array3d,z,i,j)
                    # and exactly 2 or 3 of its neighbors are also active
                    if ((val == 2) or (val == 3)):
                        st += '#'  #the cube remains active
                    # Otherwise, the cube becomes inactive.
                    else:
                        st += '.'
                j += 1
            newArray.append(st)
            i += 1
        new3dArray.append(newArray)
        z += 1
    count += 1
    
    array3d = new3dArray
    if (count > 5):
        break
                
print(array3d)

count = 0
for array in array3d:
    for line in array:
        for c in line:
            if (c == '#'):
                count += 1

print("Num charged: " + str(count))
    
f.close()
