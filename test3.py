# 4	3	[[2, 2]]	4
import heapq


def solution(m, n, puddles):
    answer = 0

    m, n = n, m
    puddles = list(map(tuple, puddles))
    puddles = set(puddles)

    dx = [1, 0]
    dy = [0, 1]

    def dfs(x, y):
        nonlocal answer
        if x == m and y == n:
            answer += 1
            answer %= 1000000007
            return

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > m or ny > n: continue
            if (ny, nx) in puddles: continue

            dfs(nx, ny)

    dfs(1, 1)

    return answer % 1000000007


print(solution(4, 3, [[2, 2]]))
