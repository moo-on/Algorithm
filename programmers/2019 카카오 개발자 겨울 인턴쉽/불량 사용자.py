# 1. banned_id를 user_id에 대입을 해본 후 맞는 아이디 목록을 만든다.
# 2. 해당 목록 중복되면 스킵하면서 DFS
# 3. 끝가지 간다면 set 목록으로 만들어서 중복이 없다면, answer에 등록

import copy

answer = []


def check(graph, check_set, n):
    #  모든 제제 아이디에 맵핑이 되었다면 중복되지 않게 넣어준 후 종료
    if n == len(graph):
        if check_set not in answer:
            answer.append(check_set)
        return
    #  각 불량 아이디에 실제 아이디의 모든 경우의 수를 맵핑 해준다
    for user in graph[n]:
        if user not in check_set:
            temp = copy.deepcopy(check_set)
            temp.add(user)
            check(graph, temp, n + 1)


def solution(user_id, banned_id):
    user_id.sort(key=lambda x: len(x))
    banned_id.sort(key=lambda x: x.count("*"))
    graph = []

    #  ban 아이디 마다 가능한 모든 유저 아이디를 맵핑 해준다
    for ban in banned_id:
        temp = []
        for user in user_id:
            if len(ban) != len(user): continue
            for b, u in zip(ban, user):
                if b == "*": continue
                if b != u: break
            else:
                temp.append(user)
        graph.append(temp)

    check(graph, set([]), 0)

    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))

#
# '*rodo'] 2'frodo' 'crodo'
# 'fr*d*'] 2'frodo' 'fradi'
# '******'] 2'abc123' 'frodoc'
# '******'] 2'abc123' 'frodoc'
