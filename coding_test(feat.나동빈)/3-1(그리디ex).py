import sys

input = sys.stdin.readline

input_lst = list(map(int, input().rstrip()))

answer = input_lst[0]
for i in range(len(input_lst)-1):
    if input_lst[i] == 0 or input_lst[i] == 1 :
        answer += input_lst[i+1]
    else :
        answer *= input_lst[i+1]

print(answer)

