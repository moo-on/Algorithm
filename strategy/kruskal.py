# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


answer = 0

# 노드의 개수와 간선(Union 연산) 입력 받기
v = 4
_input = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
parent = [i for i in range(v)]

# Union 연산을 각각 수행
_input.sort(key=lambda x: x[2])

for e in _input:
    if find_parent(parent, e[0]) != find_parent(parent, e[1]):
        union_parent(parent, e[0], e[1])
        answer += e[2]

print(answer)



