# [1, 2, 3, 9, 10, 12]	7	2
import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    heapq.heapify(scoville)

    while len(scoville) >= 2 :
        # 제일 작은 원소가 K보다 크면 로직 종료
        temp = heapq.heappop(scoville)
        if temp >= K: break
        # K보다 스코빌 지수가 낮은 음식이라면, 새로운 음식을 만든다.
        if temp < K:
            temp += 2*heapq.heappop(scoville)
            answer += 1
            # 새로운 음식을 힙에 넣는다.
            heapq.heappush(scoville, temp)

    # 원소가 K보다 작으면 -1 반환
    if scoville[0] < K: return -1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7)) # 2
