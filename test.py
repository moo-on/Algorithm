# "one4seveneight"
# 1478
# 0	zero
# 1	one
# 2	two
# 3	three
# 4	four
# 5	five
# 6	six
# 7	seven
# 8	eight
# 9	nine


def solution(s):
    dic_s = {'zero':0, 'one': 1,'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine': 9,}
    dic_i ={'1','2','3','4','5','6','7','8','9'}
    answer = []
    stack = ''
    for e in s:
        if e in dic_i:
            answer.append(e)
            continue
        else:
            stack = stack + e

        print(stack)

        if stack in dic_s:
            answer.append(str(dic_s[stack]))

            stack = ''

    return int(''.join(answer))


print(solution("one4seveneight"))

