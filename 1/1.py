
f = open("input.txt", "r")

a = 0
b = 0
c = 0

#count = 0 #len(f)

accounts = []

for i in f:
    accounts.append(i)

print ("count = " + str(len(accounts)))

i = 0

while(i < len(accounts)):
    j = i + 1
    while(j < len(accounts)):
        k = j + 1
        while(k < len(accounts)):
            
        #print (str(accounts[i]) + " + " + str(accounts[j]) + " = " +str(accounts[i] + accounts[j]))
            if (int(accounts[i]) + int(accounts[j]) + int(accounts[k]) == 2020):
                a = int(accounts[i])
                b = int(accounts[j])
                c = int(accounts[k])
                break
            k += 1
        j += 1
    i += 1
        
print (str(a) + " " + str(b) + " " + str(c))

f.close()
