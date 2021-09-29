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


# 노드의 개수와 간선(Union 연산) 입력 받기
v = 6
_input = [[1, 2], [1, 4], [2, 3], [5, 6]]
_input = [[1, 2], [2, 3], [3, 4], [4, 5]]
_input = [[1, 3], [1, 6], [2, 4], [4, 6]]

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
parent = [i for i in range(v + 1)]

# Union 연산을 각각 수행
for e in _input:
    union_parent(parent, e[0], e[1])
print(parent)
# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

# v=6
# e=4

# 1 2
# 1 4
# 2 3
# 5 6
