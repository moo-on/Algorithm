def solution(m, n, puddles):
    m, n = n, m
    matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    matrix[0][1] = 1

    for puddle in puddles:
        x, y = puddle[1], puddle[0]
        matrix[x][y] = "trap"

    for nx in range(1, m + 1):
        for ny in range(1, n + 1):
            if matrix[nx][ny] == "trap":
                matrix[nx][ny] = 0
                continue
            else:
                matrix[nx][ny] = (matrix[nx - 1][ny] + matrix[nx][ny - 1]) % 1000000007
    return matrix[m][n]


print(solution(4, 3, [[2, 2]]))
