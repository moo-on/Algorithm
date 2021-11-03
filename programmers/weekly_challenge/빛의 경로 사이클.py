# ["SL","LR"]	[16]
# ["S"]	[1,1,1,1]
# ["R","R"]	[4,4]

def solution(grid):
    # 현재 노드의 이름과 들어온 방향을 알려주면, 다음 방향을 알려줌
    def next(string, direction):
        if string == "L":
            return (direction - 1) % 4
        elif string == "R":
            return (direction + 1) % 4
        elif string == "S":
            return direction

    # 다음 위치를 알려주면, 알맞은 좌표로 바꿔줌
    def position(nx, ny):
        if nx < 0: nx = len(grid) - 1
        if nx > len(grid) - 1: nx = 0
        if ny < 0: ny = len(grid[0]) - 1
        if ny > len(grid[0]) - 1: ny = 0
        return nx, ny

    # 동남서북 = 0123
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    answer = []
    check_lst = [[[0 for _ in range(4)] for _ in range(len(grid[i]))] for i in range(len(grid))]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for i in range(4):
                nx, ny, dir = x, y, i
                node = grid[nx][ny]

                cnt = 0
                while 1:
                    dir = next(node, dir)
                    if check_lst[nx][ny][dir] == 0:
                        check_lst[nx][ny][dir] = 1
                        nx, ny = position(nx + dx[dir], ny + dy[dir])
                        node = grid[nx][ny]
                        cnt += 1
                    else:
                        answer.append(cnt)
                        break

    return sorted([e for e in answer if e != 0])


print(solution(["SL", "LR"]))
print(solution(["S"]))
print(solution(["R", "R"]))
print(solution(["SLLR", "RRRR"]))
