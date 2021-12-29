from collections import defaultdict


def solution(gems):
    answer = []
    cnt = 0
    len_ = len(set(gems))
    llen_ = len(gems)
    MIN = len(gems)

    gems_dic = defaultdict(int)
    for gem in set(gems):
        gems_dic[gem]

    s_i = 0
    e_i = 0
    for i, gem in enumerate(gems):
        if gems_dic[gem] == 0:
            cnt += 1
        gems_dic[gem] += 1
        if cnt == len_:
            e_i = i
            if MIN > e_i - 0:
                answer = [0, e_i]
                MIN = e_i - 0
            break

    while gems_dic[gems[s_i]] > 1:
        gems_dic[gems[s_i]] -= 1
        s_i += 1

    if MIN > e_i - s_i:
        answer = [s_i, e_i]
        MIN = s_i - e_i

    for i in range(e_i + 1, len(gems)):

        gems_dic[gems[i]] += 1

        while s_i <= llen_ - 1 and gems_dic[gems[s_i]] > 1 :
            gems_dic[gems[s_i]] -= 1
            s_i += 1

        if MIN > i - s_i:
            answer = [s_i, i]
            MIN = e_i - s_i

    return [e+1 for e in answer]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]), [3, 7])
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]), [1, 5])
print(solution(["A","B","B","B","B","B","B","C","B","A"]))
