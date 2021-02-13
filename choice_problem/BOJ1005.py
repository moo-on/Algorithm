import sys
from collections import deque

input = sys.stdin.readline

# 위상 정렬 정의
def topology():
    q = deque()
    # 시작점 q에 넣기
    for i in range(1, n+1):
        if degree[i] == 0:
            q.append(i)
            dp[i] += time[i]
    # 끝 지점 까지 가기
    while q:
        now = q.popleft()
        # 꺼낸 노드와 연결된 노드 처리
        for e in graph[now]:
            # 간선 하나 삭제
            degree[e] -= 1
            # 다른 경로가 더 오래 걸릴 경우 시간 바꿔줌
            if dp[e] < dp[now] + time[e]:
                dp[e] = dp[now] + time[e]
            # 간선이 0이 된 경우 q에 넣어줌
            if degree[e] == 0:
                q.append(e)

# 테스트 케이스 입력 & 정답문 생성
case = int(input())
answer = []

for _ in range(case):
    # 노드, 규칙 수 & 건물 건설 시간 입력
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))

    # 진입차수 초기화 & 지나온 시간 저장
    degree = [0] * (n+1)
    dp = [0] * (n+1)

    # 규칙 입력 ex (1,2) = 2는 1이 선행되어야함
    graph =[[] for _ in range(n+1)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        degree[b] += 1

    # 함수 실행
    topology()

    # 원하는 건물 입력 & 출력
    answer.append(dp[int(input())])

#정답 출력
[print(answer[i]) for i in range(case)]





