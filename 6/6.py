
import string

# char 'a' is 97, 'z' is 122
# so indexing into an array
# 0-25 subtract an offset of 97
offset = 97

form = [0] * 26



f = open("input.txt")
valid = 0

passportDone = False
count = 0

sums = []
groupCount = 0
#Parse the file for the needed values
for line in f:
    groupCount += 1
    if (line == '\n'):
        groupCount -= 1
        #done with this group, sum up and reset
        #i = 0
        for letter in form:
            if (letter == groupCount):
                count += 1
            
        sums.append(count)
        form = [0] * 26
        count = 0
        groupCount = 0
        #print(" ")
    for char in line:
        char = char.strip()
        #print("Adding " + char + " as index " + str(ord(char)-offset))
        if (char != ''):
            form[ord(char)-offset] += 1

for letter in form:
    if (letter == groupCount):
        count += 1
sums.append(count)

print(sums)
count = 0
for s in sums:
    count += s
print(str(count))
        

f.close()
