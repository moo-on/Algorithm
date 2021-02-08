import sys
input = sys.stdin.readline

#입력
n = int(input())
input_lst = list(map(int, input().split()))

#세팅
d = [0]*100
d[0] = input_lst[0]
d[1] = max(input_lst[0], input_lst[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + input_lst[i])

print(d[n-1])