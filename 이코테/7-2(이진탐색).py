import sys
input= sys.stdin.readline

n = int(input())
input_lst = list(map(int, input().split()))

m = int(input())
check_lst = list(map(int, input().split()))

input_lst = set(input_lst)
for e in check_lst:
    print("yes") if e in input_lst else print("no")