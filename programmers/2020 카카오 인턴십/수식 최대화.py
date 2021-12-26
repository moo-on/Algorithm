import re
from itertools import permutations


def calc(expression, operators, n):
    if n == 3: return abs(int(expression[0]))

    operator = operators[n]
    complete_expression = []
    for i in range(len(expression)):
        if expression[i] == operator:
            complete_expression.append(
                str(eval(''.join([complete_expression.pop(), expression[i], expression[i + 1]]))))
        elif expression[i - 1] == operator:
            continue
        else:
            complete_expression.append(expression[i])

    return calc(complete_expression, operators, n + 1)


def solution(expression):
    answer = []

    operators = [e for e in expression if not e.isalnum()]
    expressions = re.split("[+*-]", expression)

    expression = []
    for o, e in zip(operators, expressions):
        expression.append(e)
        expression.append(o)
    expression.append(expressions[-1])

    for operator_set in permutations(["*", "+", "-"]):
        answer.append(calc(expression, operator_set, 0))

    return max(answer)


print(solution("100-200*300-500+20"))