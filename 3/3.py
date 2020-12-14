
f = open("input.txt", "r")

a = 0
b = 0
c = 0

#count = 0 #len(f)

slopeRight = 1
slopeDown = 2

path = []

#print("Line length = " +str(len(f.readline())))

for i in f:
    path.append(i)

#print ("lines = " + str(len(path)))

loop = 2

#chars = path[321].strip()

x = 0
y = 0
trees = 0

#while (i < 74):
while(y < len(path)-1):
    x += slopeRight
    y += slopeDown
    
    line = path[y].strip()
    #print(line)
    if(line[x%31] == '#'):
        trees +=1

print ("Trees = " + str(trees))
    

'''
for line in path:
    #print(line.strip())
    
    loop = 2
    while(loop > 0):
        #for char in line:
        print(line.strip(), end='')
        loop = loop - 1
    print()
    
'''


i = 0



f.close()
