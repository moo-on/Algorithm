'''
dfs 종료 조건
    해당 경로가 더 비싼 루트
    벽에 막혀있다. & 격자 보다 크다
    목적지에 도착했을 때

다음 함수 부를 때
    방향성에 대한 비용 증가
    내가 가진 방향
'''


def solution(board):
    answer = [999999999,0]

    def dfs(y, x, cost, dir, lst):
        if x < 0 or x >= len_ or y < 0 or y >= len_:
            return
        elif board_cost[y][x] <= cost:
            return
        elif board[y][x] == 1:
            return
        elif x == len_ - 1 and y == len_ - 1:
            if answer[0] > cost:
                answer[0] = cost
                answer[1] = lst
            return

        board_cost[y][x] = cost
        lst.append([y,x])
        if dir == "row":
            dfs(y, x + 1, cost + 100, "row", lst)
            dfs(y, x - 1, cost + 100, "row", lst)
            dfs(y + 1, x, cost + 600, "col", lst)
        if dir == "col":
            dfs(y, x + 1, cost + 600, "row", lst)
            dfs(y, x - 1, cost + 600, "row", lst)
            dfs(y + 1, x, cost + 100, "col", lst)

    len_ = len(board)
    board_cost = [[99999 for _ in range(len_)] for _ in range(len_)]

    dfs(1, 0, 100, "col",[])
    board_cost = [[99999 for _ in range(len_)] for _ in range(len_)]
    dfs(0, 1, 100, "row",[])

    return answer[0]


#print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
               # [0, 0, 0, 0, 0, 0]]))

print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
