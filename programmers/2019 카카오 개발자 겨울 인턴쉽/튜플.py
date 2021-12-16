
import copy


def solution(s):
    answer = []
    temp = []
    lst = s.split("}")
    for i, e in enumerate(lst):
        lst[i] = e.strip(",{}")
    for e in lst:
        if e == "": continue
        e = e.split(",")
        e = list(map(int, e))
        temp.append(e)
    temp.sort(key=lambda x: len(x))
    temp = list(map(set, temp))

    for i, e in enumerate(temp):
        if i == 0:
            answer.append(e)
            continue

        ori = copy.deepcopy(e)
        prev = temp[i - 1]
        for e_e in prev:
            ori.discard(e_e)

        answer.append(ori)

    return [e for set in answer for e in set]


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
