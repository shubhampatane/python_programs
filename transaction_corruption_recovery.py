r = float(input())
d = int(input())
tr = []
l =[]
m = []
curr=9
tot = 0

for i in range(1,d-1):
    k = input()
    tr.extend(k.split())
interest = float(input())
for i in range(0,d-2):
    l.append(int(tr[i*4]))
    m.append(int(tr[(i*4)+3]))

    
for i in range(0,len(l)-1):
    if(l[0]==3):
        curr=1
    elif(l[i]==l[i+1]-3):
        curr=i+2   
if  l[-1]==len(l):
    curr = len(l)+1

# calculate interest
a = r/36500
for i in m:
    tot = tot + a*i
   
if(tr[((curr-1)*4)+2]=='debit'):
    bal_2 = int(tr[((curr-1)*4)+1])+int(tr[((curr-1)*4)+3])
if(tr[((curr-1)*4)+2]=='credit'):
    bal_2 = int(tr[((curr-1)*4)+3])-int(tr[((curr-1)*4)+1])
    
tot = tot + a * bal_2
int_1 = interest - tot
bal_1 = round(int_1/a)

if bal_1 >= int(tr[((curr-2)*4)+3]):
    nu = bal_1-int(tr[((curr-2)*4)+3])
    print(str(curr) + " " + str(nu) + " " + "credit" + " " + str(bal_1))
else:
    nu = int(tr[((curr-2)*4)+3])-bal_1
    print(str(curr) + " " + str(nu) + " " + "debit" + " " + str(bal_1))

if bal_2 >= bal_1:
    nu = bal_2-bal_1
    print(str(curr+1) + " " + str(nu) + " " + "credit" + " " + str(bal_2))
else:
    nu = bal_1-bal_2
    print(str(curr+1) + " " + str(nu) + " " + "debit" + " " + str(bal_2))
