
import string


f = open("input.txt")
valid = 0

#File is just a bunch of ints, easy peasy  

jolts = []
j1 = 0
j2 = 0
j3 = 0
acc = 0


# parse input file, add to list 
for line in f:
    jolts.append(int(line.strip()))

# sort list
jolts.sort()

# add the final laptop
jolts.append(jolts[-1]+3)

cont1diffs = []
cont1diff = 0
for j in jolts:
    diff = j - acc
    if (1 == diff):
        j1 += 1
        cont1diff += 1
    elif (2 == diff):
        j2 += 1
    elif (3 == diff):
        cont1diffs.append(cont1diff)
        cont1diff = 0
        j3 += 1
    else:
        print("poop " + str(acc) + " " + str(j))
    acc = j

print("1diff = " + str(j1) + " 2diff = " + str(j2) + " 3diff = " + str(j3))
print("1j * 3J = " + str(j1*j3))
print("cont 1 diffs = " + str(cont1diffs))


# for every +3, those are required values that cannot be removed.
# if there is a +1 between two +3s, they must both remain in every pattern
# it is only when we reach 3 +1s in a row when we are able to remove one
# and still ahere to requiremetns
# eg
# 30 33 36
# must include all
# 30 33 34 37
# still must include all
# 30 33 34 35 38
# we are able to use this sequence and 20 33 35 38 and meet requirements
# taking a look at the number of continuous +1s, the most we need to discover
# is +4 s inbetween each. In this case, there are 3 potentially removable numbers

#THREE MOVABLE											
#all    		42	45	46	47	48	49	52		7combos	cannot remove all 3
#remove 1		42	45	46	47		49	52			
#remove 1		42	45	46		48	49	52			
#remove 1		42	45		47	48	49	52			
#remove 2		42	45	46			49	52			
#remove 2		42	45		47		49	52			
#remove 2		42	45			48	49	52			
											
											
#all    		42	45	46	47	48	51			4combos	
#remove 1		42	45	46		48	51				
#remove1		42	45		47	48	51				
#remove 2		42	45			48	51				
											
											
#all    		42	45	46	47	50				2combos	
#remove 1		42	45		47	50					

bigsum = 1
for j in cont1diffs:
    if (j == 4):
        bigsum *= 7
    elif (j == 3):
        bigsum *= 4
    elif (j == 2):
        bigsum *= 2
    

print(bigsum)

    
f.close()
