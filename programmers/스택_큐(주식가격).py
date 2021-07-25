def solution(prices):
    answer = []
    for i,e in enumerate(prices):
        cnt = 1
        for n in range(i+1, len(prices)):
            if e>prices[n]:
                answer.append(cnt)
                break
            cnt+=1
        else: answer.append(cnt-1)
    return answer