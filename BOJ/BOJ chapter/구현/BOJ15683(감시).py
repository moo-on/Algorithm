import copy

row, column = input().split()
row = int(row)
column = int(column)
m = [list(map(int, input().split())) for _ in range(row)]
answer_lst = []

def func1(index_t, m_t, command):
    global column
    global row
    command = index_t[0]
    r = command[1]
    c = command[2]

    m_t1 = copy.deepcopy(m_t)
    m_t2 = copy.deepcopy(m_t)
    m_t3 = copy.deepcopy(m_t)
    m_t4 = copy.deepcopy(m_t)

    # row1
    for i_l in range(c, -1, -1):
        if m_t1[r][i_l] == 0:
            m_t1[r][i_l] = '#'
        elif m_t1[r][i_l] == 6:
            break

    # row2
    for i_r in range(c, column):
        if m_t2[r][i_r] == 0:
            m_t2[r][i_r] = '#'
        elif m_t2[r][i_r] == 6:
            break

    # column1
    for i_u in range(r, -1, -1):
        if m_t3[i_u][c] == 0:
            m_t3[i_u][c] = '#'
        elif m_t3[i_u][c] == 6:
            break

    # column2
    for i_d in range(r, row):
        if m_t4[i_d][c] == 0:
            m_t4[i_d][c] = '#'
        elif m_t4[i_d][c] == 6:
            break

    index_t.pop(0)
    dfs(index_t, m_t1)
    dfs(index_t, m_t2)
    dfs(index_t, m_t3)
    dfs(index_t, m_t4)


def func2(index_t, m_t, command):
    global column
    global row
    command = index_t[0]
    r = command[1]
    c = command[2]

    m_t1 = copy.deepcopy(m_t)
    m_t2 = copy.deepcopy(m_t)

    # row1
    for i_l in range(c, -1, -1):
        if m_t1[r][i_l] == 0:
            m_t1[r][i_l] = '#'
        elif m_t1[r][i_l] == 6:
            break

    for i_r in range(c, column):
        if m_t1[r][i_r] == 0:
            m_t1[r][i_r] = '#'
        elif m_t1[r][i_r] == 6:
            break

    # column1
    for i_u in range(r, -1, -1):
        if m_t2[i_u][c] == 0:
            m_t2[i_u][c] = '#'
        elif m_t2[i_u][c] == 6:
            break

    for i_d in range(r, row):
        if m_t2[i_d][c] == 0:
            m_t2[i_d][c] = '#'
        elif m_t2[i_d][c] == 6:
            break

    index_t.pop(0)
    dfs(index_t, m_t1)
    dfs(index_t, m_t2)


def func3(index_t, m_t, command):
    global column
    global row
    command = index_t[0]
    r = command[1]
    c = command[2]

    m_t1 = copy.deepcopy(m_t)
    m_t2 = copy.deepcopy(m_t)
    m_t3 = copy.deepcopy(m_t)
    m_t4 = copy.deepcopy(m_t)

    # row1
    for i_l in range(c, -1, -1):
        if m_t1[r][i_l] == 0:
            m_t1[r][i_l] = '#'
        elif m_t1[r][i_l] == 6:
            break

    for i_u in range(r, -1, -1):
        if m_t1[i_u][c] == 0:
            m_t1[i_u][c] = '#'
        elif m_t1[i_u][c] == 6:
            break

    # row2
    for i_l in range(c, -1, -1):
        if m_t2[r][i_l] == 0:
            m_t2[r][i_l] = '#'
        elif m_t2[r][i_l] == 6:
            break

    for i_d in range(r, row):
        if m_t2[i_d][c] == 0:
            m_t2[i_d][c] = '#'
        elif m_t2[i_d][c] == 6:
            break

    # row3
    for i_r in range(c, column):
        if m_t3[r][i_r] == 0:
            m_t3[r][i_r] = '#'
        elif m_t3[r][i_r] == 6:
            break

    for i_u in range(r, -1, -1):
        if m_t3[i_u][c] == 0:
            m_t3[i_u][c] = '#'
        elif m_t3[i_u][c] == 6:
            break

    # column4
    for i_r in range(c, column):
        if m_t4[r][i_r] == 0:
            m_t4[r][i_r] = '#'
        elif m_t4[r][i_r] == 6:
            break

    for i_d in range(r, row):
        if m_t4[i_d][c] == 0:
            m_t4[i_d][c] = '#'
        elif m_t4[i_d][c] == 6:
            break

    index_t.pop(0)
    dfs(index_t, m_t1)
    dfs(index_t, m_t2)
    dfs(index_t, m_t3)
    dfs(index_t, m_t4)


