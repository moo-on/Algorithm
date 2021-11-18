def visit(k, graph, visited):
    visited[k] = 1
    for i in range(len(graph[k])):
        if visited[i] == 0 & graph[k][i]:
            visit(i, graph, visited)

def solution(n, computers):
    answer = 0
    visited = [0]*n

    for i in range(n):
        if visited[i] == 0:
            visit(i, computers, visited)
            answer += 1
    return answer