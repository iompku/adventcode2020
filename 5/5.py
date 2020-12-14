
f = open("input.txt", "r")

#open file
#first 7 chars are F and Bs
# F is 0, B is 1
# binary number, convert to decimal 0-127
# last 3 chars are L and R
# binary again, L is 0 R is 1, selects column 0-7
# unique seat ID: multiply the row by 8, then add the column.

maxid = 0
seatlist = []
for line in f:
    binary = line.replace('F', '0')
    binary = binary.replace('B', '1')
    binary = binary.replace('L', '0')
    binary = binary.replace('R', '1')
    binAns = int(binary, 2)
    rowStr = line[0:7]
    colStr = line[7:10]
    row = 0
    col = 0
    i = 6
    for c in rowStr:
        if c == 'B':
            row += 2**i
        i -= 1
    i = 2
    for c in colStr:
        if c == 'R':
            col += 2**i
        i -= 1
    seatid = row*8 + col
    seatlist.append(seatid)
    if (seatid != binAns):
        print("Miss binAnswer: " + str(binAns) + " seatid = " + str(seatid) + " row = " + str(row) + " col = " + str(col))
    if (seatid > maxid):
        maxid = seatid

print(str(maxid))

i = 0
while(i < len(seatlist)):
    if (seatlist[i]+1) not in seatlist:
        seat = seatlist[i]+1
        break
    i += 1

print("My seat = " + str(seat))


f.close()
