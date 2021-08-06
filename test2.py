from collections import defaultdict

import math

def solution(people, limit):
    answer = 0
    people.sort()  # 무게 순 정렬
    low = []  # limit 보다 절반 이하의 사람들 리스트
    fat = []  # limit 보다 절반 이상의 사람들 리스트
    index_fat = 1 # 무거운 사람들과 가벼운 사람들의 무게 비교할 동적 인덱스 뒤에서 부터 탐색하기 위해서 -1로 시작
    index_low = 0 # '동일' 앞에서 부터 탐색
    count = 0 # 무거운 사람과 가벼운 사람을 합칠 수 있는 기회

    for e in people:
        if e <= limit / 2:
            low.append(e)
        else:
            fat.append(e)
    length_low = len(low)
    length_fat = len(fat)

    while (index_low <= (length_low -1)) and (index_fat <= length_fat): # 가벼운 사람의 리스트가 끝나거나 무거운 사람의 리스트가 끝날 시에 종료
        if low[index_low] + fat[-index_fat] <= limit: # 가벼운 사람과 무거운 사람이 limit 보다 작을 시에 다음 사람으로 넘어가면서 count 증가
            index_fat += 1
            index_low += 1
            count += 1
        else:
            index_fat += 1 # 아닐 시에 무거운 사람 리스트 가벼운 쪽으로 이동
    print(count)
    answer += (length_low - count) // 2 # limit 보다 작은 수들 합쳐서 더 해준다.
    answer += length_fat - count # limit 보다 큰 수들 다 더해준다
    answer += count # 앞서 같이 묶어줬던 수 들의 합을 더해준다

    if (length_low - count) % 2 == 1: answer += 1

    return answer


print(solution([70, 50, 80], 100))
print(solution([10,20,30,40,50,60,70,80,90], 100))
