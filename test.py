import sys
input = sys.stdin.readline

n = int(input())
lst = [input().split() for _ in range(n)]

s = set()

for l in lst:
    if l[0] =='add':
        s.add(l[1])
    elif l[0] == 'remove':
        if l[1] in s: s.remove(l[1])
    elif l[0] == 'check':
        if l[1] in s: print(1)
        else: print(0)
    elif l[0] == 'toggle':
        if l[1] in s: s.remove(l[1])
        elif l[1] not in s: s.add(l[1])
    elif l[0] == 'all':
        s = set([i for i in range(1,21)])
    elif l[0] == 'empty':
        s= set()



