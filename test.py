import heapq


def solution(jobs):
    answer = []
    heap_ = [] # 작업이 밀렸을 때 저장할 자료공간
    jobs.sort() # 작업 순서대로 정렬

    temp = jobs[0][0] # 시각을 가장 첫번째 작업의 시각으로 맞춰줌

    for job in jobs:
        # 1. heap 내부가 비어있고, 시각이 작업 요청보다 작거나 같다면, 작업 바로 실행
        if not heap_ and temp <= job[0]:
            answer.append(job[1])
            temp = job[0] + job[1]
        # 2. heap 안에 사용할 자료가 있고&시각이 작업요청보다 작거나 같다면, 지금까지 쌓은 작업을 현재 작업을 넣기 전까지 사용.
        elif heap_ and temp <= job[0]:
            while True:
                item = heapq.heappop(heap_)
                item[0], item[1] = item[1], item[0]
                # 값 추가 및 시각 증가
                answer.append(item[1]+temp-item[0])
                temp += item[1]
                # 현재 시각이 작업 요청보다 커진다면 힙안에 넣어주고 종료.
                if temp > job[0]:
                    heapq.heappush(heap_, [job[1], job[0]])
                    break
                # 현재 시각이 작업 요청보다 작은데, heap안의 자료를 다 사용헀다면 작업 바로 실행
                elif not heap_ and temp <= job[0]:
                    answer.append(job[1])
                    temp = job[0] + job[1]

        # 3. 시각이 작업 요청보다 크다면 해당 작업은 heap_안에 저장
        elif temp > job[0]:
            heapq.heappush(heap_, [job[1], job[0]]) # 작업 순서가 작은 순서로 뽑기 위해 반대로 저장

    # for 문 종료 후 남은 heap_안의 작업 들 처리
    while heap_:
        item = heapq.heappop(heap_)
        item[0], item[1] = item[1], item[0]
        # 값 추가 및 시각 증가
        answer.append(item[1] + temp - item[0])
        temp += item[1]


    return sum(answer)//len(jobs)



print(solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]])) #13
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]])) # 72

print(solution([[0, 10], [4, 10],  [5, 11], [15, 2],])) # 15



