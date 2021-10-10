n1 = 6
edge1 = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	#3

def DFS(answer_lst, edge, i, cnt,n):
    for e in edge[i]:
        if cnt == len(answer_lst) - 1: break
        elif e == 1:
            if answer_lst[n] > cnt:
                answer_lst[n] = cnt
                break
        DFS(answer_lst, edge, e, cnt +1, n)

def solution(n, edge):
    answer_lst  = [30000 for _ in range(n+1)]
    lst = [set() for _ in range(n+1)]

    for e in edge:
        lst[e[0]].add(e[1])
        lst[e[1]].add(e[0])

    for i in range(2, n+1):
        DFS(answer_lst, lst, i,1,i)

    uniq = set(answer_lst)
    MAX = sorted(uniq, reverse=True)[1]
    answer = answer_lst.count(MAX)
    return answer


#solution(n1, edge1)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)
print(solution(11, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [
      3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]]), 4)
print(solution(4, [[1, 2], [2, 3], [3, 4]]), 1)
print(solution(2, [[1, 2]]), 1)
print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 2)
print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]), 1)
print(solution(4, [[1, 4], [1, 3], [2, 3], [2, 1]]), 3)
print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]]), 1)
print(solution(4, [[4, 3], [1, 3], [2, 3]]), 2)