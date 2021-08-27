def solution(price):
    answer_lst = []
    for i in range(len(price)):
        answer_lst.append(solve(price[i:]))
    return answer_lst

def solve(lst):
    target = 1000000000
    chance = True
    share, remainder = divmod(100000000, lst[0])
    for i in range(1,len(lst)):
        if share*lst[i] + remainder >= target:
            return i
        elif lst[0] >= lst[i]*2 and chance:
            temp_1, remainder = divmod(50000000+remainder, lst[i])
            share += temp_1
            target += 50000000
            chance = False
    return -1

print(solution([78000,48000,27000,285000,320000,335100]))
print(solution([34000,78000,48000,27000,11000,285000,320000,335100]))