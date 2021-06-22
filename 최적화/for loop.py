import time

lst = [0] * 10000000

#case1
answer = []
start = time.time()
for i in range(len(lst)):
    answer.append(lst[i])
print(time.time()-start)

#case2
answer = []
start = time.time()
for i in lst:
    answer.append(i)
print(time.time()-start)

# index의 접근보다 직접적인 할당이 더 빠르다.