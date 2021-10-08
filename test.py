n1 = 2
case1 = [1, 2]  # 2

n2 = 2
case2 = [2, 2]  # 2

n3 = 6
case3 = [7, 10]  # 28

n4 = 1
case4 = [2, 2]  # 2


def solution(n, times):
    right = max(times) * n
    left = 1

    while True:
        mid = (right + left) // 2  # 가운뎃 값 정의

        print(left, mid, right)
        # 해당 시간(mid)에서 몇 명 심사 가능한지 answer에 넣어준다.
        answer = 0
        for time in times:
            answer += mid // time
        #
        if left == mid or right == mid: break
        if answer > n:  # 심사해야할 인원보다 많이 할수있다면, 시간을 줄인다.
            right = mid - 1
        elif answer < n:  # 심사해야할 인원보다 적다면, 시간을 늘린다.
            left = mid + 1
        else:
            break  # 심사해야할 인원과 시간이 알맞다면 반복문을 끝낸다.

    # 인원이 충족되는 시간 mid에서 1초씩 깎으면서 최적의 시간을 찾아낸다.
    while answer == n:
        mid -= 1

        answer = 0
        for time in times:
            answer += mid // time
    mid += 1
    return int(mid)


print(solution(n4, case4))


def solution(n, times):
    right = min(times) * n
    left = 1
    answer = 0
    while (left <= right):
        mid = (right + left) // 2
        temp = n
        for i in times:
            temp -= mid // i
            if temp <= 0:
                answer = mid
                right = mid - 1
                break
        if temp > 0:
            left = mid + 1
    return answer

