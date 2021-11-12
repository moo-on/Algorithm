# [4,7,12]	[true,false,true]	9

def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs):
        if not sign:
            num = -num

        answer += num
    return answer


print(solution([4, 7, 12], [True, False, True]))
