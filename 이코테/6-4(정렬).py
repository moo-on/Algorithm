import sys

input = sys.stdin.readline

# 입력문
n, k = map(int, input().split())
input_lst = [list(map(int, input().split())) for _ in range(2)]

# 정렬
input_lst[0].sort()
input_lst[1].sort(reverse= True)

# 교체
count = 0

for i in range(n):
    if input_lst[0][i] < input_lst[1][count]:
        input_lst[0][i] = input_lst[1][count]
        count += 1
    if count == k: break

print(input_lst[0])
print(sum(input_lst[0]))
