from itertools import permutations
import math

def solution(input):
    def prime_n(n):
        if n == (0 or 1) : return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0 : return False
        return True

    input = int("".join(list(sorted(input, reverse=True))))
    s_input = list(str(input))

    answer = 0
    answer_lst = []
    for i in range(1, len(s_input) + 1):
        lst = permutations(s_input, i)
        for e in lst:
            if e[0] == '0': continue
            answer_lst.append(int("".join(e)))

    for e in set(answer_lst):
        if prime_n(e) == True:
            answer +=1
    return answer

print(solution('011'))