# ["AAAACX", "AAAACX", "AAAACX", "ZZZZZX", "ATTTTX", "XUUUUU"]	[1, 2, 4]	[2, 3]	4
# ["KKKK", "KKKK", "KKKK", "FGHI"]	[2, 3]	[2]	2
# ["KKK", "KKK", "KKK"]	[2]	[2]	1


def solution(cakes, cut_rows, cut_columns):
    answer = []
    temp_lst = []
    prev_row = 0
    for row in cut_rows:
        cake = cakes[prev_row:row]


        prev_column = 0
        for column in cut_columns:
            temp = []
            for e in cake:
                temp.append(e[prev_column:column])
            prev_column = column
            check = "".join(temp)
            temp_lst.append(len(set(list(check))))

        temp = []
        for e in cake:
            temp.append(e[prev_column:])

        check = "".join(temp)
        temp_lst.append(len(set(list(check))))

        prev_row = row

    cake = cakes[prev_row:]

    prev_column = 0
    for column in cut_columns:
        temp = []
        for e in cake:
            temp.append(e[prev_column:column])
        prev_column = column
        check = "".join(temp)
        temp_lst.append(len(set(list(check))))

    temp = []
    for e in cake:
        temp.append(e[prev_column:])

    check = "".join(temp)
    temp_lst.append(len(set(list(check))))

    return max(temp_lst)


print(solution(["AAAACX", "AAAACX", "AAAACX", "ZZZZZX", "ATTTTX", "XUUUUU"], [1, 2, 4], [2, 3]))
