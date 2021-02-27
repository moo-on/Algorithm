import sys

input = sys.stdin.readline


def main():
    n = int(input())
    lst = list(map(int, input().split()))

    visited =[0 for _ in range(n)]
    answers = []

    def DFS(lst, visited, start):
        stack = [lst[start]]
        visited[start] = 1
        now = start
        answer = 1
        while stack:
            e = stack.pop()

            if visited[e+now] == 0 :
                visited[e+now] = 1
                stack.append(lst[e+now])
                now = e+now
                answer += 1
            else: return answer+1
    for i in range(3):
        answers.append(DFS(lst, visited, i))
    print(max(answers))


if __name__ == "__main__":
    main()