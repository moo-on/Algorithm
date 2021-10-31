input = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90",
         "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]

# 푼 문제 수가 같아야함(5문제 이상)
# 푼 문제 번호도 같다
# 푼 문제의 점수도 같다

from collections import defaultdict
from operator import itemgetter


def solution(logs):
    answer = [[] for _ in range(101)]
    students = defaultdict(list)

    for log in logs:
        log_lst = log.split()
        students[log_lst[0]].append([int(log_lst[1]), int(log_lst[2])])

    for key, values in students.items():
        values.sort(key=itemgetter(0))
        temp_dict = defaultdict(int)

        for lst in values:
            if temp_dict[lst[0]] < lst[1]:
                temp_dict[lst[0]] = lst[1]

        numbers = list(temp_dict.keys())
        scores = list(temp_dict.values())
        if len(numbers) >= 5:
            answer[len(numbers)].append([key, numbers, scores])

        cheater = set()
        for lst in answer:
            for log1 in lst:
                for log2 in lst:
                    if log1[0] == log2[0]:
                        continue
                    if log1[1] == log2[1] and log1[2] == log2[2]:
                        cheater.add(log1[0])
                        cheater.add(log2[0])
    if not cheater:
        return ["None"]
    return sorted(list(cheater))


print(solution(input))
