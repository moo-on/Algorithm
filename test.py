import heapq
from collections import deque

def solution(jobs):
    answer = []
    len_ = len(jobs)

    heap_ = []
    jobs = deque(sorted(jobs))

    job = jobs.popleft()
    temp = job[0]

    finish = []


    while jobs:
        # 1. heap이 비어 있어, 작업 요청이 들어오고 바로 시작하는 경우
        if not heap_ and temp <= job[0]:
            answer.append(job[1])`
            temp = job[0]+job[1]
            job = jobs.popleft() # 새로운 작업 시작

        # 2. 작업 요청이 끝나는 지점 보다, 이전 작업이 요청 들어오는 경우 전부 추가해주기
        while temp > job[0]:
            heapq.heappush(heap_, [job[1], job[0]]) # 소요시간이 짧은 작업부터 빼내기 위함
            if jobs:
                job = jobs.popleft()
            else:
                break


        # 3. heap 안에 작업 하나씩 요청 처리
        if heap_:
            item = heapq.heappop(heap_)
            item[0], item[1] = item[1], item[0]
            answer.append(temp - item[0] + item[1])
            temp += item[1]

        if not jobs:
            heapq.heappush(heap_, [job[1], job[0]])


    # heap 안에 작업이 남은 경우
    while heap_ :
        item = heapq.heappop(heap_)
        item[0], item[1] = item[1], item[0]
        answer.append(temp - item[0] + item[1])
        temp += item[1]



    if len_ == 1:
        return job[1]

    print(answer)

    return answer



#print(solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]])) #13
#print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]])) # 72

print(solution([[0, 10], [4, 10], [15, 2], [5, 11]]))



