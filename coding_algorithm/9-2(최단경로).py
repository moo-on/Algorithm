import sys
input = sys.stdin.readline

INF = int(1e9)


n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    idx,idy = map(int, input().split())
    graph[idx][idy] = 1
    graph[idy][idx] = 1

for i in range(1, n+1):
    graph[i][i] = 0

x, k = map(int, input().split())



for k in range(1, n+1):
    for idx in range(1, n+1):
        for idy in range(1, n+1):
            graph[idx][idy] = min(graph[idx][idy], graph[idx][k]+graph[k][idy])


print(graph[1][k]+graph[k][x])

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
