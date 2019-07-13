import math
cars = input()
cars = int(cars)
da = []
d = []
sec = []
for i in range(cars):
    y=[]
    x = input()
    y = x.split(" ")
    da = da + y
for i in da:
    d.append(int(i))
for i in range(0,cars):
    dis = math.sqrt((d[i*3]*d[i*3])+(d[i*3+1]*d[i*3+1]))
    if d[i*3+2]==0:
        pass
    else:
        dis = int(dis/d[i*3+2])
    sec.append(dis)
done = set()
count = 0

for i in sec:
    c = sec.count(i)
    if(c!=1 and i not in done):
        a = (c*(c-1))/2
        count =count + a
        done.add(i)
print(int(count))

