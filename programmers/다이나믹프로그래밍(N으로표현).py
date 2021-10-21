#  5	12	4
# 2	11	3

def solution(N, number):
    if N == number: return 1
    lst_set = [set() for _ in range(9)]
    lst_set[1].add(N)

    # 2~8까지 조합 찾기
    for i in range(2, 9):
        j = i // 2  # i=2 j=1, i=3 j=1, i=4 j=2
        lst_set[i].add(int(str(N) * i))
        for k in range(1, j + 1):
            # i = 5 -> k=1 i-k=4, k=2 i-k=3
            for e1 in lst_set[k]:
                for e2 in lst_set[i - k]:
                    lst_set[i].add(e1 * e2)
                    lst_set[i].add(e1 + e2)
                    lst_set[i].add(e1 - e2)
                    lst_set[i].add(-e1 + e2)
                    if e2 != 0: lst_set[i].add(e1 // e2)
                    if e1 != 0: lst_set[i].add(e2 // e1)

                    if number in lst_set[i]: return i
    return -1


print(solution(5, 12))
print(solution(2, 11))
print(solution(8, 53))
