# ["abab","bbaa","bababa","bbbabababbbaa"] [true,false,false,true]

def bitwise(lst):
    temp = lst[0]
    for e in lst:
        if temp & e == 0: return True
        temp = temp & e
    else: return False


def BFS(lst, i):
    for i in range(len(lst)):
        lst[i] = lst[i] - 1
        if bitwise(lst) == True:
            return i



def solution(m, b):
    answer = []
    index = 0
    for i in m:
        lst = b[:m]
        b = b[m:]



    return answer

print(solution([2, 2], [3, 2, 1, 2]))



b =[1,2,3,4]
m= b[:2]
b= b[2:]

print()
