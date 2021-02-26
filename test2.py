def solution(begin, target, words):
    answer = 0
    return answer

begin = 'hit'
target = 'cog'
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog'] #4
length = len(words)

node = [[] for _ in range(length)]

i=0
for word in words[:-1]:
    node[i].append(1)
    i += 1
    j= 0
    for word_2 in words[i:]:
        s = 0

        for w, w2 in zip(list(word), list(word_2)):
            if w != w2: s += 1
        if s == 1:
            node[i+j].append(1)
        else :
            node[i+j].append(0)
        print(i)
        j += 1


print(node)