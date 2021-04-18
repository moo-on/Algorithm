from collections import Counter
from itertools import combinations

def solution(number, k):
    answer = ''
    return answer

number = '1924'
k=2

lst = combinations(list( number),k)
print(list(lst))
answer = []

for l in list(lst):
    string = ''.join(l)
    answer.append(int(string))

print(answer)

print(max(answer))


string = ''.join(['1','2'])



