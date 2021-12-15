from collections import defaultdict


def solution(s):
    str_dict = defaultdict(int)

    for e in s:
        str_dict[e] += 1

    lst = [0 for _ in range(1 + max(str_dict.values()))]

    for i, e in str_dict.items():
        lst[e] += 1

    lst.reverse()

    cnt = 0

    for i, e in enumerate(lst):
        if i == len(lst) - 1:
            continue
        if e > 1:
            over = lst[i] - 1
            lst[i + 1] += over
            cnt += over

    return cnt


print(solution("ceabaacb"))
print(solution("ccceeeaabbfdz"))
