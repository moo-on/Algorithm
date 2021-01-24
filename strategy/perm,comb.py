#체크리스트와 DFS를 이용한 순열 출력, 문제점 : result가 저장이 안됌.

def perm(n, r):
    results =[]
    checklist = [0]*len(n)
    result= [0]*r
    def DFS(L) :
        #종료조건
        if L== r:
            print(result)
            results.append(result[:])
        #재귀문
        else :
            for i in range(len(n)):
                if checklist[i]==0:
                    result[L] =n[i]
                    checklist[i] = 1
                    DFS(L+1)
        #백트래버스
                    checklist[i] = 0
    DFS(0)
    return results

print(perm([1,2,3],2))




#조합1
# def comb(lst, n):
#     ret = []
#     if n > len(lst): return ret
#
#     if n == 1:
#         for i in lst:
#             ret.append([i])
#     elif n > 1:
#         for i in range(len(lst) - n + 1):
#             for temp in comb(lst[i + 1:], n - 1):
#                 ret.append([lst[i]] + temp)
#
#     return ret

#순열1
# def perm(lst, n):
#     ret = []
#     if n > len(lst): return ret
#
#     if n == 1:
#         for i in lst:
#             ret.append([i])
#     elif n > 1:
#         for i in range(len(lst)):
#             temp = [i for i in lst]
#             temp.remove(lst[i])
#             for p in perm(temp, n - 1):
#                 ret.append([lst[i]] + p)
#    return ret



#순열2
# def permute(lst, r):
#     results = []
#     prev_elements = []
#
#     def dfs(elements):
#         if len(elements) ==(len(lst)-r):
#             results.append(prev_elements[:])
#
#         for e in elements:
#             next_elements = elements[:]
#             next_elements.remove(e)
#
#             prev_elements.append(e)
#             dfs(next_elements)
#             prev_elements.pop()
#
#     dfs(lst)
#     return




