for i in range(3,-1,-1):
    print(i)


word_1 = [1,2,3,3]
word_2 = [2,3,3,3]
lst = [x!=y for x, y in zip(word_1, word_2)]
print(sum(lst))

lst = [1,2,3,4]
for i in range(len(lst)):
    lst.pop()
    print(i)