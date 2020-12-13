
x = 0
y = 1

def turnShip(direction, turn, amount):
    if (turn == 'L'):
        direction +=  amount
    elif (turn == 'R'):
        direction -=  amount

    if (abs(direction) >= 360):
        direction = direction % 360
    if (direction < 0):
        direction = 360 + direction

    return direction

def moveForward(location, direction, amount):
    #parsing input indicates turns are in increments of 90 degrees
    if (direction == 0):
       location[x] += amount
    elif (direction == 90):
       location[y] += amount
    elif (direction == 180):
       location[x] -= amount
    elif (direction == 270):
       location[y] -= amount
    else:
        print("Bad directions " + str(direction))
    return location

f = open("input.txt")

action = []
magnitude = []
turns = []
# parse input file, add to list 
for line in f:
    action.append(line[0])
    magnitude.append(int(line[1:].strip()))
    #if(line[0] == 'L' or line[0] == 'R'):
        #turns.append(int(line[1:].strip()))
#print(turns)

# direction ship is facing, represented in degrees, east 0
direction = 0

# where the ship has travelled in relative terms of the starting location, x and y
location = [0, 0]

# Loop through and perform the actions
i = 0
while (i < len(action)):
    #print(action[i] + " " + str(magnitude[i]))
    if (action[i] == 'N'):
        location[y] +=  magnitude[i]
    elif (action[i] == 'E'):
        location[x] +=  magnitude[i]
    elif (action[i] == 'S'):
        location[y] -=  magnitude[i]
    elif (action[i] == 'W'):
        location[x] -=  magnitude[i]
    elif (action[i] == 'L' or action[i] == 'R'):
        direction = turnShip(direction, action[i], magnitude[i])
        
    elif (action[i] == 'F'):
        location = moveForward(location, direction, magnitude[i])        
    else:
        print("Error, unexpected action '" + action[i] + "'")
        
    i += 1

print("Location at " + str(location[0]) + "," + str(location[1]) + " being " + str(location[0] + location[1]))

    
f.close()
