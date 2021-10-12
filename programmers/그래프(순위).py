n1 = 5
case1 = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	#2

def solution(n, results):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for result in results:
        graph[result[0]].append(result[1])
    print(graph)
    return answer

solution(n1, case1)