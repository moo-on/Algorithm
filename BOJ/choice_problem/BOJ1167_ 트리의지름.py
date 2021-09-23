# 5
# 1 3 2 -1
# 2 4 4 -1
# 3 1 2 4 3 -1
# 4 2 4 3 3 5 6 -1
# 5 4 6 -1

import sys
input = sys.stdin.readline
n = int(input())
array = [input().split() for _ in range(n)]

print(array)
