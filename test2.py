def solution(n, computers):
    answer = 0

    for i,l in enumerate(computers):
        for j,e in enumerate(l):
            if e ==1:
                computers[i] = j
                break

    for i,e in enumerate(computers):
        computers[i] = computers[e]

    return len(set(computers))


n = 3
lst = [[1, 1, 0], [1, 1, 0], [0, 0, 1]] # return 2
#lst = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, lst))



# def solution(n, computers):
#     answer = 0
#     visited = [0 for _ in range(n)]
#
#     def DFS(computers, n, start, visited):
#         stack = [start]
#         while stack:
#             j = stack.pop()
#             visited[j] = 1
#             for i in range(n):
#                 if computers[j][i] == 1 and visited[i] ==0:
#                     stack.append(i)
#
#     i = 0
#     while 0 in visited:
#         if visited[i] == 0:
#             DFS(computers, n, i, visited)
#             answer += 1
#         i += 1
#
#     return answer