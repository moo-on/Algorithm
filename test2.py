
def solution(numbers):
    answer = 0
    _set = set(numbers)

    for i in range(1,10):
        if i not in _set: answer += i
    return answer

print(solution([1,2,3,4,6,7,8,0]))