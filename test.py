#1150

def comb(lst, n):
    ret = []
    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst)-n+1):
            for temp in comb(lst[i+1:],n-1):
                ret.append([lst[i]]+temp)
    return ret

def re_duplicate(lst):
    copy_lst = lst.copy()
    for group in copy_lst:
        for e in group:
            if e+1 in group:
                lst.remove(group)
                break
    return lst

def answer(group, d_lst):
    lst= []
    for elements in group:
        sum = 0
        for e in elements:
            sum+=d_lst[e]
        lst.append(sum)

    ans = min(lst)
    return ans


n, k = map(int, input().split())

d=[]
for i in range(n):
    d.append(int(input()))

distance = [d[i+1]-d[i] for i in range(len(d)-1)]

n_lst = [i for i in range(len(d)-1)]
g = re_duplicate(comb(n_lst, k))

ans = answer(g, distance)
print(ans)

































