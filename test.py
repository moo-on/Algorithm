def permute(lst, r):
    results = []
    prev_elements = []

    def dfs(elements):
        if len(elements) ==(len(lst)-r):
            results.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(lst)
    return results

print(permute([1,2,3], 2))
































#체크리스트와 DFS를 이용한 순열 출력, 문제점 : result가 저장이 안됌.
# def DFS(L) :
#     #종료조건
#     if L== r:
#         print(result)
#     #재귀문
#     else :
#         for i in range(len(n)):
#             if checklist[i]==0:
#                 result[L] =n[i]
#                 checklist[i] = 1
#                 DFS(L+1)
#     #백트래버스
#                 checklist[i] = 0




