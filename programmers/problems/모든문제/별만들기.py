def down_grade(floor, star):
    cnt = True
    down_floor = ""
    for e in floor:
        if e == "*":
            down_floor = ''.join([down_floor, " "])
        elif e == " " and cnt == True:
            down_floor = ''.join([down_floor, "*"])
            cnt = False
        elif e == " " and cnt == False:
            down_floor = ''.join([down_floor, " "])
            cnt = True
    return down_floor


def solution(n):
    answer = []
    last_floor_num = 2 ** (n - 1)
    star = '* '
    last_floor = star * last_floor_num
    last_floor = last_floor[:-1]
    print(last_floor)
    for i in range(n):
        answer.append(last_floor)
        last_floor = down_grade(last_floor, star)

    return answer


print(solution(3))
