def swift(board):
    matrix = [[] for _ in range(len(board) + 1)]
    for L in board:
        for i in range(len(board)):
            if L[i] == 0: continue
            matrix[i + 1].insert(0, L[i])
    return matrix


def basket(board, moves):
    lst = []
    result = 0
    while moves:
        m = moves.pop(0)
        if len(board[m]) == 0: continue
        e = board[m].pop()
        lst.append(e)
        if len(lst) >= 2:
            if lst[-2] == lst[-1]:
                del lst[-2]
                del lst[-1]
                result += 2
    return result

def solution(board, moves):
    board = swift(board)
    answer = basket(board, moves)
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(swift(board))
print(solution(board, moves))