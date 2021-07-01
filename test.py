
a = [1,2,3]

del a[1]

l = [1,0,0,2,0,0,3,0,4,0]


temp = []
for e in l:
    if e != 0:
        temp.append(e)
temp.extend([0]*(len(l)-len(temp)))
l = temp
temp.clear()
print(l)
print(temp)
print(l)