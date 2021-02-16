import sys

number = [
    [0,"A"],[0,"B"],[0,"C"],[0,"D"],[0,"E"],
    [0,"F"],[0,"G"],[0,"H"],[0,"I"],[0,"J"]
]

def solution():
    N = int(sys.stdin.readline())

    arr = [0 for _ in range(10)]
    for i in range(N):
        word = sys.stdin.readline().strip()
        for j in range(len(word)):
            index = ord(word[len(word) - 1 - j]) - 65
            if j == len(word) - 1:
                arr[index] = 1
            number[index][0] = number[index][0] + 10 ** j

    number.sort(reverse=True)
    if number[9][0] != 0:
        for i in range(9, -1, -1):
            if arr[ord(number[i][1]) - 65] == 0:
                temp = list(number[i])
                number.remove(temp)
                number.append(temp)
                break

    ret = 0
    for i in range(10):
        ret += number[i][0] * (9 - i)
    print(ret)

solution()