#
#
#
#
#
#
#
#
#
#
#
#
import math


def solution(width, height, diagonals):
    answer = []

    for dia in diagonals:
        start_to_dia = []
        dia_to_end = []
        # 대각선 하나씩 구해주기
        for i in [[1, 0], [0, 1]]:
            dia_1 = [dia[0] - i[0], dia[1] - i[1]]
            mid_route = math.factorial(dia_1[0] + dia_1[1]) / (
                        math.factorial(dia_1[0]) * math.factorial(dia_1[1]))  # 나중 end_route 곱
            start_to_dia.append(mid_route)

            w, h = width - dia_1[0], height - dia_1[1]  # 대각선지나고 난 후 계산
            end_route = math.factorial(w + h) / (math.factorial(w) * math.factorial(h))
            dia_to_end.append(end_route)
        # 값 들 대칭으로 곱해주기
        total = start_to_dia[0] * dia_to_end[1] + start_to_dia[1] * dia_to_end[0]
        answer.append(total)

    return answer


print(solution(2, 2, [[1, 1], [2, 2]]))
print(solution(51, 37, [[17, 19]]))
