
n =3
ll = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def solution(n, computers):

    parent =find_parent(computers)

    for i in range(n):
        parent[i] = union_parent(parent, i)

    answer = len(set(parent))

    return answer

def find_parent(computers):
    parent = []
    for L  in computers:
        for i, e in enumerate(L):
            if e ==1:
                parent.append(i)
                break
    return parent

def union_parent(parent,x):
    if parent[x] != x:
        return union_parent(parent,parent[x])
    return parent[x]

print(solution(n, ll))

print(find_parent())






