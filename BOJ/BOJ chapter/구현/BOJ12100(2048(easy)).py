# 3
# 2 2 2
# 4 4 4
# 8 8 8

# 3
# 0 2 2
# 4 0 4
# 8 8 0


import copy

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
MAX = 0
def rotate(m):
    g = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            g[c][N-1-r] = m[r][c]
    return g

def left(t, graph):

    if t == 5:
        global MAX
        for l in graph:
            if max(l) > MAX:
                MAX = max(l)
        return
    g = copy.deepcopy(graph)
    for i in range(N):
        temp = []
        for e in g[i]:
            if e != 0:
                temp.append(e)
        temp.extend([0] * (len(g[i]) - len(temp)))
        g[i] = copy.deepcopy(temp)

    for i in range(N):
        for j in range(N-1):
            if g[i][j] == g[i][j+1]:
                g[i][j] = g[i][j] + g[i][j+1]
                del g[i][j+1]
                g[i].append(0)

    left(t+1, g)
    right(t+1,g)
    up(t+1, g)
    down(t+1, g)


def right(t, graph):
    if t == 5:
        global MAX
        for l in graph:
            if max(l) > MAX:
                MAX = max(l)
        return

    g = copy.deepcopy(graph)
    g = rotate(g)
    g = rotate(g)

    for i in range(N):
        temp = []
        for e in g[i]:
            if e != 0:
                temp.append(e)
        temp.extend([0] * (len(g[i]) - len(temp)))
        g[i] = copy.deepcopy(temp)

    for i in range(N):
        for j in range(N-1):
            if g[i][j] == g[i][j+1]:
                g[i][j] = g[i][j] + g[i][j+1]
                del g[i][j+1]
                g[i].append(0)

    g = rotate(g)
    g = rotate(g)

    left(t + 1, g)
    right(t + 1, g)
    up(t + 1, g)
    down(t + 1, g)




def up(t, graph):
    if t == 5:
        global MAX
        for l in graph:
            if max(l) > MAX:
                MAX = max(l)
        return
    g = copy.deepcopy(graph)
    g = rotate(g)
    g = rotate(g)
    g = rotate(g)
    for i in range(N):
        temp = []
        for e in g[i]:
            if e != 0:
                temp.append(e)
        temp.extend([0] * (len(g[i]) - len(temp)))
        g[i] = copy.deepcopy(temp)

    for i in range(N):
        for j in range(N-1):
            if g[i][j] == g[i][j+1]:
                g[i][j] = g[i][j] + g[i][j+1]
                del g[i][j+1]
                g[i].append(0)

    g = rotate(g)

    left(t + 1, g)
    right(t + 1, g)
    up(t + 1, g)
    down(t + 1, g)




def down(t, graph):
    if t == 5:
        global MAX
        for l in graph:
            if max(l) > MAX:
                MAX = max(l)
        return
    g = copy.deepcopy(graph)
    g = rotate(g)
    for i in range(N):
        temp = []
        for e in g[i]:
            if e != 0:
                temp.append(e)
        temp.extend([0] * (len(g[i]) - len(temp)))
        g[i] = copy.deepcopy(temp)

    for i in range(N):
        for j in range(N-1):
            if g[i][j] == g[i][j+1]:
                g[i][j] = g[i][j] + g[i][j+1]
                del g[i][j+1]
                g[i].append(0)

    g = rotate(g)
    g = rotate(g)
    g = rotate(g)

    left(t + 1, g)
    right(t + 1, g)
    up(t + 1, g)
    down(t + 1, g)

down(0,lst)
left(0, lst)
right(0, lst)
up(0, lst)

print(MAX)






