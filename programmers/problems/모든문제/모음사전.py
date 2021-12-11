#
#
#
#
#
#

available = ['A', 'E', 'I', 'O', 'U']
order = []


def dfs(n, word):
    if n == 5:
        return
    for alpha in available:
        order.append(word + alpha)
        dfs(n + 1, word + alpha)


def solution(word):
    dfs(0, "")

    return order.index(word)+1


print(solution("I"))
