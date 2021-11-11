# [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
def solution(lottos, win_nums):
    zero_cnt = 0
    level = 1
    for i in lottos:
        if i == 0:
            zero_cnt += 1
        elif i not in win_nums:
            level += 1

    if level == 7: cnt = 6

    high, low = level, level + zero_cnt

    if low > 6:
        low = 6
    if high > 6:
        high = 6

    answer = [high, low]

    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
