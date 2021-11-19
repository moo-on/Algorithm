def divisor(n):
    lst=[]
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            lst.append([i, n//i])
    return lst

def solution(brown, yellow):

    for lst in divisor(yellow):
        if brown == (lst[0]*2 + lst[1]*2 + 4):
            lst[0] += 2
            lst[1] += 2
            return list(reversed(lst))