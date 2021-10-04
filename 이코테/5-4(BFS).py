from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx =[ -1, 0, 1, 0]
dy =[0, -1, 0, 1]
def bfs( x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]


print(bfs(0,0))

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111