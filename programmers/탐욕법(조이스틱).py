def solution(name):
    index_lst = []
    answer = []
    for i, e in enumerate(name):
        if e != 'A':
            index_lst.append(i)

    answer.append(index_lst[-1])  # straight
    for i, j in zip(index_lst, index_lst[1:]):
        reverse = (len(name)) - j + 2*i # (len(name) - 1) - j + i + 1 +i
        answer.append(reverse)
    answer = min(answer)

    for i in name:
        answer += min(abs(ord(i) - ord('A')), abs(ord('Z') - ord(i)) + 1)
    return answer

name = "JEROEN"
print(solution(name))