def func4(index_t, m_t, command):
    global column
    global row
    command = index_t[0]
    r = command[1]
    c = command[2]

    m_t1 = copy.deepcopy(m_t)
    m_t2 = copy.deepcopy(m_t)
    m_t3 = copy.deepcopy(m_t)
    m_t4 = copy.deepcopy(m_t)

    # row1
    for i_l in range(c, -1, -1):
        if m_t1[r][i_l] == 0:
            m_t1[r][i_l] = '#'
        elif m_t1[r][i_l] == 6:
            break

    for i_r in range(c, column):
        if m_t1[r][i_r] == 0:
            m_t1[r][i_r] = '#'
        elif m_t1[r][i_r] == 6:
            break

    for i_u in range(r, -1, -1):
        if m_t1[i_u][c] == 0:
            m_t1[i_u][c] = '#'
        elif m_t1[i_u][c] == 6:
            break

    # row2
    for i_l in range(c, -1, -1):
        if m_t2[r][i_l] == 0:
            m_t2[r][i_l] = '#'
        elif m_t2[r][i_l] == 6:
            break

    for i_r in range(c, column):
        if m_t2[r][i_r] == 0:
            m_t2[r][i_r] = '#'
        elif m_t2[r][i_r] == 6:
            break

    for i_d in range(r, row):
        if m_t2[i_d][c] == 0:
            m_t2[i_d][c] = '#'
        elif m_t2[i_d][c] == 6:
            break

    # row3
    for i_r in range(c, column):
        if m_t3[r][i_r] == 0:
            m_t3[r][i_r] = '#'
        elif m_t3[r][i_r] == 6:
            break

    for i_u in range(r, -1, -1):
        if m_t3[i_u][c] == 0:
            m_t3[i_u][c] = '#'
        elif m_t3[i_u][c] == 6:
            break

    for i_d in range(r, row):
        if m_t3[i_d][c] == 0:
            m_t3[i_d][c] = '#'
        elif m_t3[i_d][c] == 6:
            break

    # column4
    for i_l in range(c, -1, -1):
        if m_t4[r][i_l] == 0:
            m_t4[r][i_l] = '#'
        elif m_t4[r][i_l] == 6:
            break

    for i_d in range(r, row):
        if m_t4[i_d][c] == 0:
            m_t4[i_d][c] = '#'
        elif m_t4[i_d][c] == 6:
            break

    for i_u in range(r, -1, -1):
        if m_t4[i_u][c] == 0:
            m_t4[i_u][c] = '#'
        elif m_t4[i_u][c] == 6:
            break

    index_t.pop(0)
    dfs(index_t, m_t1)
    dfs(index_t, m_t2)
    dfs(index_t, m_t3)
    dfs(index_t, m_t4)


def func5(index_t, m_t, command):
    global column
    global row
    command = index_t[0]
    r = command[1]
    c = command[2]

    # row
    for i_l in range(c, -1, -1):
        if m_t[r][i_l] == 0:
            m_t[r][i_l] = '#'
        elif m_t[r][i_l] == 6:
            break

    for i_r in range(c, column):
        if m_t[r][i_r] == 0:
            m_t[r][i_r] = '#'
        elif m_t[r][i_r] == 6:
            break
    # column
    for i_u in range(r, -1, -1):
        if m_t[i_u][c] == 0:
            m_t[i_u][c] = '#'
        elif m_t[i_u][c] == 6:
            break

    for i_d in range(r, row):
        if m_t[i_d][c] == 0:
            m_t[i_d][c] = '#'
        elif m_t[i_d][c] == 6:
            break

    index_t.pop(0)
    dfs(index_t, m_t)

def dfs(index, m):
    global column
    global row
    if not index:
        answer = 0
        for l in m:
            answer += l.count(0)
        answer_lst.append(answer)
        return

    index_t = copy.deepcopy(index)
    m_t = copy.deepcopy(m)

    command = index_t[0]

    if command[0] == 1:
        func1(index_t, m_t, command)
    elif command[0] == 2:
        func2(index_t, m_t, command)
    elif command[0] == 3:
        func3(index_t, m_t, command)
    elif command[0] == 4:
        func4(index_t, m_t, command)
    elif command[0] == 5:
        func5(index_t, m_t, command)

index = []

for r in range(row):
    for c in range(column):
        if m[r][c] != 0 and m[r][c] != 6:
            index.append([m[r][c], r, c])

dfs(index, m)

print(min(answer_lst))


