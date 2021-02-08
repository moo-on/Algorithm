import sys

input = sys.stdin.readline

n = int(input())

input_lst =[]
for _ in range(2):
    name, age = input().split()
    input_lst.append([name, int(age)])

input_lst = sorted(input_lst, key = lambda student: student[1])
print(input_lst)



# 홍길동 100
# 가나다 30