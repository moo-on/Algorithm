answer = -1

def DFS(n, pos, num, number, s):
    global answer
    if pos > 8:
        return
    if num == number:
        if pos < answer or answer == -1:
            #print(s)            
            answer=pos
        return

    nn=0
    for i in range(8):
        nn=nn*10+n
        DFS(n, pos+1+i, num+nn, number, s+'+')
        DFS(n, pos+1+i, num-nn, number, s+'-')
        DFS(n, pos+1+i, num*nn, number, s+'*')
        DFS(n, pos+1+i, num/nn, number, s+'/')

def solution(N, number):    
    DFS(N, 0, 0, number, '')    
    return answer


print(solution(8, 53))