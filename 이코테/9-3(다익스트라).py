import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
visited = [False]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q= []
    heapq.heappush(q, (0,start))
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

# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         #처리된 노드 무시
#         if distance[now] < dist:
#             continue
#         #현재 노드와 연결된 노드확인
#         for i in graph[now]:
#             cost = i[1] + dist
#             #현재 노드 거쳐서 이동하는게 더 빠를 경우
#             if cost<distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
for i in range(1, n+1):
    if distance[i] < INF and distance[i] != 0 : count += 1
MAX = max(distance[1:])

print("%d %d" %(count, MAX))



#
# dijkstra(start)