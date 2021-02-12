import sys
input = sys.stdin.readline

#원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

#두 원소 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a< b:
        parent[b] = a
    else:
        parent[a] = b

#노드&간선 입력
v, e = map(int, input().split())

#부모테이블 초기화
parent = [0]*(v+1)
for i in range(1, v+1):
    parent[i] = i

#union연산
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

#각 원소 속한 집합
print('각 원소가 속한 집합:')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print("\n부모테이블")

#부모테이블
for i in range(1, v+1):
    print(parent[i], end = ' ')

