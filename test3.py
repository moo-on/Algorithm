#
#

# 상하좌우 패턴이 같으므로 하나의 컴포넌트 완성 후 돌려서 합친다.
def rotated(a):
    n = len(a)
    m = len(a[0])

    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


def solution(n, clockwise):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    up = [[0 for _ in range(n)] for _ in range(n)]

    # up, 만들기 쉬운 컴포넌트 제작
    start, end = 0, n - 1
    cnt = 1
    for i in range(n // 2):  # 짝수 6 ->3개 블럭, 홀수 9 -> 4개 블럭
        for j in range(start, end):
            up[i][j] = cnt
            cnt += 1
        start += 1
        end -= 1

    # 각 컴포넌트를 돌려서 만들어 준다.
    right = rotated(up)
    down = rotated(right)
    left = rotated(down)

    # 합치기
    for i in range(n):
        for j in range(n):
            answer[i][j] += (up[i][j] + right[i][j] + down[i][j] + left[i][j])

    # 홀수
    if n % 2 == 1:
        answer[n // 2][n // 2] = answer[n // 2][n // 2 - 1] + 1

    # 반시계
    if clockwise == False:
        for i in range(n):
            answer[i].reverse()

    return answer


print(solution(6, False))
