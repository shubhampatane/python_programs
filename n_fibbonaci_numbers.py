def fibb(n):
    j =""
    arr = []
    arr.append("1")
    if n==1:
        j = j.join(arr)
        return j
    else:
        arr.append(" ")
        a= 0
        b=1
        c=0
        while n>=2:
            c=a+b
            a = b
            b = c
            arr.append(str(c))
            arr.append(" ")
            n= n-1
        del arr[-1]
        j = j.join(arr)
        return j

n = int(input())
while(n>=1):
    k = int(input())
    print(fibb(k))
    n = n-1
    
