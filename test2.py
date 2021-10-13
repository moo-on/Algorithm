

def solution(n):
    if n == 5: return

    solution(n+1)
    return n


print(solution(1))
