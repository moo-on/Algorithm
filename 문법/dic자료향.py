# 선언
dic = {}

dic = {'a' : 1 }

dic['a'] += 1
print(dic['a'] + 1)


def solution(participant, completion):
    dic = {}
    for E in participant:
        dic[E] = 0
    for E in participant:
        dic[E] += 1
    for E in completion:
        dic[E] -= 1

    for key, val in dic.items():
        if val == 1:
            answer = key

    return answer

lst_1 =['leo', 'kiki', 'eden']
lst_2 =['eden', 'kiki']

print(solution(lst_1, lst_2))

