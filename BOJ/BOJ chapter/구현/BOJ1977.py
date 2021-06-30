import sys
import math

input = sys.stdin.readline


n1 = int(input())
n2 = int(input())
answer = []

n = n1 ** 0.5
m = int(math.ceil(n))

n = n2 ** 0.5
M = int(math.floor(n))

if m ** 2 > n2:
    print(-1)
    quit()

answer = sum([i ** 2 for i in range(m, M + 1)])
print(answer)
print(m ** 2)

