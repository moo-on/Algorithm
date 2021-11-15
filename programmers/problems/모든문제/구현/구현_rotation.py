input = ['1', '234', '56789']

from collections import deque


def rotation(graph):
    rotation_tree = [deque() for _ in range(len(graph))]

    for i, lst in enumerate(graph):
        for i2, e2 in enumerate(lst):
            if i2 == 0:
                rotation_tree[i].appendleft(e2)
            else:
                rotation_tree[i - (i2 + 1) // 2].appendleft(e2)
    rotation_tree.reverse()

    return rotation_tree


def solution(tree):
    answer = ""

    rotation_tree = rotation(tree)
    rotation_tree = rotation(rotation_tree)
    print(rotation_tree)

    return answer


print(solution(input))