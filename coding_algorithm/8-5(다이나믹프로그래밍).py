import sys
input = sys.stdin.readline

n, m = map(int, input().split())
input_lst = [int(input()) for _ in range(n)]

d = [10001]*10001
d[0] = 0


for e in input_lst:
    d[e] = 1
    for i in range(1, m+1):
        if i>e:
            d[i] = min(d[i-e] + 1, d[i])

print(d[m]) if d[m] != 10001 else print(-1)
