#1150

import sys
import itertools

sys.setrecursionlimit(1000)

#input = sys.stdin.readline

#case = int(input())


def re_duplicate(lst):
    copy_lst = lst.copy()
    for group in copy_lst:
        for e in group:
            if e + 1 in group:
                lst.remove(group)
                break
    return lst


def answer(group, d_lst):
    lst = []
    for elements in group:
        sum = 0
        for e in elements:
            sum += d_lst[e]
        lst.append(sum)

    ans = min(lst)
    return ans


def comb2(lst, n):
    a = itertools.combinations(lst, n)
    e = []
    for i in a:
        e.append(list(i))
    return e


# n, k = map(int, input().split())
#
# d = []
# for i in range(n):
#     d.append(int(input("입력하세요 %d" %i)))
#
#
# distance = [d[i + 1] - d[i] for i in range(len(d) - 1)]
#
# n_lst = [i for i in range(len(d) - 1)]
# print("step1")
# g = comb2(n_lst, k)
# print("step2")
# g = re_duplicate(g)
# print("step3")
# ans = answer(g, distance)
# print("step4")
# print(ans)