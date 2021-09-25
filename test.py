case1 = [3, 0, 6, 1, 5]  # 3
case2 = [12,11,10,9,8,1] # 5

# 인용횟수는 10000이하
# 길이는 1000이하
def solution(citations):
    length = len(citations)
    citations.sort()
    if citations[-1] == 0 : return 0
    for citation in citations:
        if citation == length: return length
        if citation > length:
            return length
        length -= 1

# 0 1 3 5 6
# 5 4 3 2 1

print(solution(case2))
print(solution(case1))