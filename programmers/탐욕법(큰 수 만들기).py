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
    lst = list(map(int, number))
    answers = []
    lst_f = lst[:k + 1]
    index_l = 0

    while k != 0:
        max_n = max(lst_f)
        index = lst_f.index(max_n)
        index_l += index+1
        k -= (index)

        lst_f = lst[index_l: index_l + k+1]
        answers.append(max_n)
        print("lst_f: ", lst_f)
        print("answers: ", answers)
        print("index_l: ", index_l)
        print("_______")
        if len(lst_f) == 2: break
    if len(answers) == len(lst) -k: return ''.join(map(str, answers))
    answers.extend(lst[index_l:])
    return ''.join(map(str, answers))



#number = "4177252841"  #원소 10개
number = "99991"
k = 3 # 7752841 3개 뽑아서 없애기 7개 원소 고르기
#k = 4 # 775841 4개 뽑아서 없애기




#print(solution(number, k ))
print(solution(number,k))