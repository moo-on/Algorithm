def solution(S):
    answer = 0
    length = len(S)
    lst = []
    temp = []

    for i in range(1, int(length // 2) + 1):

        if i != 1:
            if not temp:
                lst.append(length)
            else:

                m = 0
                for l in temp:
                    a = len(l[0] * l[1])
                    b = len(l[0]) + len(str(l[1]))
                    m += (a - b)
                lst.append(length - m)

        s = 0
        e = i
        temp = []

        while e <= length:
            # i = 2

            if temp:
                if S[s:e] == temp[-1][0]:
                    temp[-1][1] += 1
                    s = e
                    e = e + i
                    continue

            if e + i > length: break

            if S[s:e] == S[e:e + i]:

                temp.append([S[s:e], 2])
                s = e + i
                e = e + i + i
            else:
                s += 1
                e += 1

    if temp:

        m = 0
        for l in temp:
            a=len(l[0] * l[1])
            b=len(l[0]) + len(str(l[1]))
            m +=  a-b
        lst.append(length - m)
    answer = min(lst)
    return answer

print(solution("ababcdcdababcdcd"))


for i in range(0,8, 5):
    print(i)