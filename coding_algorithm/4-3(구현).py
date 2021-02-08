import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())

x, y, dir = map(int, input().split())

input_lst = [list(map(int, input().split())) for _ in range(N)]
check_lst = [[0]*M for _ in range(N)]

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def go():
    global dir
    dir -= 1
    if dir ==-1:
        dir =3

count = 1
check = 0

check_lst[x][y] = 1
while True:
    go()
    nx = x + dx[dir]
    ny = y + dy[dir]

    if check_lst[nx][ny] == 0 and input_lst[nx][ny]==0:
        x = nx
        y = ny
        count += 1
        check_lst[nx][ny] = 1
        check = 0
    else:
        check += 1

    if check ==4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        if input_lst[nx][ny] ==0 :
            x = nx
            y = ny
        else:
            break
        check = 0

print(count)

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

# 7 7 1 1 0
# 1 1 1 1 1 1 1
# 1 0 0 1 1 1 1
# 1 0 0 1 1 1 1
# 1 1 0 1 1 1 1
# 1 1 0 1 1 1 1
# 1 1 0 0 1 1 1
# 1 1 1 1 1 1 1
