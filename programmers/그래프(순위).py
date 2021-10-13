n1 = 5
case1 = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	#2

from collections import deque

def solution(n, results):
    answer = 0
    graph = [[[],[]] for _ in range(n+1)]

    # 각 노드에 [node, 승패 여부] 추가 0 == 패, 1== 승
    for result in results:
        win_node = result[0]
        lose_node = result[1]
        graph[win_node][1].append(lose_node)
        graph[lose_node][0].append(win_node)

    # 탐색
    for i in range(1, n+1):
        cnt = 0
        visited = [0 for _ in range(n+1)]
        win_lst = deque(graph[i][1])
        lose_lst = deque(graph[i][0])

        while win_lst:
            node = win_lst.pop()
            if visited[node] ==1: continue
            else: visited[node] = 1
            win_lst.extend(graph[node][1])
            cnt += 1

        while lose_lst:
            node = lose_lst.pop()
            if visited[node] ==1: continue
            else: visited[node] = 1
            lose_lst.extend(graph[node][0])
            cnt +=1

        if cnt == n-1: answer += 1
    return answer

print(solution(n1, case1))