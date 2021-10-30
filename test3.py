# 4	3	[[2, 2]]	4
import heapq

heap = [9999]


def solution(m, n, puddles):
    graph = [[9999 for _ in range(m + 1)] for _ in range(n + 1)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def DFS(start, cnt):
        if start == [m, n]:
            heapq.heappush(heap, cnt)
            return

        x, y = start[0], start[1]
        graph[y][x] = cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= 0 or nx > m or ny <= 0 or ny > n: continue
            if graph[ny][nx] < cnt + 1: continue
            if [nx, ny] in puddles: continue
            if cnt + 1 > heap[0]: return
            DFS([nx, ny], cnt + 1)

    DFS([1, 2], 1)
    DFS([2, 1], 1)

    return heap.count(heap[0])


print(solution(4, 3, [[2, 2]]))

set1 = [1,2,3]
set2 = [1,2,3]
if set1 == set2:
    print("yes")