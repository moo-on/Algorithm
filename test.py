import sys

n,k = map(int, input().split())


input_lst = []
for _ in range(n):
    input_lst.append(list(map(int,sys.stdin.readline().split())))

answer_lst = []
for idy in range(n):
    line = [0]*n*k
    for i in range(n):
        line[i*k:(i+1)*k] = [input_lst[idy][i]]*k
    for _ in range(k):
        answer_lst.append([line])

for i in answer_lst:
    print(i)




