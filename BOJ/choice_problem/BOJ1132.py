import sys

input = sys.stdin.readline

# 입력 : 문자 개수와 문자
n = int(input())
lst = [list(input().rstrip()) for _ in range(n)]

# 각 알파벳의 우선순위를 정하기 위한 리스트 & 정한 리스트를 통해 각 알파벳에 숫자를 배당할 리스트
discri = [0 for _ in range(10)]
discri_ans = [0 for _ in range(10)]

# 우선순위를 정하기 위해 앞자리에 알파벳이 많이 나올수록 큰 숫자
s = ord('A')
for L in lst:
    length = len(L)
    for e in L:
        discri[ord(e)-s] += 10**length
        length -=1

# 우선순위를 정한 리스트를 통해 각 알파벳에 숫자 배당
discri_sort = sorted(discri, reverse=True)
print(discri)
print(discri_sort)
for i in range(len(discri)):
    idx = discri.index(max(discri_sort))

    discri_ans[idx] = 9-i
    print(idx,"__",9-i )

    discri_sort = discri_sort[1:]

print(discri_ans)
# 앞에 0이오면 안되는것들 삭제
# # 첫번째 문자 배당
lst_first = []
for i in range(n):
    lst_first.append(ord(lst[i][0]) - s)
for _ in range(10):
    i = 1
    idx = discri_ans.index(0)
    if idx in lst_first:
        idx_2 = discri_ans.index(i)
        discri_ans[idx], discri_ans[idx_2] = discri_ans[idx_2], discri_ans[idx]
        i += 1
    else:
        break

# 정답 출력
answer =[]
for L in lst:
    lis = []
    strings =''
    for e in L:
        lis.append(str(discri_ans[ord(e)-s]))
    strings = ''.join(lis)
    answer.append(int(strings))
print(discri_ans)

print(sum(answer))


# 2
# ABC
# BCA
# 3
# ABCDEFGHIJ
# JCD
# IGH
