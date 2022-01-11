'''
종료 조건
    해당 경로가 더 비싼 루트
    벽에 막혀있다. & 격자 보다 크다
    목적지에 도착했을 때

다음 함수 부를 때
    비용(cost)
    위치(z, y, x)
    방향(dir)
z축 : row = 0, column = 1
'''
from collections import deque


def solution(board):
    answer = 987654321
    len_ = len(board)
    board_cost = [[[987654321 for _ in range(len_)] for _ in range(len_)] for _ in range(2)]
    # z  y  x  cost  dir
    q = deque([[0, 0, 1, 100], [1, 1, 0, 100]])

    while q:
        temp = q.popleft()
        z, y, x, cost = temp[0], temp[1], temp[2], temp[3]

        # termination condition
        if x == len_ - 1 and y == len_ - 1:  # encounter of destination
            if answer > cost:
                answer = cost
            continue
        elif x < 0 or x >= len_ or y < 0 or y >= len_:  # out of range
            continue
        elif board_cost[z][y][x] <= cost:  # cost more expensive than dp
            continue
        elif board[y][x] == 1:  # encounter of wall
            continue

        # after pass
        board_cost[z][y][x] = cost

        # if dir == "row"
        if z == 0:
            q.append([0, y, x + 1, cost + 100])
            q.append([0, y, x - 1, cost + 100])
            q.append([1, y + 1, x, cost + 600])
            q.append([1, y - 1, x, cost + 600])
        elif z == 1:
            q.append([0, y, x + 1, cost + 600])
            q.append([0, y, x - 1, cost + 600])
            q.append([1, y + 1, x, cost + 100])
            q.append([1, y - 1, x, cost + 100])

    return answer




print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
# print(solution([[0,0,0,0,0,0,0,0],[1,0,1,1,1,1,1,0],[1,0,0,1,0,0,0,0],[1,1,0,0,0,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,0]]))
