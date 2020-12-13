import math

f = open("input.txt")

timestamp = int(f.readline().strip())
buses = f.readline().strip().split(',')
#print(timestamp)
#print(buses)

activeBuses = []

for bus in buses:
    if (bus != 'x'):
        activeBuses.append(int(bus))

print(activeBuses)
times = []

for bus in activeBuses:
    times.append((math.floor(timestamp/bus)+1)*bus - timestamp)

i = 0
min = times[0]
minIndex = 0
for time in times:
    if (time < min):
        min = time
        minIndex = i
    i += 1

print(times)
print("Smallest = " + str(times[minIndex]) + " " + str(activeBuses[minIndex]))
print("id times minutes = " + str(times[minIndex] * activeBuses[minIndex]))
    
f.close()
