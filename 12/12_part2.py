
x = 0
y = 1

#rotating waypoint in part 2
def turnShip(waypoint, turn, amount):
    direction = 0
    if (turn == 'L'):
        direction =  amount
    elif (turn == 'R'):
        direction =  360 - amount

    if (direction == 90):
        temp = waypoint[x]
        waypoint[x] = (-1)*waypoint[y]
        waypoint[y] = temp

    elif (direction == 180):
        waypoint[x] = (-1) * waypoint[x]
        waypoint[y] = (-1) * waypoint[y]

    elif (direction == 270):
        temp = waypoint[x]
        waypoint[x] = waypoint[y]
        waypoint[y] = (-1)*temp

    else:
        print("Unexpected direction " + str(direction))


    return waypoint

#in part 2, move forward moves towards the waypoint that much
def moveForward(location, waypoint, amount):
    location[x] += waypoint[x] * amount
    location[y] += waypoint[y] * amount
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

# part 2
#The waypoint starts 10 units east and 1 unit north relative to the ship.
waypoint = [10, 1]

# Loop through and perform the actions
i = 0
while (i < len(action)):
    #print(action[i] + " " + str(magnitude[i]))
    if (action[i] == 'N'):
        waypoint[y] +=  magnitude[i]
    elif (action[i] == 'E'):
        waypoint[x] +=  magnitude[i]
    elif (action[i] == 'S'):
        waypoint[y] -=  magnitude[i]
    elif (action[i] == 'W'):
        waypoint[x] -=  magnitude[i]
    elif (action[i] == 'L' or action[i] == 'R'):
        waypoint = turnShip(waypoint, action[i], magnitude[i])
        
    elif (action[i] == 'F'):
        location = moveForward(location, waypoint, magnitude[i])        
    else:
        print("Error, unexpected action '" + action[i] + "'")
        
    i += 1

print("Location at " + str(location[0]) + "," + str(location[1]) + " being " + str(location[0] + location[1]))

    
f.close()
