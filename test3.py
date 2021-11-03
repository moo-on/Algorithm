# 9	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	3
# 4	[[1,2],[2,3],[3,4]]	0
# 7	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	1

# 1. 그래프 만들기
# 2-1 그래프 하나씩 자르기
# 2. 그래프로 각 노드 개수 세기
# 3. 서로 비교하는데, 비교한 놈이랑 겹치면 취소

from collections import deque
import copy


def solution(n, wires):
    answer = []
    graph = [[] for _ in range(n + 1)]
    # 그래프 만들기
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    for wire in wires:
        # 그래프 하나 씩 끊어주기
        copy_graph = copy.deepcopy(graph)
        copy_graph[wire[0]].remove(wire[1])
        copy_graph[wire[1]].remove(wire[0])

        node1, node2 = wire[0], wire[1]
        # 그래프 노드 차이 세주기
        diff = []
        for node in [node1, node2]:
            queue = deque([node])
            visited = [0 for _ in range(n + 1)]

            cnt = 0
            while queue:
                temp = queue.popleft()
                if visited[temp] == 0:
                    visited[temp] = 1
                    cnt += 1
                    queue.extend(copy_graph[temp])
            diff.append(cnt)
        answer.append(abs(diff[0] - diff[1]))

    return min(answer)


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
