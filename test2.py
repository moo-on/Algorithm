answer = 0

def solution(begin, target, words):
    global answer

    if target not in words:
        return 0
    visited = [0 for i in words]
    dfs(begin, target, words, visited)




    return answer

def dfs(begin, target, words, visited):
    global answer

    stacks = [begin]
    modify_lst = []

    while stacks:

        stack = stacks.pop(0)
        n=0
        if stack == target:
            return answer
        for i in range(len(words)):

            if visited[i] == 1: continue
            if len([s1 for s1, s2 in zip(words[i], stack) if s1 == s2]) == 1:
                visited[i] = 1
                stacks.append(words[i])
                n += 1

        modify_lst.append(n)

        answer += 1

a = solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])
print(a)