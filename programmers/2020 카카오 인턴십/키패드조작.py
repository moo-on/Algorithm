def solution(numbers, hand):
    if hand == "right":
        hand = "R"
    else:
        hand = "L"
    answer = []
    nl, nr = 10, 12
    left_right = set([1, 4, 7, 10, 3, 6, 9, 12])

    for n in numbers:
        # 147 369일 경우
        if n in left_right:
            if n % 3 == 0:
                answer.append("R")
                nr = n
            else:
                answer.append("L")
                nl = n
            continue

        # 2580의 경우
        if n == 0: n = 11

        dl = sum(divmod(abs(nl - n), 3))
        dr = sum(divmod(abs(nr - n), 3))

        if dl == dr:
            if hand == "R":
                answer.append("R")
                nr = n
            else:
                answer.append("L")
                nl = n

        elif dl < dr:
            answer.append("L")
            nl = n

        else:
            answer.append("R")
            nr = n

    return ''.join(answer)


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
