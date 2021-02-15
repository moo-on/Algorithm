import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
limit = int(input())

lst_sort = sorted(lst, reverse= True)
lst_sort_ori = lst_sort.copy()
answer = []
answer_ori = lst_sort.copy()
i = 0
# 큰거 부터 하나 씩 옮김
for _ in range(len(lst) -1):
    for e in lst_sort_ori:
        index = lst.index(e)
        # 가장 큰 원소 옮길 수 있을 때
        if index <= limit and lst[0]<lst[index]:
            # 가능한 가장 큰 원소 정답문에 넣기
            answer.append(e)
            lst.remove(e)
            lst_sort.remove(e)
            limit -= index
    # 바꿀 기회를 다썼다면 반복문 끝내기
    if limit == 0: break
    if (answer + lst) == answer_ori: break
    # 첫번째 원소 못 바꿀 경우 반복
    # 첫번째 원소 정답문에 넣고 다음 원소 확인
    answer.append(lst[0])
    lst_sort.remove(lst.pop(0))
    lst_sort_ori = lst_sort.copy()


answer = answer + lst
for i in range(len(answer)):
    print(answer[i], end=' ')

# 1
# 13 9 7 19 21 6 3 145 28 67 1 59
# 13
# [145, 21, 13, 9, 7, 6, 3, 19, 28, 67, 1, 59]

