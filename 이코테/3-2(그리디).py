import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

input_lst = list(map(int, input().split()))
input_lst.sort()

stack = 0
answer_lst = []
while (m > 0):
    m -= 1

    if stack < k:
        answer_lst.append(input_lst[n - 1])
        stack += 1

    else:
        answer_lst.append(input_lst[n - 2])
        stack =0

print(sum(answer_lst))
