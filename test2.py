import sys

input = sys.stdin.readline

# 입력 : 문자 개수와 문자
n = int(input())
lst = [list(input().rstrip()) for _ in range(n)]

# 각 알파벳의 우선순위를 정하기 위한 리스트 & 정한 리스트를 통해 각 알파벳에 숫자를 배당할 리스트
discri = dict([[chr(65+i),0] for i in range(10)])
discri_ans = dict([[chr(65+i),1] for i in range(10)])

# 우선순위를 정하기 위해 앞자리에 알파벳이 많이 나올수록 큰 숫자
for L in lst:
    length = len(L)
    for e in L:
        discri[e] = 10**length + discri[e]
        length -=1

#앞자리에 0이 오면 안되는 아이들
lst_first = [lst[i][0] for i in range(n)]
print(lst_first)

# 우선순위를 정한 리스트를 통해 각 알파벳에 숫자 배당
discri_sort = dict(sorted(discri.items(), key=lambda x: x[1]))


k_0 = 'a'
for k, v in discri_sort.items():
    if k  not in lst_first:
        discri_ans[k] = 0
        k_0 = k
        break

if k_0 != k:
    for k, v in discri_sort.items():
        discri_ans[k] = 0
        k_0 = k
        break

i = 1
for k,v in discri_sort.items():
    if k == k_0: continue
    discri_ans[k] = i
    i+=1

print(discri_ans)

# 정답 출력
answer =[]
for L in lst:
    lis = []
    strings =''
    for e in L:
        lis.append(str(discri_ans.get(e)))
    strings = ''.join(lis)
    answer.append(int(strings))

answer = sum(answer)

print(answer)
# 2
# ABC
# BCA
# 3
# ABCDEFGHIJ
# JCD
# IGH

# 4
# ABCDEFGHIJ
# JCD
# ICD
# H