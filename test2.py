import copy
score = 0
max = 0
def solution(n, info):
    global score


    answer = []
    lst = [0 for _ in range(11)]
    score = 0

    def DFS(i, lst):
        global score
        global max
        if i == n:
            lion = 0
            apeach = 0

            temp = 10
            for a, l in zip(info, lst):
                if a == 0 and l == 0:
                    temp -= 1
                    continue
                if a >= l:
                    apeach += temp
                else:
                    lion += temp
                temp -= 1
            # 점수가 더 크면
            if lion - apeach >=1 and score <= lion - apeach:
                score = lion - apeach
                answer.append([score, lst])
                if max < lion-apeach:
                    max = lion-apeach
            return

        for step in range(10):
            t_lst = copy.deepcopy(lst)
            t_lst[step] += 1
            DFS(i + 1, t_lst)

    DFS(0,lst)

    for lst in answer:
        if lst[0] == max:
            answer = lst[1]


    if max >0:
        return answer
    else: return [-1]






print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))