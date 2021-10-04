import sys
input = sys.stdin.readline

input_lst = list(input().rstrip())

location = [int(ord(input_lst[0]))-96, int(input_lst[1])]

moving_case = [[-2,-1],[-2,+1],[2,-1],[2,1],[-1,-2],[-1,2],[1,2],[1,-2]]

number_case=0
for e in moving_case:
    check_lst = [location[i] + e[i] for i in range(len(location))]
    if 9>check_lst[0]>0 and 9>check_lst[1]>0 : number_case+=1

print(number_case)


