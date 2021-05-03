from collections import Counter
from itertools import combinations

'''
def solution(number, k):
    lst = list(combinations(list(number), k))
    answer = []
    for l in lst:
        string = ''.join(l)
        answer.append(int(string))
    return str(max(answer))
'''


def solution(number, k):
    lst = number
    answers = []
    lst_f = lst[:k + 1]
    index_l = 0

    while k != 0:
        index = lst_f.index(max(lst_f))
        answers.append(lst_f[index])
        index_l += index + 1
        k -= index
        lst_f = lst[index_l: index_l + k + 1]
        if len(answers) == len(number) - k: return "".join(map(str, answers))
    answers.extend(lst[index_l:])
    return ''.join(map(str, answers))


number = "99991"
number = '4177252841' #"775841"
k = 4 # 7752841 4개 뽑아서 없애기 7개 원소 고르기
print(solution(number,k))


def solution(number, k):
    # stack에 입력값을 순서대로 삽입
    stack = [number[0]]
    for num in number[1:]:
        # 들어오는 값이 stack 값보다 크면, 기존의 값을 제거하고 새로운 값으로 바꿈
        # 참고 : len(stack) > 0 == stack
        while len(stack) > 0 and stack[-1] < num and k > 0:
            # 값을 한개 빼서 k는 1이 제거
            k -= 1
            # 내부의 값을 제거
            stack.pop()
        # 새로운 값을 삽입
        stack.append(num)
    # 만일 충분히 제거하지 못했으면 남은 부분은 단순하게 삭제
    # 이렇게 해도 되는 이유는 이미 큰 수부터 앞에서 채워넣었기 때문
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


