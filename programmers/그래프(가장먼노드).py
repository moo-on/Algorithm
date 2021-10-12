from collections import deque


def solution(n, edge):
    answer_lst = []  # 1로부터 떨어진 노드의 거리가 들어갈 리스트
    graph = [[] for _ in range(n + 1)]  # 인접리스트
    visited_lst = [0 for _ in range(n + 1)]  # 방문리스트
    visited_lst[1] = 1  # 1번 노드로 부터 시작하므로 방문 처리

    queue = deque()  # BFS 처리용 큐 생성

    # 그래프에 인접 리스트 만들어주기.
    for e in edge:
        graph[e[0]].append(e[1])
        if e[0] == 1: continue
        graph[e[1]].append(e[0])

    # 1번 노드와 연결된 노드 넣어주기
    for i in graph[1]:
        queue.append([i, 1])
        visited_lst[i] = 1

    # BFS 실행
    while queue:
        node = queue.popleft()
        answer_lst.append(node[1])  # answer_lst에 BFS의 깊이를 넣어주기

        # 층을 나누어서 돌기 떄문에 가장 먼저 방문한 노드의 거리가 최소 거리
        for i in graph[node[0]]:
            if visited_lst[i] == 1: continue
            visited_lst[i] = 1
            queue.append([i, node[1] + 1])

    # 마지막에 도착한 노드가 가장 깊은 노드이기 때문에 마지막에 있는 값을 최대값으로 설정
    MAX = answer_lst[-1]
    answer = 0

    # 최대값의 카운터가 끝나는 지점의 개수를 세준다.
    for i in reversed(answer_lst):
        if i != MAX: break
        answer += 1


    return answer


# print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)
# print(solution(11, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [
#     3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]]), 4)
# print(solution(4, [[1, 2], [2, 3], [3, 4]]), 1)
# print(solution(2, [[1, 2]]), 1)
# print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 2)
# print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]), 1)
# print(solution(4, [[1, 4], [1, 3], [2, 3], [2, 1]]), 3)
# print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]]), 1)
# print(solution(4, [[4, 3], [1, 3], [2, 3]]), 2)
