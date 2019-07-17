s = input()
j = ["0","1","2","3","4","5","6","7","8","9","0"]
n = [i for i in s if i in j]
n = [int(i) for i in n]
n = n[::-1]
a = []
c= 0
for i in s:
    if i not in j:
        a.append(i)
    else:
        a.append(str(n[c]))
        c+=1
st = ""
st = st.join(a)
print(st)

"""
Input
sk#b3bkjb4bk1
output
sk#b1bkjb4bk3
"""
