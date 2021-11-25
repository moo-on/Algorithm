
import copy

SHEEP = 1


def solution(info, edges):
    def dfs(cnt, nodes, sheep):
        global SHEEP

        if sheep > SHEEP: SHEEP = sheep  # 현재 가지고 있는 양의 개수가 더 많다면 최대 값 바꿔주기

        for node in nodes:
            copy_nodes = copy.deepcopy(nodes)
            copy_nodes.remove(node)
            copy_nodes.extend(graph[node])

            if info[node] == 1:  # 늑대라면
                if cnt - 1 == 0: continue  # 늑대와 같아진다면 멈추기
                dfs(cnt - 1, copy_nodes, sheep)
            elif info[node] == 0:  # 양이라면
                dfs(cnt + 1, copy_nodes, sheep + 1)

    graph = [[] for _ in range(len(info))]
    for edge in edges:
        graph[edge[0]].append(edge[1])

    dfs(1, graph[0], 1)
    return SHEEP


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))

print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
               [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))
