def down_grade(floor, n):
    cnt = True
    start = False
    down_floor = ""
    floors = 0
    for e in floor:
        if e == "*":
            down_floor = ''.join([down_floor, " "])
            start = True
        elif e == " " and cnt == True and start == True:
            down_floor = ''.join([down_floor, "*"])
            cnt = False
            floors += 1
        elif e == " " and cnt == False and start == True:
            down_floor = ''.join([down_floor, " "])
            cnt = True

        if floors == n: break
    return down_floor


def solution(n):
    answer = []
    last_floor_num = 2 ** (n - 1)
    star = '* '
    last_floor = star * last_floor_num
    last_floor = last_floor[:-1]
    print(last_floor)
    for i in range(1 ,n):
        answer.append(last_floor)
        last_floor = down_grade(last_floor, 2**(n-1-i))
    answer.append(last_floor)

    return answer


print(solution(3))
