n1 = 6
edge1 = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	#3

def DFS(answer_lst, check, edge, i, n):
    for e in edge[i]:
        if check[e] == 1 :
            continue
        else:
            check[e] = 1
            if answer_lst[e] > n: answer_lst[e] = n
            DFS(answer_lst, check, edge, e, n+1)

def solution(n, edge):
    answer_lst  = [20002 for _ in range(n+1)]
    check_lst = [0 for _ in range(n+1)]
    lst = [set() for _ in range(n+1)]

    for e in edge:
        lst[e[0]].add(e[1])
        lst[e[1]].add(e[0])

    print(lst)

    DFS(answer_lst, check_lst, lst, 1,1)

    print(answer_lst)
    return 1







solution(n1, edge1)