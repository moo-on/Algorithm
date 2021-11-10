# price	money	count	result
# 3	20	4	10

def solution(price, money, count):
    return int(0 if price*count*(count+1)/2 < money else price*count*(count+1)/2-money)
