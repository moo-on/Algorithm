# 8	2	["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

def solution(n, k, cmd):

    lst = [i for i in range(n)]
    trash = []

    for e in cmd:
        if e[0] == 'D':
            k += int(e[2])
            continue
        if e[0] == 'U':
            k -= int(e[2])
            continue

        if e[0] == 'C':
            trash.append(lst.copy())
            lst.pop(k)
            if len(lst) == k:
                k -= 1
            continue

        if e[0] == 'Z':
            i = lst[k]
            lst = trash.pop()
            k = lst.index(i)
            continue

    answer = ['X'] * n
    for i in lst:
        answer[i] = 'O'


    return ''.join(answer)

cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

n =  8
k = 2
lst = [i for i in range(n)]
trash = []

for e in cmd:
    if e[0] == 'D':
        k += int(e[2])
        continue
    if e[0] == 'U':
        k -= int(e[2])
        continue

    if e[0] == 'C':
        print('lst:',lst)
        trash.append(lst.copy())
        print('Z_f k:',k)
        lst.pop(k)
        if len(lst)  == k:
            k -= 1
        print(lst)
        print('Z_b k:', k)
        continue

    if e[0] == 'Z':
        i = lst[k]
        lst = trash.pop()
        k = lst.index(i)
        continue

answer = ['X'] * n
for i in lst:
    answer[i] = 'O'

''.join(answer)




a= [1,2,3,4]
tra= []
tra.append(a)
tra.pop()
