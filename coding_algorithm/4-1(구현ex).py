import sys

input = sys.stdin.readline

#ex1
# n = int(input())
#
# input_lst = list(input().split())
#
# answer ={'x' : 1, 'y' :1}
#
# for i in input_lst:
#
#     if i == 'L':
#         if answer['x'] == 1 : continue
#         answer['x'] = answer['x'] - 1
#
#     if i == 'R':
#         if answer['x'] == n : continue
#         answer['x'] = answer['x'] + 1
#
#     if i == 'U':
#         if answer['y'] == 1 : continue
#         answer['y'] = answer['y'] -1
#
#     if i == 'D':
#         if answer['y'] == n : continue
#         answer['y'] = answer['y'] + 1
#
# print(list(answer.values()))










#ex2

n = int(input())

result = (n+1)*1575

if 23 <= n: result += 2025*3
elif 13 <= n: result += 2025*2
elif 3 <= n: result += 2025

print(result)


