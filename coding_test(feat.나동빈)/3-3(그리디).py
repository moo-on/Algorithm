import sys

input = sys.stdin.readline

n,m = map(int, input().split())

input_lst = []

for _ in range(n):
    input_lst.append(list(map(int, input().split())))

min_lst=[]
for i in range(len(input_lst)):
    min_lst.append(min(input_lst[i]))

print(max(min_lst))