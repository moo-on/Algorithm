from collections import defaultdict, Counter

def solution(s):
    answer_lst = []
    special_alpha = ['t', 'o', 's']
    input_lst = Counter(s.lower()).most_common()
    max_n = input_lst[0][1]

    for i in range(len(input_lst)):
        if input_lst[i][1] != max_n:
            n = i
            break
    else: n = len(input_lst)

    input_lst = set(sorted(dict(input_lst[:n]).keys()))

    for alpha in special_alpha:
        if alpha in input_lst:
            answer_lst.append(alpha.upper())
            input_lst.remove(alpha)

    if "S" in answer_lst:
        i = answer_lst.index('S')
        answer_lst[i] = 'SS'

    for key in input_lst:
        answer_lst.append(key)

    return "".join(answer_lst)

print(solution('aAb'))
print(solution('BA'))
print(solution('BbA'))
print(solution('aaBBTtooSS'))



