def DFS(cnt, prev_node, i):
    if cnt == len(lst): return

    # 현재 가는 경로가 더 긴 루트라면 끝낸다.
    if check_lst[i] <= check_lst[prev_node] + 1: return

    # 아니라면 현재 노드에 짧은 값 대입
    check_lst[i] = check_lst[prev_node] + 1

    # 현재 노드에서 다음 노드로 가지 쳐준다.
    for node in lst[i]:
        DFS(cnt + 1, i, node)

def solution(n, edge):
    global lst
    global check_lst

    lst = [[] for _ in range(n+1)]
    check_lst = [20001 for _ in range(n+1)]
    check_lst[0] = -1

    for e in edge:
        lst[e[0]].append(e[1])
        if e[0] == 1: continue
        lst[e[1]].append(e[0])

    DFS(0, 0, 1)

    check_lst.sort(reverse=True)
    for i in check_lst:
        if i == 20001: continue
        MAX = i
        break

    answer = check_lst.count(MAX)

    return answer


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
