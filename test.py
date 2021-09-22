import heapq

case1 = ["I 16", "D 1"]
case2 = ["I 7","I 5","I -5","D -1"]
case3 = ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]
def solution(operations):
    answer = 0
    min_heap = []
    max_heap = []

    # 값 제거 연산 시, 큐에 있는것보다 삭제 연산이 같아지면 큐 초기화
    for operation in operations:
        if operation[0] == "I":
            heapq.heappush(min_heap,int(operation[2:]))
            heapq.heappush(max_heap, [-int(operation[2:]), int(operation[2:])])
        else: # D 연산 일 경우
            if not min_heap or not max_heap: continue # 둘 중에 하나라도 비어 있다면, 연산 패스
            if operation[2] == "1": heapq.heappop(max_heap)  # 최대 값 제거 연산
            else: heapq.heappop(min_heap)  # 최소 값 제거 연산
            # 연산 끝난 후 둘 중에 하나라도 큐가 비어 있다면 큐 둘다 초기화
            if not min_heap or not max_heap:
                min_heap = []
                max_heap = []
    # 연산 다 종료 후
    if not min_heap or not max_heap: return [0,0]
    else: return [max_heap[0][1], min_heap[0]]


print(solution(case3))