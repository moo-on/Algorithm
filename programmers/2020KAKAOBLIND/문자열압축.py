def solution(S):
    answer = []
    lst = []

    for i in range(1, len(S) // 2 + 2):
        s = 0
        e = i
        temp = []
        while True:
            temp.append(S[s:e])
            s = s + i
            e = e + i
            if e >= len(S):
                temp.append(S[s:])
                break
        lst.append(temp)

    answer_lst = []
    temp_lst = []
    t = ""

    for l in lst:
        temp_lst.append([l[0], 0])
        for e in l:
            if temp_lst[-1][0] == e:
                temp_lst[-1][1] += 1
            else:
                temp_lst.append([e, 1])

        # temp_lst길이계산
        if temp_lst:
            answer_lst = []
            for ll in temp_lst:
                if ll[1] == 1:
                    answer_lst.append(ll[0])
                else:
                    ll[1] = str(ll[1])
                    answer_lst.append(''.join(ll))

            answer.append(len(''.join(answer_lst)))
            temp_lst = []

    return min(answer)