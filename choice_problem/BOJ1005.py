import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

t = int(input())
answer= []
for _ in range(t):
    n,k = map(int, input().split())

    #기본세팅

    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    distance = [INF]*(n+1)

    lst = list(map(int, input().split()))
    #간선입력
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b].append((a, -lst[a-1]))

    start = int(input())

    dijkstra(start)
    MIN = min(distance)
    answer.append(-MIN+lst[start-1])

[print(str(answer[i])+"\n") for i in range(t)]