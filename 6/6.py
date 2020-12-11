
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
        
'''
    list = line.split(' ')
    for item in list:
        if (item == '\n'):
            #print("Poopy")
            passportDone = True
            break
        key,value = item.split(':')
        value = value.strip()
        passport[key] = value
        #count += 1
        #print("Key = " + key + " Value = " + value)
    if(passportDone):
        #print(passport)
        if (passport['byr'] != '' and
            passport['iyr'] != '' and
            passport['eyr'] != '' and
            passport['hgt'] != '' and
            passport['hcl'] != '' and
            passport['ecl'] != '' and
            passport['pid'] != ''):
            #count += 1 #from part 1
            # This is extra data checking added to part 2, holy fuck
            if (int(passport['byr']) > 1919 and int(passport['byr']) < 2003 and
                int(passport['iyr']) > 2009 and int(passport['iyr']) < 2021 and
                int(passport['eyr']) > 2019 and int(passport['eyr']) < 2031 and
                passport['hcl'][0] == '#' and len(passport['hcl'][1:]) == 6 and
                all(c in string.hexdigits for c in passport['hcl'][1:]) and
                (passport['ecl'] == 'amb' or passport['ecl'] == 'blu' or
                 passport['ecl'] == 'brn' or passport['ecl'] == 'gry' or
                 passport['ecl'] == 'grn' or passport['ecl'] == 'hzl' or
                 passport['ecl'] == 'oth') and
                len(passport['pid']) == 9
                ):
                
                heightType = passport['hgt'][-2:]
                if (heightType == 'cm'):
                    if (int(passport['hgt'][:-2]) > 149 and int(passport['hgt'][:-2]) < 194):
                        count += 1
                elif (heightType == 'in'):
                    if (int(passport['hgt'][:-2]) > 58 and int(passport['hgt'][:-2]) < 77):
                        count += 1
            
        passport = {
            'byr': '',
            'iyr': '',
            'eyr': '',
            'hgt': '',
            'hcl': '',
            'ecl': '',
            'pid': '',
            'cid': ''
        }
        passportDone = False
        #count = 0

print(count)        
'''

f.close()
