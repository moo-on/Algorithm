# [93, 30, 55]	[1, 30, 5]	[2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    lst = []
    time_lst = [math.ceil((100-p) / s) for p, s in zip(progresses, speeds)]

    for e in time_lst:
        if not lst:
            lst.append(e)
            continue

        if lst[0] < e:
            answer.append(len(lst))
            lst = [e]
        else:
            lst.append(e)

    answer.append(len(lst))
    return answer

lst =[1,2,3]
print(lst[:0])

if __name__ == "__main__":
    # [93, 30, 55]	[1, 30, 5]	[2, 1]
    # [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
    # [99, 1, 99, 1] [1, 1, 1, 1] [1, 3]
    input1 = [99, 1, 99, 1]
    input1_1 = [1, 1, 1, 1]
    print(solution(input1, input1_1))

