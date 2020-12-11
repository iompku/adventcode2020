
'''
#This was part 1 version

f = open("input.txt")
valid = 0

#Parse the file for the needed values
for line in f:
    #voodoo magic by Andrew
    linelist = line.split('-')
    minimum = int(linelist[0])
    linelist = linelist[1].split(' ')
    maximum = int(linelist[0])
    letter = linelist[1].split(":")[0]
    password = linelist[2].strip()
    #print("Letter " + letter + " Between " + str(minimum) + " and " + str(maximum) + " password: '" + password + "'")

    #Determine if the password meets the requirements
    count = password.count(letter)
    if ((count >= minimum) and (count <= maximum)):
        valid += 1
    #else:
        #bad

print(valid)

f.close()
'''


#part 2 version
#basically the parsing is the same, but "minimum" and "maximum"
#mean something different.
#Determine if the password meets the requirements secion changed

f = open("input.txt")
valid = 0

#Parse the file for the needed values
for line in f:
    #voodoo magic by Andrew
    linelist = line.split('-')
    minimum = int(linelist[0])
    linelist = linelist[1].split(' ')
    maximum = int(linelist[0])
    letter = linelist[1].split(":")[0]
    password = linelist[2].strip()
    #print("Letter " + letter + " Between " + str(minimum) + " and " + str(maximum) + " password: '" + password + "'")

    #Determine if the password meets the requirements
    if((len(password) >= minimum) and password[minimum-1] == letter):
        pos1Valid = True
    else:
        pos1Valid = False

    if((len(password) >= maximum) and (password[maximum-1] == letter)):
        pos2Valid = True
    else:
        pos2Valid = False

    # performing an XOR, password is valid
    # only if one is true and the other is false.
    if (pos1Valid != pos2Valid):
        valid += 1
        

print(valid)

f.close()
