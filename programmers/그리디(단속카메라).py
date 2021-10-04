case1 = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]  # 2

from collections import deque


def solution(routes):
    camera = []
    routes.sort(key=lambda x: (x[1], x[0]))  # 가장 빨리 나가는 순서
    routes = deque(routes)

    route = routes.popleft()
    camera.append(route[1])  # 가장 빨리 나가는 차량의 종착점에 카메라 추가
    while routes:
        # 시작점이 카메라보다 더 뒤에 있다면
        while routes[0][0] <= camera[-1] <= routes[0][1]:
            routes.popleft()
            if not routes: break
        if not routes: break
        # 시작점이 카메라 앞에 있다면
        if routes[0][0] > camera[-1]:
            route = routes.popleft()
            camera.append(route[1])

    return len(camera)


print(solution(case1))
