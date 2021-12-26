import re


def solution(expression):
    answer = []

    # 곱하기 젤 나중에, 플러스 마이너스 먼저
    # 마이너스 먼저 곱하기 더하기
    # 플러스 먼저 곱하기 마이너스
    operators = []
    for e in expression:
        if not e.isalnum():
            operators.append(e)

    rm_multiple = expression.split("*")

    #  기본
    answer.append(abs(eval(expression)))

    #  곱하기 젤 나중에
    temp_lst = []
    for express in rm_multiple:
        temp_lst.append(str(eval(express)))
    answer.append(abs(eval('*'.join(temp_lst))))

    #  마이너스 > 곱하기 > 더하기
    temp_express = []
    for express in re.split("[*+]", expression):
        temp_express.append(str(eval(express)))

    temp_operator = []
    for operator in operators:
        if operator == "-":
            continue
        temp_operator.append(operator)

    temp_lst = []
    for express, operator in zip(temp_express, temp_operator):
        temp_lst.append(express + operator)
    temp_lst.append(temp_express[-1])

    answer.append(abs(eval(''.join(temp_lst))))

    #  더하기 > 곱하기 > 마이너스
    temp_express = []
    for express in re.split("[*-]", expression):
        temp_express.append(str(eval(express)))

    temp_operator = []
    for operator in operators:
        if operator == "+":
            continue
        temp_operator.append(operator)

    temp_lst = []
    for express, operator in zip(temp_express, temp_operator):
        temp_lst.append(express + operator)
    temp_lst.append(temp_express[-1])

    answer.append(abs(eval(''.join(temp_lst))))

    return max(answer)


print(solution("50*6-3*2"))
print(solution("100-200*300-500+20"))
print(solution("177-661*999*99-133+221+334+555-166-144-551-166*166-166*166-133*88*55-11*4+55*888*454*12+11-66+444*99"))



50 * 6 + 5

