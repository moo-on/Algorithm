from collections import deque


def solution(stones, k):
    answer = max(stones)

    left, right = 0, answer
    mid = (left + right) // 2
    while left <= right:
        cnt = 0
        for stone in stones:
            # 못 건너는 돌
            if stone - mid < 0:
                cnt += 1
            else:
                cnt = 0
            # 건널 수 있을 돌의 개수 초과했을 때
            if cnt == k:
                right = mid - 1
                mid = (left + right) // 2
                break
        #  돌의 횟수가 남았을 경우
        else:
            left = mid + 1
            mid = (left + right) // 2

    return mid


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
