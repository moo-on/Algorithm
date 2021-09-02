# ["abab","bbaa","bababa","bbbabababbbaa"] [true,false,false,true]


def solution(a):
    answer = []
    for s in a:
        while len(s)>=2:
            if s[0] == 'a' or s[-1] == 'a':
                s = s.strip("a")
            elif s[0] == 'b' and s[-1] == 'b':
                s = ''.join([s[1:-1]])
        if s =='a':
            answer.append(True)
        else :
            answer.append(False)
    return answer

print(solution(["abab","bbaa","bababa","bbbabababbbaa"]))

