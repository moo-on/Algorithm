MAX = 0


def dfs(k, dungeons, n):
    global MAX
    if MAX < n:
        MAX = n
    for i, e in enumerate(dungeons):
        if k < e[0]:
            continue
        else:
            dfs(k - e[1], dungeons[:i] + dungeons[i + 1:], n + 1)


def solution(k, dungeons):
    answer = -1
    dfs(k, dungeons, 0)
    return MAX