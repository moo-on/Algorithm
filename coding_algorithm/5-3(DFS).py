import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
def dfs(x, y):
    if not (0<=x<n and 0<=y<m) :
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x + 1, y)
        dfs(x , y+1)
        dfs(x, y - 1)
        return True
    return False

result = 0
for idx in range(n):
    for idy in range(m):
        if dfs(idx, idy) == True:
            result +=1

print(result)

# 1 1 1 1 0 0 1 1 1
# 1 1 1 1 0 0 1 1 1
# 0 0 1 1 1 0 1 1 1
# 0 0 0 1 1 1 1 1 1
# 0 0 0 1 1 1 1 1 1
# 1 1 1 1 0 0 1 1 0
# 1 1 0 0 1 1 0 0 1
# 0 1 0 0 1 0 0 1 1
# 1 1 0 1 1 1 1 0 0
# -1>= x or n<=x or -1>=y or m<=y

