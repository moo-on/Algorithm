import heapq

def solution(jobs):
    jobs.sort()
    answer = 0
    _heap = []

    # 1. 기준점보다 작업요청이 빠른 작업들을 힙안에 넣어준다.
    temp = 0
    for job in jobs:
        if temp >= job[0]:

            # 1-1. 작업시간이 최소인 아이템을 선별하기 위해서 바꿔서 푸쉬해준다.
            heapq.heappush(_heap, [job[1], job[0]])
    # 2. 기준점보다 작업요청이 느린 작업을 만나면, 지금까지 힙에 쌓아논 아이템 중에 가장 최소 값을 빼내어서 현재 기준점을 업데이트 해준다. 그 후 heap 안에 push
        elif temp < job[0]:
            if len(_heap) == 0:
                temp = job[0]
                heapq.heappush(_heap, [job[1], job[0]])

            items = heapq.heappop(_heap)
            # 대기시간 더해주기.(순서를 바꿔서 넣은것 참고)
            answer += (temp - items[1] + items[0])
            heapq.heappush(_heap, [job[1], job[0]])
            # 기준점 올려주기
            temp += items[0]

            # 2-1. 올라간 기준점으로 할 수 있는 2번 작업 다 해주기
            if len(_heap) >=1:
                while _heap[0][1] >= temp:
                    items = heapq.heappop(_heap)

                    # 대기시간 더해주기.(순서를 바꿔서 넣은것 참고)
                    answer += (temp - items[1] + items[0])
                    heapq.heappush(_heap, [job[1], job[0]])
                    # 기준점 올려주기
                    temp += items[0]
                    # heap이 남아있지 않은 경우 에러 방지
                    if len(_heap) ==0: break
                    # 다시 heapq 넣기 반복

    # for state 반복 후 heapq 안에 작업들 남아 있을 경우 처리.
    while _heap:
        items = heapq.heappop(_heap)
        answer += (temp - items[1] + items[0])
        temp += items[0]

    return answer//len(jobs)



print(solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]))