def down_grade(floor, n):
    down_floor = [" " for _ in range(2 ** n - 1)]
    check_lst = []
    check = 0
    cnt = 0

    for i, e in enumerate(floor):
        if e == " ": continue

        if e == "*" and cnt < 2:
            cnt += 1

        if e == "*" and cnt == 2:
            check_lst.append(int((check + i) / 2))
            cnt = 0

        check = i

    for i in check_lst:
        down_floor[i] = "*"

    return ''.join(down_floor)


def solution(n):
    answer = []
    last_floor_num = 2 ** (n - 1)
    star = '* '
    last_floor = (star * last_floor_num).rstrip()

    for i in range(n):
        answer.append(last_floor)
        last_floor = down_grade(last_floor, n)
    answer.reverse()

    for i in answer:
        print(i)

    return


print(solution(3))
