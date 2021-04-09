try_n = int(input())

right_answer =[]
for i in range(try_n):
    s,e = map(int, input().split())

    n=1
    for k in range(1,e+1):
       n = n*k
    e_f = n

    n = 1
    for k in range(1,e-s+1):
       n = n*k
    e_s_f = n

    n = 1
    for k in range(1,s+1):
       n = n*k
    s_f = n
    number = int(e_f/(e_s_f*s_f))

    right_answer.append(number)

for i in right_answer:
    print(i)