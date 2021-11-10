# [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
def solution(lottos, win_nums):
    zero_cnt = 0
    cnt = 7
    for i in lottos:
        if i == 0:
            zero_cnt += 1
        elif i in win_nums:
            cnt -= 1


    if cnt == 7: cnt = 6
    answer = [cnt - zero_cnt, cnt]

    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
