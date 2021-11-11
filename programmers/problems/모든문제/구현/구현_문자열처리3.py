# ["A B C D", "A D", "A B D", "B D"]	2	7
# ["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"]	3	8

from collections import defaultdict


def solution(id_list, k):
    answer = 0
    customer_dict = defaultdict(int)

    for strings in id_list:
        day_lst = set(strings.split())
        for e in day_lst:
            customer_dict[e] += 1

    for i in customer_dict.values():
        if i > k: i = k
        answer += i

    return answer


print(solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3))
