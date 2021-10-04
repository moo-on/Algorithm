import sys
input =sys.stdin.readline


n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    #a->b의 비용은 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for idx in range(n+1):
        for idy in range(n+1):
            graph[idx][idy] = min(graph[idx][idy], graph[idx][k] + graph[k][idy])

[print("INF", end = " ") if graph[idx][idy] == INF else print(graph[idx][idy], end=" ") for idx in range(1,n+1) for idy in range(1, n+1)]


# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if graph[a][b] == 1e9:
#             print("INFINITY", end=" ")
#         else:
#             print(graph[a][b], end=" ")
#     print()
# 4 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2