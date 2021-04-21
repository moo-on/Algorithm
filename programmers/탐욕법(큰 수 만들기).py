from collections import Counter
from itertools import combinations

'''
def solution(number, k):
    lst = list(combinations(list(number), k))
    answer = []
    for l in lst:
        string = ''.join(l)
        answer.append(int(string))
    return str(max(answer))
'''
def solution(number, k):
    answer = []
    lst = list(map(int, number))
    k = 4  # 4개제거 6개가져가기
    n = len(number) - k

    while True:
        lst_f = lst[:-(n - 1)]
        if len(lst_f) == 0: break
        lst_b = lst[n - 1:]
        index = lst.index(max(lst_f))
        answer.append(lst_f[index])
        lst = lst[index + 1:]
        n -= 1

    answer = answer + lst_b

    return "".join(map(str, answer))


answer = []
number = "4177252841"  #"7752841" 7개 뽑기 # 4177 252841
k = 3

lst = list(map(int, number))
l = len(number)
lst_f = lst[:k-l+1]
lst_b = lst[k-l+1:]

while len(lst_f) != 0:
    i = lst_f.index(max(lst_f))
    answer.append(lst_f[i])

    k += 1
    index =+ i
    lst_f = lst[index+1 : k-l +1]




print(solution(number, k ))


