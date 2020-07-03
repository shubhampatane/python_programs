n = input()
st = [i for i in n]

ans = []
cur = 0
nlock = False

for i in st:
    if i == "<":
        cur = 0
    elif i == ">":
        cur = len(ans)
    elif i == "*":
        if cur!=0:
            ans.pop(cur-1)
            cur = cur - 1
    elif i == "#":
        if nlock:
            nlock = False
        else:
            nlock = True
    else:
        if i.isnumeric():
            if nlock:
                pass  
            else:
                ans.insert(cur,i)
                cur += 1
        else:
            ans.insert(cur,i)
            cur += 1
    print(ans)
print("".join(ans))
