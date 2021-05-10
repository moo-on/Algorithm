def solution(numbers, target):
    answer = 0
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3  # return 5
answer = 0

def DFS(numbers, idx, value, target):
    global answer
    # if idx == len(numbers) and value == target: answer +=1
    # if idx == len(numbers): return

    if idx == len(numbers):
        if value == target: answer += 1
        else: return
        return


    DFS(numbers, idx + 1, value + numbers[idx], target)
    DFS(numbers, idx + 1, value - numbers[idx], target)


DFS(numbers, 0,0, target)
print(answer)